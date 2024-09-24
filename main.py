from sudoku.table import Table
from sudoku.solve import solve

if __name__ == "__main__":
    table = Table()
    files = [
        "./sudoku_files/easy/sudoku_1.csv",
        "./sudoku_files/easy/sudoku_2.csv",
        "./sudoku_files/medium/sudoku_1.csv",
        "./sudoku_files/hard/sudoku_1.csv",
    ]
    for file in files:
        table.load_from_csv(file)
        is_solved = solve(table)
        if is_solved:
            print(f"{file} was solved !")
        else:
            print(f"Oh oh, {file} was not solved")
