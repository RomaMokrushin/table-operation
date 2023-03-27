def print_operation_table(operation, num_rows=9, num_columns=9):
    table = list()
    for i in range(num_rows):
        for j in range(num_columns):
            table.append(operation(i + 1, j + 1))
    for j in range(num_rows):
        print()
        for i in range(num_columns):
            print(table[i], end='\t')
        del table[0:num_columns]
