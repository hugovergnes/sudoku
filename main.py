import numpy as np

from sudoku.table import Table
from sudoku.solve import solve


def run_kaggle_files(rows_to_read=1000):
    """Run the solver on a few kaggle files.

    Args:
        rows_to_read (int, optional): Number of rows to read in the file.
            Defaults to 1000.
    """
    quizzes = np.zeros((1000000, 81), np.int32)
    solutions = np.zeros((1000000, 81), np.int32)
    for i, line in enumerate(
        open("./sudoku_files/kaggle/sudoku.csv", "r").read().splitlines()[1:]
    ):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
        if i == rows_to_read:
            break

    quizzes = quizzes[:rows_to_read, :]
    solutions = solutions[:rows_to_read, :]
    quizzes = quizzes.reshape((-1, 9, 9))
    solutions = solutions.reshape((-1, 9, 9))

    solved = 0
    for i in range(rows_to_read):
        table = Table()
        table.load_from_data(quizzes[i])
        _ = solve(table)
        res = table.get_table_data()
        if (np.array(res) == solutions[i]).all():
            solved += 1

    print(f"{solved}/{rows_to_read} files were solved in the Kaggle dataset")


if __name__ == "__main__":
    files = [
        "./sudoku_files/easy/sudoku_1.csv",
        "./sudoku_files/easy/sudoku_2.csv",
        "./sudoku_files/medium/sudoku_1.csv",
        "./sudoku_files/hard/sudoku_1.csv",
    ]
    for file in files:
        table = Table()
        table.load_from_data(file)
        is_solved = solve(table)
        if is_solved:
            print(f"{file} was solved !")
        else:
            print(f"Oh oh, {file} was not solved")

    run_kaggle_files()
