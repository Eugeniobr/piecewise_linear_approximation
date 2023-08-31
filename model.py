import pyomo.environ as pyo

model = pyo.AbstractModel()

model.J = pyo.Set()

model.c = pyo.Param(model.J)
model.d = pyo.Param(model.J)

model.z = pyo.Var()
model.x = pyo.Var()

def objective(m):
    return m.z

model.obj = pyo.Objective(rule=objective)

def constraint_rule1(m, j):
    return  m.z >= m.c[j] * m.x + m.d[j]
    


model.constraint1 = pyo.Constraint(model.J, rule=constraint_rule1)


