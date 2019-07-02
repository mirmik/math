#include <linalg-v3/linalg.h>
#include <linalg-v3/linalg-ext.h>
#include <math.h>

#include <igris/math/deg.h>
#include <nos/print.h>

constexpr double phi = deg(20.);
constexpr double psi = deg(25.);

using namespace linalg;
using namespace linalg::aliases;
using namespace linalg::ostream_overloads;

int main() 
{
	quat<double> q0 = {sin(phi/2), 0, 0, cos(phi/2)};
	quat<double> q1 = {0, 0, sin(psi/2), cos(psi/2)};

	PRINT(q0);
	PRINT(q1);

	double3 v0 = qrot(q0, double3{0,0,1.});
	double3 v1 = qrot(q1, double3{1.,0,0});
	
	auto v01 = cross(v0, v1);
	v01 = normalize(v01);

	PRINT(v0);
	PRINT(v1);
	PRINT(v01);

	nos::println();

//	auto p0 = q0.w;
//	auto p1 = q0.z;
//	auto pz = p0*p0 - p1*p1;

	auto x = v01.x;
	auto y = v01.y;
	auto z = v01.z;

	auto theta = asin(-x);
	auto omega = asin(z/cos(theta));

	quat<double> q10 = {0, 0, sin(theta/2), cos(theta/2)};
	quat<double> q11 = {sin(omega/2), 0, 0, cos(omega/2)};
	
	auto q = q11 * q10;
	auto vq = qrot(q, double3(0,1,0));

	PRINT(qrot(q, {0,0,1}));

	PRINT(q10);
	PRINT(q11);
	PRINT(q);
	
	nos::println();
	PRINT(vq);
	PRINT(v01);
	PRINT(length(q0));
	PRINT(length(q1));
	PRINT(length(q));
	PRINT(length(vq));
	PRINT(length(v01));
}