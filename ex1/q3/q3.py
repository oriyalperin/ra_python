def sort(struct):
    """
    deeply sort the given structure in recursion.

    :param struct: data structure (list,tuple,set,dict)
    :return: the structure deeply sorted in ascending order
    """
    if type(struct) not in [list, set, tuple, dict]:
        return struct
    else:
        typ = type(struct)
        if typ == dict:
            sorted_struct = dict()
            for k, v in struct.items():
                sorted_struct[sort(k)] = sort(v)
            sorted_struct = sorted(sorted_struct.items())
        elif typ == set:
            sorted_struct = set()
            for mem in struct:
                sorted_struct.add(sort(mem))
            sorted_struct = sorted(sorted_struct)
        else:
            sorted_struct = list()
            for mem in struct:
                sorted_struct.append(sort(mem))
            if typ == tuple:
                sorted_struct = tuple(sorted_struct)
            sorted_struct = sorted(sorted_struct)

        return sorted_struct


def print_sorted(struct):
    """
    print the deeply sorted struct.
    :param struct:
    :return: None
    """
    print(sort(struct))
