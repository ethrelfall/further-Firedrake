# further-Firedrake

# Warm-up

I want to solve

$$
\frac{1}{r} \frac{d}{dr} \left ( r \frac{d u}{dr} \right ) = -1
$$

on the interval $[1,2]$ with homogeneous Dirichlet conditions (i.e. $u=0$) at the end points.

Get a weak form by multiplying the equation by $r$ and then by the test function $v$ and integrating.  Throwing away a boundary term (the boundary conditions will be strongly enforced by constraining the test functions) this is then

$$
-\int_1^2 r \frac{du}{dr} \frac{dv}{dr} dr = - \int_1^2 r v dr.
$$

The solution ought to be

$$
u = \frac{1}{4} + \frac{3}{4 \ln 2} \ln r - \frac{r^2}{4}.
$$

See RadialPP_interval_Laplacian.py for Firedrake implementation, which closely reproduces the analytic answer.

# Equation from RAPTOR

This is, writing $u$ instead of $\psi$ and $r$ instead of $\hat{\rho}$,

$$
m_{u} \frac{\partial u}{\partial t} = a_{u} \frac{\partial u}{\partial r} + \frac{\partial}{\partial r} \left (  d_{u} \frac{\partial u}{\partial r} \right ) + s_{u}.
$$

It is easy to put this into a weak form with Dirichlet BCs at two endpoints in $r$.  Here is a simple example where the time-derivative vanishes:

$$
u' + \left ( r u' \right )' + 1 = 0.
$$

The weak form, again having discarded the boundary terms, is

$$
\int_1^2 u v' dx + \int_1^2 r u' v' dx = \int_1^2 v dx.
$$

Let us take inhomogeneous Dirichlet BCs on the interval $r \in [1,2]$ $u(1)=2$ and $u(2)=1$, then the analytic solution is

$$
u = \frac{3}{2} +\frac{1}{r} - \frac{r}{2}.
$$

See RAPTOR_simple.py for Firedrake implementation, which again closely reproduces the analytic solution.
