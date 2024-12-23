import numpy as np

# Define states and transition matrix
states = ['Sunny', 'Rainy']
transition_matrix = np.array([[0.8, 0.2], [0.4, 0.6]])

# Simulate
current_state = 1  # Start with Sunny
days = 10
weather_seq = []

for i in range(days):
    weather_seq.append(states[current_state])
    current_state = np.random.choice([0, 1], p=transition_matrix[current_state])

print("Weather sequence:", weather_seq)
