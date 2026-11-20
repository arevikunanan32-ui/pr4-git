MAX_DIM = 16
def get_dimension(name):
    while True:
        raw = input(f"{name} = ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Введите целое число!")
            continue
        if value < 1 or value > MAX_DIM:
            print(f"Допустимо от 1 до {MAX_DIM}!")
            continue
        return value
def get_matrix(rows, cols):
    matrix = []
    print(f"Вводите матрицу по строкам (чисел в строке: {cols})")
    while len(matrix) < rows:
        values = input(f"[{len(matrix) + 1}] ").replace(",", ".").split()
        if len(values) != cols:
            print(f"Чисел в строке должно быть: {cols}!")
            continue
        try:
            matrix.append(list(map(float, values)))
        except ValueError:
            print("Встретилось не число!")
    return matrix
def columns_of(matrix):
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]
def print_by_columns(matrix):
    for number, column in enumerate(columns_of(matrix), start=1):
        print(f"Столбец {number}:", "  ".join(f"{x:.2f}" for x in column))
def main():
    print("Ввод матрицы по строкам и вывод по столбцам")
    rows = get_dimension("n (строк)")
    cols = get_dimension("m (столбцов)")
    matrix = get_matrix(rows, cols)
    print()
    print_by_columns(matrix)


if __name__ == "__main__":
    main()
