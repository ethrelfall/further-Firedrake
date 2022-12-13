# further-Firedrake

I want to solve

$$
\frac{1}{r} \frac{d}{dr} \left ( r \frac{d u}{dr} \right ) = -1
$$

on the interval $[1,2]$.

Get a weak form by multiplying the equation by $r$ and then by the test function $v$ and integrating.  Throwing away a boundary term this is then

$$
-\int_1^2 r \frac{du}{dr} \frac{dv}{dr} dr = - \int_1^2 r v dr.
$$

The solution ought to be

$$
u = \frac{7}{4} - \frac{3}{2r} - \frac{r^2}{4}.
$$
