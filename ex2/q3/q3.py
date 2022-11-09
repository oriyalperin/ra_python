class List(list):
    """
    List is a list structure variant, but can get item by multi-matrix syntax as followed:

    >>> mylist = List([[1,2],[3,4]])
    >>> mylist[1,0]
    3

    List overrides '__getitem__' method and uses the original method for passing over each inner-list.
    """
    def __getitem__(self, args):  # operator[] for reading
        if type(args) == int:
            return super().__getitem__(args)
        lst = super().__getitem__(args[0])
        for i in range(1, len(args)):
            lst = lst[args[i]]
        return lst



