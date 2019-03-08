def two_fer(*args):
    if len(args)==1 and isinstance(args[0],str):
        return "One for " + args[0] + ", one for me."
    else:
        return "One for you, one for me."


