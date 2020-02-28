def exception_str(f):
    try:
        f()
    except Exception as x:
        return str(x)
    else:
        return "No exception was raised"