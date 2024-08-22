# Lambda Function In Python................/////////////////////
# It Is a mini function which is  used for small function like two or three line function........
print()


def apply(fx, value):
    return 6 + fx(value)


sqr = lambda x: x * x

sum = lambda x, y: x + y

avg = lambda x, y, z: (x + y + z) / 3

print(sqr(5))

print(sum(2, 2))

print(avg(4, 8, 7))

print(apply(sqr, 5))
