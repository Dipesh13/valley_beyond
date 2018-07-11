def variable_no_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["description"])

variable_no_arguments(name="Bob",description="loves to build")