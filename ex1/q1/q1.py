from typing import Callable


def safe_call(f: Callable, **kwargs):
    """
    call f with the given arguments only if they are from the right type (as defined in f),
    otherwise - raise an exception.

    :param f: a function
    :param kwargs: the function arguments
    :return: behave like f
    """

    # get f arguments type
    annotations = f.__annotations__

    # pass the given arguments and check for compatibility with f arguments type
    for arg_key, arg_val in kwargs.items():
        type_val = type(arg_val)
        type_ann = annotations[arg_key]

        # raise an exception for wrong argument type
        if type_val != type_ann:
            raise Exception("wrong argument type in " + arg_key +
                            ", expected " + str(type_ann) + ", got " + str(type_val))

    # call f with the given arguments if compatibility is existed
    f(**kwargs)


def fun(x: int, y: str, z: dict):
    z[x] = y
    print(z)


def pow(x: int, p: float):
    return x ** p


def chain(str1: str, str2: str):
    print(str1 + " " + str2)


# safe_call(f=pow, x=2.5, p=1)
safe_call(f=chain, str1="Im", str2="tiered")
# safe_call(f=chain, str1="no", str2=1)
# safe_call(fun, x=5, y="a", z={})
