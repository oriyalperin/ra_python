from typing import Callable


def last_call(func: Callable):
    """
    a decorator that call func with the given argument only if it's the first time with this argument.
    otherwise - the function print the returned value of the func without calling it.

    the decorator saves the called arguments and the returned value for each func,
    and uses them when func recalling with the same argument.

    :param func: a one parameter function.
    :return: func returned value (only in the given argument first time)

    Example:
    >>> @last_call
    ... def power_3(x: int):
    ...     return x ** 3

    >>> print(power_3(3))
    27
    >>> print(power_3(2))
    8
    >>> power_3(3)
    oops you did it again! the answer is 27
    """

    func_args = {}

    def wrapper(arg):
        func_name = func.__name__
        params = func_args.get(func_name)
        if params:
            ans = params.get(arg)
            if ans:
                print(f"oops you did it again! the answer is {ans}")
            else:
                ans = func(arg)
                params[arg] = ans
                return ans
        else:
            ans = func(arg)
            func_args[func_name] = {}
            func_args[func_name][arg] = ans
            return ans

    return wrapper
