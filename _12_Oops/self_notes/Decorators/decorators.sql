what is Decorators?
__ A Decorator in Python is a fuction that takes another function as its arguments, and returns yet another function.
decorators can be extremely useful as they allow the extension of an existing function, without any modification to 
the original function source code.
(Decorators are usually called before the defination of a function that we want to decorate)

ex:- def add_togerther(a,b):
           return a+b

    print(add_together(4,6))


why decorators are used in python?
__ decorators are a very powerful and useful tool in python since it allows programmers to modify the behaviour of function or class.
decorators allow us to wrap another function in order to extend the behaviour of the wrapped function. without permanently modifying it.


how do i create a decorators in python?
__ To create a decorator function in python, i create an outer funcion that takes a function as an argument.
there is also an inner function that wraps around the decorated function. 