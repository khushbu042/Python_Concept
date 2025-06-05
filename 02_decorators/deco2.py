# problem 2 : debugging Function Calls 
# create a decorator to print the function name and the value of its argument every time the function is called



def function_info(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        args_value = ", ".join( str(arg) for arg in args)
        kwargs_value = ', '.join( f"{k}= {w}"for k, w in kwargs.items())
        print(f"function calling name is {func_name} and args values is {args_value} and kwargs values is {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper 

@function_info
def hello():
    print("Hello")

@function_info
def greeting(name, greeting= "Hello"):
    print(f"{name} -  {greeting}")

hello()
greeting("khushbu","mourya")