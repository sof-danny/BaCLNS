import sympy as sp

def generic_backstepping_controller(num_states, state_equations, control_input, gains):
    # Define symbolic variables
    states = sp.symbols(f'x1:{num_states+1}')  # Create symbols x1, x2, ..., xn
    u = sp.Symbol(control_input)
    
    errors = states
    
    # Unpack the gains
    gains = [sp.Symbol(f'k{i}') for i in range(1, num_states+1)]
    
    # Step 1: Initialize the error terms and control laws
    control_laws = []
    error_terms = []
    
    # Iteratively compute the virtual controls and error terms
    for i in range(num_states - 1):
        # Define the virtual control phi
        if i == 0:
            phi = -gains[i] * errors[i]
        else:
            phi = -gains[i] * error_terms[i-1]
        
        # Define the error term z
        z = errors[i+1] - phi
        error_terms.append(z)
        
        # Compute the derivative of the error term (z_dot)
        z_dot = sum(sp.simplify(sp.diff(z, states[j]) * state_equations[j]) for j in range(num_states))
        
        # Store the control law
        control_laws.append(sp.simplify(z_dot + gains[i+1] * z))
    
    # Step 2: Derive the final control law for u
    final_control_law = sp.simplify(sp.solve(control_laws[-1], u)[0])
    
    # Return the derived control law, and optionally, the errors and references
    return final_control_law, states, gains
