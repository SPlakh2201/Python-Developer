def val_checker(x):
   def val_checker_decorator(func):
      def wrapper(*args, **kwargs):
         result = func(*args, **kwargs)
         return result
      return wrapper
   return val_checker_decorator


@val_checker(lambda x: x > 0)
def calc_cube(*x):
   return [num**3 for num in x]

a = calc_cube(5, 6, 7, 8)
print(a)