def pascal_triangle(n):
    if n <= 0:
        return []

    result = []

    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = result[i - 1]
                row.append(prev_row[j - 1] + prev_row[j])

        result.append(row)

    return result
