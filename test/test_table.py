import pytest
from sudoku.table import Table

# The test function using pytest


class TestTable:
    @pytest.fixture
    def sudoku_2(self):
        table = Table()
        table.load_from_data("./sudoku_files/easy/sudoku_2.csv")
        return table

    def test_table_load_and_cells(self, sudoku_2):
        assert sudoku_2[0, 0] == 0
        assert sudoku_2[1, 1] == 6
        assert sudoku_2[0, 1] == 0

        assert sudoku_2[0, 0].candidate_values == {8}


if __name__ == "__main__":
    pytest.main()
