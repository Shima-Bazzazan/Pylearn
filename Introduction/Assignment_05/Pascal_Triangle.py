
def pascal_triangle(height: int):
    triangle = []
    for row in range(1, height + 1):  
        temp = 1
        triangle.append([])
        for i in range(1, row + 1):
            triangle[row - 1].append(temp) 
            temp = int(temp * (row - i) / i)
    return triangle


def print_pascal_triangle(triangle: int):
    for row in triangle:
        for num in row:
            print("{:4d}".format(num), end ="")
        print()


n = int(input("Please enter the height of Pascal triangle: "))

print("pascal_triangle: ",pascal_triangle(n))

print_pascal_triangle(pascal_triangle(n))