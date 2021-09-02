def type_logger(func):
   def wrapper(*args):
      for arg in args:
         print(f'{func.__name__}({arg}: {type(func(arg))})')
      return func(*args)
   return wrapper


@type_logger
def calc_cube(*x):
   for num in x:
      return num ** 3

calc_cube(5, 10, 12)