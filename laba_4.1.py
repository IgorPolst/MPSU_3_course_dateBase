def no_kwargs(func):
    def wrapper(*args, **kwargs):
        if kwargs:
            raise TypeError
            return func(*args)
    return wrapper

@no_kwargs
def square(x):
    return x * x

print(square(4))        # 16
print(square(x=4))      # TypeError