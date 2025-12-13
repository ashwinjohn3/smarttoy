from supabase import Client, create_client

from utils.constants import SUPABASE_KEY_ENV_VAR, SUPABASE_URL_ENV_VAR
from utils.utils import get_env_var

class SupabaseClient:
    __supabase_client: Client
    
    def __init__(self):
        url = get_env_var(SUPABASE_URL_ENV_VAR)
        key = get_env_var(SUPABASE_KEY_ENV_VAR)
        self.__supabase_client = create_client(url, key)