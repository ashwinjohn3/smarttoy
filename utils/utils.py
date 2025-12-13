import os

def get_env_var(env_var_name: str):
    env_val = os.environ.get(env_var_name)
    
    if not env_val:
        raise ValueError(f"Please set: {env_var_name} environment variable!")
    
    return env_val
    
