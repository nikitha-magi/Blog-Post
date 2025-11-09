"module to get config as dict"

def get_config(file="config.py"):
    config = {}
    with open(file, 'r') as conf:
        while line:=conf.readline():
            var_val = line.split("=")
            var = var_val[0].strip()
            val = var_val[1].strip().replace("\"", "")
            config[var] = val
    return config
