pip install pgmpy

from pgmpy.models import MarkovNetwork
from pgmpy.factors.discrete import DiscreteFactor

# Define the network structure
model = MarkovNetwork()
model.add_edges_from([('A', 'B'), ('B', 'C'), ('A', 'C')])

# Define potential functions
phi_ab = DiscreteFactor(['A', 'B'], cardinality=[2, 2], values=[1, 2, 2, 1])
phi_bc = DiscreteFactor(['B', 'C'], cardinality=[2, 2], values=[1, 3, 3, 1])
phi_ac = DiscreteFactor(['A', 'C'], cardinality=[2, 2], values=[1, 4, 4, 1])

# Add potentials to the model
model.add_factors(phi_ab, phi_bc, phi_ac)

# Check
model.check_model()

# Query or process information (implementation of inference for Markov Networks is more custom).
print(model)

# Get the factors
factors = model.get_factors()
for factor in factors:
    print(factor)

# Get the cardinality of nodes
cardinality = model.get_cardinality()
print(cardinality)
