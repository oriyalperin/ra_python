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
            raise TypeError()

    # call f with the given arguments if compatibility is existed
    return f(**kwargs)
