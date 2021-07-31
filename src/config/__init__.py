from os import getenv

config_env = {
    'api_port': int(getenv('API_PORT')),
    'psg_uri': getenv('PSG_URI')
}