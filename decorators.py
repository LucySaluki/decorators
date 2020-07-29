def say_hello():
  return "Hello world!"

hi = say_hello

# print(hi())

# print(hi)
# print(say_hello)

# def function_caller(callback):
#   return callback()

# print(function_caller(hi))

# def outer_function():
#   def inner_function():
#     print("Hello from the inner function")

#   inner_function()

# outer_function()

# def make_pretty(callback):
#     def wrapper():
#         print("I am a decorated function!")
#         callback()
#     return wrapper

# def ordinary():
#     print("I am an ordinary function")

# # pretty = make_pretty(ordinary)

# ordinary()
# # pretty()

def make_pretty(callback):
    def wrapper():
        print("I am a decorated function!")
        callback()
    return wrapper

def doTwice(callback): # ADDED
    def wrapper():
        callback()
        callback()
    return wrapper

@doTwice # ADDED
@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()