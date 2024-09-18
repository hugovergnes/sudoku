import pandas as pd
from sudoku.cell import Cell


class Table:
    def __init__(self, none_value=0):
        self.none_value = none_value
        self._data = []

    def __getitem__(self, pos):
        row, col = pos
        return self._data[row][col]

    def update_candidate_values(self):
        for row_idx, row in enumerate(self._data):
            for col_idx, cell in enumerate(row):
                if cell.value != 0:
                    cell.candidate_values = {}
                else:
                    candidate_values = set(i for i in range(1, 10))
                    # Remove row values
                    for other_cell in row:
                        if other_cell.pos != cell.pos and other_cell.value != 0:
                            candidate_values.discard(other_cell.value)
                    # Remove col values
                    for other_row_idx in range(9):
                        other_cell = self[other_row_idx, col_idx]
                        if other_cell.pos != cell.pos and other_cell.value != 0:
                            candidate_values.discard(other_cell.value)
                    # Remove block values
                    block_row_idx = row_idx // 3
                    block_col_idx = col_idx // 3
                    for i in range(3):
                        for j in range(3):
                            other_cell = self[
                                block_row_idx * 3 + i, block_col_idx * 3 + j
                            ]
                            if other_cell.pos != cell.pos and other_cell.value != 0:
                                candidate_values.discard(other_cell.value)
                    cell.candidate_values = candidate_values

    def load_from_csv(self, path_to_csv, delimiter=";"):
        df = pd.read_csv(path_to_csv, delimiter=delimiter, header=None)
        df = df.fillna(self.none_value)
        original_data = df.to_numpy().astype(int)
        # Now convert to a Table of Cells
        data = []
        for row_idx, row in enumerate(original_data):
            new_row = []
            for col_idx, value in enumerate(row):
                new_row.append(Cell((row_idx, col_idx), value=value))
            data.append(new_row)
        self._data = data
        self.update_candidate_values()

    def get_table_data(self):
        data = []
        for row in self._data:
            line = [cell.value for cell in row]
            data.append(line)
        return data

    def set_value(self, row, col, value):
        self[row, col].set_value(value)
        self.update_candidate_values()

    def is_solved(self):
        for row in self._data:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
