def Dec(func):
    def transform(*args, **kwargs):
        print("arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)
    return transform

@Dec
def someFun(s):
    print("%s %s" % (s, s))

someFun("kevin")
