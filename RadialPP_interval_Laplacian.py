from firedrake import *

# attempt to solve 1/r d/dr (r du/dr) = -1 homog. Dirichlet problem in 1D on [1,2]

# solution ought to be 7/4-3/(2r)-r^2/4

# multiply by r v on both sides and integrate to get primal weak form

mesh = IntervalMesh(100,1,2)

#primal formulation
V = FunctionSpace(mesh, "CG", 1)
u = TrialFunction(V)
v = TestFunction(V)
w = Function(V)
x = SpatialCoordinate(mesh)
w.interpolate(x[0])  # this is supposed to be r

a = (w*inner(grad(u),grad(v)))*dx

L = (w*v)*dx

g = Function(V)

#BCs
bc1 = DirichletBC(V, 0.0, 1)
bc2 = DirichletBC(V, 0.0, 2)

solve(a == L, g, bcs=[bc1, bc2])  #has strongly imposed BCs

File("RadialPP_interval_Laplacian_primal.pvd").write(g)
