from functools import reduce

compose = lambda *fs: reduce(lambda f, g: lambda *a, **kw: f(g(*a, **kw)), fs)
