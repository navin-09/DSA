# Q5: How does variable scoping work in Python (LEGB rule)?

Python resolves variable names using the LEGB rule — Local, Enclosing, Global, Built-in. When a variable is referenced, Python first looks in the local scope (inside the current function), then in enclosing scopes (outer functions, if nested), then the global module scope, and finally in built-ins like len or range. This hierarchy determines which variable is used or modified. Understanding this helps avoid shadowing and scope-related bugs, especially in closures or nested functions.

# Q6: Explain *args and **kwargs. When would you use each?

In Python, *args collects a variable number of positional arguments into a tuple, while **kwargs collects keyword arguments into a dictionary. They allow flexible function definitions where the number of inputs isn’t fixed. Use *args when you want to accept any number of unnamed arguments, and **kwargs when you want to handle named parameters dynamically. This is especially useful in wrapper functions, decorators, or API methods that pass arguments forward.