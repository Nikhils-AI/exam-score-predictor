def convert_int_safe(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def convert_float_safe(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

