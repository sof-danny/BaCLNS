import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import json

def simulate_system(final_control_law, states, gains, initial_conditions, time, state_equations, params_subs, save_path=None, plot=False, print_law=False):
    # Substitute the gains and parameters with their numerical values
    final_control_law_num = final_control_law.subs(params_subs)
    
    # Convert the control law to a numerical function
    control_law_func = sp.lambdify(states, final_control_law_num, modules='numpy')
    
    # Simulation parameters
    dt = time[1] - time[0]
    num_states = len(states)
    
    # Initialize state values and errors
    state_values = [np.array([float(ic)]) for ic in initial_conditions]
    control_inputs = []
    errors = []
    
    # Simulation loop
    for t in time[1:]:
        current_values = [float(state[-1]) for state in state_values]
        
        # Compute the control input
        u_curr = control_law_func(*current_values)
        control_inputs.append(u_curr)
        
        # Update the system using Euler's method
        next_values = []
        current_errors = []
        for i in range(num_states):
            # Substitute the gains and parameters into state equations
            state_eq_num = state_equations[i].subs(params_subs)
            # Create a numerical function for the state equations
            state_dot_func = sp.lambdify(tuple(states) + (sp.Symbol('u'),), state_eq_num, modules=['numpy'])
            state_dot = state_dot_func(*current_values, u_curr)
            
            # Ensure state_dot is fully evaluated
            state_dot = float(state_dot)
            
            next_value = current_values[i] + state_dot * dt
            next_values.append(next_value)
            
            # Calculate error (difference between current and next state value)
            error = next_value - current_values[i]
            current_errors.append(error)
        
        # Store the next state values and errors
        for i in range(num_states):
            state_values[i] = np.append(state_values[i], next_values[i])
        errors.append(current_errors)
    
    # Print control law
    if print_law:
        print("Control Law:", final_control_law)
    
    # Plot results
    if plot:
        plt.figure(figsize=(12, 8))
        for i in range(num_states):
            plt.plot(time, state_values[i], label=f'State x{i+1}')
        plt.xlabel('Time (s)')
        plt.ylabel('State values')
        plt.title('System Simulation')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    # Save results
    if save_path:
        results = {
            "time": list(time),
            "state_values": [list(state) for state in state_values],
            "control_inputs": list(control_inputs),
            "errors": [error_list for error_list in errors]
        }
        with open(save_path, 'w') as f:
            json.dump(results, f)
    
    return state_values, control_inputs, errors
