from functools import reduce


"""
Compose is a pure function used on a serie of curried functions defining a pipeline of morphism.

"""
compose = lambda *fs: reduce(lambda f, g: lambda *a, **kw: f(g(*a, **kw)), fs)


"""
Trace is a unpure function used for debugging composition of functions.
Insert Trace to display its input(which is the output of previous function).
"""
def trace(tag): 
    def f(x):
        print(tag, x)
        return x
    return f

"""
Basic wrapper for error handling.
"""
def errorHandle(f):
    def wrapper(*args, **kwargs):
        try:
           return f(*args, **kwargs)
        except Exception as e:
            print(f'Error: {e}')
    return wrapper

"""
Curry function wraps the original function and keeps returning functions 
until enough arguments are provided.

Ex: new_f = curry(f)
    f(a, b) = new_f(a,b) = new_f(a)(b) 
"""
def curry(f):
    def curried(*args, **kwargs):
        if len(args) >= f.__code__.co_argcount:
            return f(*args, **kwargs)
        return lambda *next_args, **next_kwargs: curried(
            *(args + next_args), **{**kwargs, **next_kwargs}
        )
    return curried


"""
Basic map function to apply a morphism to an array of values
"""
map = curry(lambda f, xs: [f(s) for s in xs])
