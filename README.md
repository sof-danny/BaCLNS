# BaCLNS: Efficient Backstepping Control for Linear and Nonlinear Dynamic Systems

BaCLNS (Backstepping Control for Linear and Nonlinear Systems) is a Python package designed to provide efficient and robust control solutions for dynamic systems (Control Affine Systems) using backstepping techniques. This package offers a flexible and user-friendly interface for designing, simulating, and analyzing control systems, with options for plotting and saving results.

Introduction to Backstepping Control

Backstepping is a systematic and recursive control design technique primarily used for stabilizing nonlinear systems. Unlike traditional control methods that might struggle with complex nonlinearities, backstepping breaks down the control problem into smaller, more manageable sub-problems. These sub-problems are then solved sequentially, "stepping back" from the output to the input, hence the name "backstepping."

Key Concepts:

Virtual Control: Intermediate control laws are designed for each state, leading to the final control input.
Lyapunov Function: A mathematical function that helps ensure system stability. Backstepping uses this function to guide the control design process.
Recursive Design: The control input is designed by recursively stabilizing each state in the system.

Worked examples can be found in [this paper]( https://doi.org/10.1016/B978-0-12-817582-8.00008-8)


## Installation

To install the package, simply run:

```bash
pip install BaCLNS
```

## Usage

1. Importing the Package
To use the package, import the necessary functions:

```bash
import sympy as sp
import numpy as np
from baclns import generic_backstepping_controller, simulate_system, plot_responses, save_responses
```

2. Define the System 
First, define your system's state equations and parameters. For example, if you have a 3D system:

```bash
# Define system parameters
num_states = 3

x1, x2, x3 = sp.symbols('x1 x2 x3')
u = sp.Symbol('u')
a, b, c = sp.symbols('a b c')

# Define the state equations for a 3D system
state_equations = [
    a * x1 + x2,
    b * x2 + x3,
    c * x3 + u
]

# Define the gains
gains_vals = [10.0, 10.0, 15.0]
```
3. Creating the Control Law
Use the 'generic_backstepping_controller' function to create the control law for your system:

```bash
final_control_law, states, gains = generic_backstepping_controller(num_states, state_equations, 'u', gains_vals)
```

4. Simulating the System
Simulate the system using the 'simulate_system' function. You can configure it to print the control law, plot the results, and save the responses:

```bash 
# Simulation parameters
time = np.linspace(0, 10, 1000)  # 10 seconds of simulation with 1000 time steps
initial_conditions = [0.1, 0.0, 0.1]  # Initial conditions for x1, x2, x3
params_subs = {a: 1.0, b: 0.5, c: 0.2, 'k1': gains_vals[0], 'k2': gains_vals[1], 'k3': gains_vals[2]}

# Simulate the system
state_values, control_inputs, errors = simulate_system(
    final_control_law, states, gains_vals, initial_conditions, time, state_equations, params_subs, 
    plot=True, save_path='results.json', print_law=True
)
```

5. Plotting the Results
If you haven't plotted the results directly in the simulation, you can use the plot_responses function to plot the states, control inputs, and errors on separate plots:

```bash
plot_responses(time, state_values, control_inputs, errors)
```

6. Saving the Results
The results can be saved to a JSON file for later analysis. The simulate_system function allows you to save the results directly during the simulation by specifying the save_path:

```bash
simulate_system(final_control_law, states, gains_vals, initial_conditions, time, state_equations, params_subs, save_path='results.json')
```

Alternatively, you can save the results after the simulation using the 'save_responses' function:

```bash
save_responses('results.json', time, state_values, control_inputs)
```

## Example Workflow: 2D Linear system

```bash
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

save_responses(time, state_values, control_inputs, 'test_results.json', errors)
```


## Example Results

### State Response
![State Response](https://github.com/sof-danny/BaCLNS/blob/main/tests/states_response.png)

### Errors Over Time
![Errors](https://github.com/sof-danny/BaCLNS/blob/main/tests/errors.png)

### Control Input
![Control Input](https://github.com/sof-danny/BaCLNS/blob/main/tests/control_input.png)

...

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/sof-danny/BaCLNS/blob/main/LICENSE) file for details.



## Contact 
If you have questions or issues using the package or understanding Backstepping techniques, please reach out to [Samuel Folorunsho](https://github.com/sof-danny)

## Citation
If you find this useful for your class or research, please cite:

[BaCLNS: A toolbox for fast and efficient control of Linear and Nonlinear Control Affine Systems](https://www.arxiv.org/pdf/2409.09609)

