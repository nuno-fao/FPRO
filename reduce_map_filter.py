import functools as f
def reduce_map_filter(args):
    if type(args[2])==tuple:
        args = args[:2]+(reduce_map_filter(args[2]),)
    if args[0]=="map":
        w = list(map(args[1],args[2]))
    elif args[0]=="filter":
        w = list(filter(args[1],args[2]))
    else:
        w = f.reduce(args[1],args[2])
    return w