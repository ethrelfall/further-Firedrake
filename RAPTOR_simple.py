from firedrake import *

# attempt to solve du/dr + d/dr (r du/dr) + 1 = 0 Dirichlet problem in 1D on [1,2] with u(1)=2 and u(2)=1

# solution ought to be 3/2+1/(r)-r/2

# multiply by v on both sides and integrate to get primal weak form

mesh = IntervalMesh(100,1,2)

#primal formulation
V = FunctionSpace(mesh, "CG", 1)
u = TrialFunction(V)
v = TestFunction(V)
w = Function(V)
x = SpatialCoordinate(mesh)
w.interpolate(x[0])  # this is supposed to be r

a = (u*grad(v)[0]+w*inner(grad(u),grad(v)))*dx

L = (v)*dx

g = Function(V)

#BCs
bc1 = DirichletBC(V, 2.0, 1)
bc2 = DirichletBC(V, 1.0, 2)

solve(a == L, g, bcs=[bc1, bc2])  #has strongly imposed BCs

File("RAPTOR_simple.pvd").write(g)
