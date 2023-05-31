def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(operation(i, j), end = "\t")
        print(" ")

rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
data_table = print_operation_table(lambda rows,columns:rows*columns, rows,columns)