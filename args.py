def var_args(name,*args):
    print(name)
    print(type(args))
    print(args)

var_args("Bob","loves to build",None,13)