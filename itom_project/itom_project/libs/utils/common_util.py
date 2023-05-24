
def chain_getattr(obj, *args, default=None, raise_error=False):
    """
    Chain get object attribute or multidimensional dict value with no exception.
    e.g:
        request.user.group.name
        If the user object has no group, there will be raised an error(User object has no attribute 'group')
        Instead you can use chain_getattr(request, 'user', 'group', 'name', raise_error=False) to avoid the error.
        {'a': {'aa': {'aaa': 1}}}
        chain_getattr({'a': {'aa': {'aaa': 1}}}, 'a', 'aa', 'aaa', raise_error=False)
    """
    for arg in args:
        has_attr = arg in obj if isinstance(obj, dict) else hasattr(obj, arg)
        if not has_attr:
            if raise_error:
                raise AttributeError(f'{obj} object has no attribute {arg}')
            return default
        obj = obj.get(arg) if isinstance(obj, dict) else getattr(obj, arg)
    return obj
