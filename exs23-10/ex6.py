def pascals_triangle(n):
    triangle = []

    for i in range(n): #0 1 2
        row = [1]
        if i > 1:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        for element in row:
            print(element, end=' ')
        print()


print_pascals_triangle(pascals_triangle(5))