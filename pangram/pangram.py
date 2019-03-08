def is_pangram(*args):
    if len(args)==1 and isinstance(args[0],str):
        pangram='abcdefghijklmnopqrstuvwxyz'
        sentence=''.join(sorted(set(args[0].replace(" ","").lower())))
        if pangram == sentence:
            return True
        else:
            return False
    else:
        return False
