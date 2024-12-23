pip install pgmpy

from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

# Define network structure
model = BayesianNetwork([('Rain', 'WetGrass'), ('Sprinkler', 'WetGrass')])

# Define probabilitites
from pgmpy.factors.discrete import TabularCPD

cpd_rain = TabularCPD(variable = 'Rain', variable_card = 2, values = [[0.7], [0.3]])
cpd_sprinkler = TabularCPD(variable = 'Sprinkler', variable_card = 2, values = [[0.6], [0.4]])
cpd_wetgrass = TabularCPD(variable = 'WetGrass', variable_card = 2, values = [[0.99, 0.9, 0.8, 0.0], [0.01, 0.1, 0.2, 1.0]],
                          evidence = ['Rain', 'Sprinkler'], evidence_card = [2, 2])

# Add cpd
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wetgrass)

# Check
model.check_model()

# Inference
inference = VariableElimination(model)
prob_wetgrass = inference.query(variables = ['WetGrass'], evidence={'Rain': 1, 'Sprinkler': 0})
print(prob_wetgrass)
