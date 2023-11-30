def lozi (n):
    for i in range(n):
        print








def diamond(height: int):
    for i in range(height):
        print(" " * (height - i), "*" * (2 * i + 1))

    for i in range(height - 2, -1, -1):
        print(" " * (height - i), "*" * (2 * i + 1))


n =int (input("Please enter diamond's height: "))
diamond(n)