config_file = "config.py"

def set_env(var, value):
    f = open(config_file)
    lines = f.readlines()
    f.close()

    f = open(config_file, "w")
    for line in lines:
        if line.startswith(var):
            if type(value) is str:
                f.write(f'{var}\t\t= "{value}"\n')
            else:
                f.write(f'{var}\t\t\t= {value}\n')
        else:
            f.write(line)
    f.close()

def get_env(var):
    f = open(config_file)
    lines = f.readlines()
    f.close()

    r = None
    f = open(config_file, "r")
    for line in lines:
        if line.startswith(var):
            r = line.split('=')[1].strip()
    f.close()
    return r

