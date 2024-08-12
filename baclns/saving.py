import json

def save_responses(time, state_values, control_inputs, filename, errors=None):
    data = {
        "time": time.tolist(),
        "state_values": [state.tolist() for state in state_values],
        "control_inputs": control_inputs
    }
    
    if errors is not None:
        data["errors"] = [error_list for error_list in errors]
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
