def find_sqrt(n: int) -> int:
    if n < 0 :
        raise ValueError("n must not be negative number")
    for i in range(n+1):
        if i*i > n:
            return i-1
    return n

print(find_sqrt(0))#0
print(find_sqrt(1))#1
print(find_sqrt(2))#1
print(find_sqrt(3))#1
print(find_sqrt(4))#2
print(find_sqrt(8))#2
print(find_sqrt(9))#3
print(find_sqrt(15))#3
print(find_sqrt(16))#4
print(find_sqrt(24))#4
print(find_sqrt(25))#5
print(find_sqrt(26))#5
print(find_sqrt(99))#9
print(find_sqrt(100))#10
print(find_sqrt(101))#10


#Another method

# def sqrt_floor(n: int) -> int:
#     if n < 0:
#         raise ValueError("n must be non-negative")
#     return max([i for i in range(int(n**0.5) + 1) if i*i <= n])
#
# # Demo
# print(sqrt_floor(25))  # 5
# print(sqrt_floor(2))  # 5