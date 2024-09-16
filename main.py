from sudoku.table import Table
from sudoku.solve import naive_solve

if __name__ == '__main__':
    table = Table()
    table.load_from_csv('./sudoku_files/easy/sudoku_2.csv') # One is broken
    naive_solve(table)
    res = table.get_table_data()
    print(res)