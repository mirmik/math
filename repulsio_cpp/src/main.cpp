#define GLEW_STATIC
#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include <rabbit/camera.h>
#include <rabbit/mesh/mesh.h>
#include <rabbit/opengl/drawer.h>
#include <rabbit/opengl/opengl_shader_program.h>
#include <rabbit/opengl/projection.h>
#include <rabbit/opengl/shader_collection.h>
#include <rabbit/util.h>
#include <ralgo/space/pose3.h>
#include <random>

#define WIDTH 800
#define HEIGHT 600

float random_float(float a, float b)
{
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(a, b);
    return dis(gen);
}

class Ball
{
    linalg::vec<float, 3> _pos;
    linalg::vec<float, 3> _vel;

public:
    Ball(linalg::vec<float, 3> pos, linalg::vec<float, 3> vel)
        : _pos(pos), _vel(vel)
    {
    }

    void update(float dt, linalg::vec<float, 3> A, linalg::vec<float, 3> B)
    {
        _vel += linalg::vec<float, 3>{random_float(-0.01, 0.01),
                                      random_float(-0.01, 0.01),
                                      random_float(-0.01, 0.01)};

        _pos += _vel * dt;

        // if ball is out of box, it velosity is reversed
        /*if (_pos.x < A.x || _pos.x > B.x)
        {
            _vel.x = -_vel.x;
            _pos.x = std::min(std::max(_pos.x, A.x), B.x);
        }
        if (_pos.y < A.y || _pos.y > B.y)
        {
            _vel.y = -_vel.y;
            _pos.y = std::min(std::max(_pos.y, A.y), B.y);
        }
        if (_pos.z < A.z || _pos.z > B.z)
        {
            _vel.z = -_vel.z;
            _pos.z = std::min(std::max(_pos.z, A.z), B.z);
        }*/
    }

    void apply_demping(float dt)
    {
        _vel -= 0.5f * _vel * dt;
    }

    void apply_force(linalg::vec<float, 3> f, float dt)
    {
        _vel += f * dt;
    }

    linalg::vec<float, 3> pos() const
    {
        return _pos;
    }

    linalg::vec<float, 3> vel() const
    {
        return _vel;
    }

    linalg::vec<float, 3> force(const Ball &other,
                                linalg::vec<float, 3> A,
                                linalg::vec<float, 3> B) const
    {

        auto r = _pos - other._pos;
        auto d = length(r);
        auto f = 500.0f / (d * d * d) * r;
        return -f;
    }
};

std::vector<std::pair<rabbit::vec3f, rabbit::vec3f>>
make_box_lines(rabbit::vec3f a, rabbit::vec3f b)
{
    auto xl = a.x;
    auto xr = b.x;
    auto yl = a.y;
    auto yr = b.y;
    auto zl = a.z;
    auto zr = b.z;

    std::vector<std::pair<rabbit::vec3f, rabbit::vec3f>> res = {
        {{xl, yl, zl}, {xr, yl, zl}},
        {{xl, yl, zl}, {xl, yr, zl}},
        {{xl, yl, zl}, {xl, yl, zr}},
        {{xr, yr, zr}, {xl, yr, zr}},
        {{xr, yr, zr}, {xr, yl, zr}},
        {{xr, yr, zr}, {xr, yr, zl}},
        {{xr, yl, zl}, {xr, yr, zl}},
        {{xr, yl, zl}, {xr, yl, zr}},
        {{xl, yr, zl}, {xr, yr, zl}},
        {{xl, yr, zl}, {xl, yr, zr}},
        {{xl, yl, zr}, {xr, yl, zr}},
        {{xl, yl, zr}, {xl, yr, zr}}};

    return res;
};

std::vector<Ball> create_balls(
    int n, rabbit::vec3f A, rabbit::vec3f B, float velmin, float velmax)
{
    // make n balls in random points of box A, B
    std::vector<Ball> res;
    for (int i = 0; i < n; ++i)
    {
        auto x = random_float(A.x, B.x);
        auto y = random_float(A.y, B.y);
        auto z = random_float(A.z, B.z);
        auto vx = random_float(velmin, velmax);
        auto vy = random_float(velmin, velmax);
        auto vz = random_float(velmin, velmax);
        res.push_back(Ball({x, y, z}, {vx, vy, vz}));
    }
    return res;
}

linalg::vec<float, 4> position_to_color(linalg::vec<float, 3> pos,
                                        linalg::vec<float, 3> A,
                                        linalg::vec<float, 3> B)
{
    // map position to color. red in center, blue in faces
    auto xc = (A.x + B.x) / 2.0f;
    auto yc = (A.y + B.y) / 2.0f;
    auto zc = (A.z + B.z) / 2.0f;
    auto x = std::abs(pos.x - xc);
    auto y = std::abs(pos.y - yc);
    auto z = std::abs(pos.z - zc);
    auto r = std::max(std::max(x, y), z);
    auto g = 0.0f;
    auto b = 1.0f - r;
    return {r, g, b, 1.0f};
}

int main()
{
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_RESIZABLE, GL_FALSE);
    GLFWwindow *window =
        glfwCreateWindow(WIDTH, HEIGHT, "LearnOpenGL", nullptr, nullptr);
    glfwMakeContextCurrent(window);
    glewExperimental = GL_TRUE;
    glewInit();
    glViewport(0, 0, WIDTH, HEIGHT);
    glEnable(GL_BLEND);

    auto drawer = rabbit::opengl_drawer();
    drawer.init_opengl_context();
    auto surf = rabbit::sphere_surface(0.3);
    auto mesh = rabbit::surface_rubic_mesh(surf, 30, 20);

    float aspect = (float)WIDTH / (float)HEIGHT;
    rabbit::mat4f projection =
        rabbit::opengl_perspective(rabbit::deg(100) / aspect, aspect, 0.1, 100);

    rabbit::camera camera;

    auto color = rabbit::vec4f{1, 0.7, 0.7, 1};
    auto white = rabbit::vec4f{1, 1, 1, 1};

    auto A = rabbit::vec3f{-10, -10, -10};
    auto B = rabbit::vec3f{10, 10, 10};

    std::vector<std::pair<rabbit::vec3f, rabbit::vec3f>> cube_lines =
        make_box_lines(A, B);

    std::vector<Ball> balls; // = create_balls(2, A, B, -10, 10);
    balls.push_back(Ball({0, -5, 0}, {5, 0, 0}));
    balls.push_back(Ball({0, 5, 0}, {-5, 0, 0}));

    while (!glfwWindowShouldClose(window))
    {
        double delta = 0.01;
        glfwPollEvents();
        drawer.clean(0.2f, 0.3f, 0.3f, 1.0f);

        auto curtime = glfwGetTime();
        camera.set_eye(rabbit::vec3f{float(20 + 0.1 * cos(curtime * 16)),
                                     float(20 + 0.1 * sin(curtime * 16)),
                                     18});
        camera.correct_up();
        camera.set_target(rabbit::vec3f{0, 0, 0});

        for (auto &ball : balls)
        {
            for (auto &other : balls)
            {
                if (&ball == &other)
                    continue;

                auto f = ball.force(other, A, B);
                ball.apply_force(f, delta);
            }

            // ball.apply_demping(delta);
            ball.update(delta, A, B);

            auto color = position_to_color(ball.pos(), A, B);

            drawer.draw_mesh(
                mesh,
                ralgo::pose3<float>({0, 0, 0, 1}, ball.pos()).to_mat4(),
                camera.view_matrix(),
                projection,
                color);
        }

        for (auto &line : cube_lines)
        {
            drawer.draw_line(line.first,
                             white,
                             line.second,
                             white,
                             ralgo::pose3<float>().to_mat4(),
                             camera.view_matrix(),
                             projection);
        }

        glfwSwapBuffers(window);
    }

    glfwTerminate();
    return 0;
}