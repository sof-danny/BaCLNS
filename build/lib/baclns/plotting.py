import matplotlib.pyplot as plt

def plot_responses(time, state_values, control_inputs, errors):
    plt.figure(figsize=(12, 8))
    
    # Plot state variables
    for i, state in enumerate(state_values):
        plt.plot(time, state, label=f'State x{i+1}')
    
    plt.xlabel('Time (s)')
    plt.ylabel('States')
    plt.title('System Response')
    plt.grid(True)
    plt.legend()
    
    plt.figure(figsize=(12, 8))
    
    # Plot control inputs
    plt.plot(time[:-1], control_inputs, label='Control Input u')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Control Input')
    plt.title('System Control Input')
    plt.grid(True)
    plt.legend()
    
    plt.figure(figsize=(12, 8))
    
    # Plot errors
    for i, error_list in enumerate(zip(*errors)):
        plt.plot(time[:-1], error_list, label=f'Error in State x{i+1}')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Error')
    plt.title('State Errors Over Time')
    plt.grid(True)
    plt.legend()
    
    plt.show()
