def reverse_integer(num):
    reversed_int = 0
    remainder = 0

    while num > 0:
        remainder = num%10
        reversed_int = reversed_int*10 + remainder
        num = num // 10

    return reversed_int

if __name__ == '__main__':

    print(reverse_integer(12345))
