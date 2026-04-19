import numpy as np

def create_function(equation):

    def f(x):
        return eval(equation)

    def df(x):
        h = 1e-5
        return (f(x + h) - f(x - h)) / (2*h)

    return f, df
