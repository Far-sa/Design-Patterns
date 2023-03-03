

def compute_test(a, b, c, *, e):
    return a + b + c

# def compute_test(*args, a, b, c, e):
#     return a + b + c


print(compute_test(1, 2, 3, e=10))
