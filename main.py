from sudoku.table import Table
from sudoku.solve import solve

if __name__ == '__main__':
    table = Table()
    table.load_from_csv('./sudoku_files/hard/sudoku_1.csv')
    solve(table)
    res = table.get_table_data()
    print(res)