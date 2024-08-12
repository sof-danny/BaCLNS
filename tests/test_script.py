import sys
import os

# Add the root directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sympy as sp
import numpy as np
from baclns import generic_backstepping_controller, simulate_system, plot_responses, save_responses

# 1. Define system parameters and state equations

num_states = 2
x1, x2 = sp.symbols('x1 x2')
u = sp.Symbol('u')
a, b = sp.symbols('a b')

# Define the state equations for a 2D system
state_equations = [
    a * x1 + x2,
    b * x2 + u
]

# Define the gains
gains_vals = [10.0, 15.0]

# 2. Create the control law using generic_backstepping_controller

final_control_law, states, gains = generic_backstepping_controller(num_states, state_equations, 'u', gains_vals)

# 3. Define simulation parameters

time = np.linspace(0, 10, 500)  # 10 seconds of simulation with 500 time steps
initial_conditions = [1.0, 0.0]  # Initial conditions for x1, x2
params_subs = {a: 1.0, b: 0.5, 'k1': gains_vals[0], 'k2': gains_vals[1]}

# 4. Simulate the system

state_values, control_inputs, errors = simulate_system(
    final_control_law, states, gains_vals, initial_conditions, time, state_equations, params_subs, 
    plot=True, print_law=True
)

# 5. Plot the results

plot_responses(time, state_values, control_inputs, errors)

# 6. Save the results to a JSON file

#save_responses(time, state_values, control_inputs, 'test_results.json', errors)
plot_responses(time, state_values, control_inputs, errors, save_folder='plots')
