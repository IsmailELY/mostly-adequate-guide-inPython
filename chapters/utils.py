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
