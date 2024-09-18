from collections import Counter


def solve(table):
    # First check the cells that only have one possible candidate value
    changed = update(table)
    while changed:
        changed = update(table)

    # Then, check if the value can be in only one place in
    # the row, col and block.
    if not table.is_solved():
        changed = True
        while changed:
            changed = False
            changed |= fill_unique_value(table, "row")
            changed |= fill_unique_value(table, "column")
            changed |= fill_unique_value(table, "block")

    return table.is_solved()


def fill_unique_value(table, unit_type):
    """
    Fill unique values in rows, columns, or blocks based on unit_type.

    Args:
        table: The Sudoku table.
        unit_type (str): One of 'row', 'column', or 'block'.

    Returns:
        bool: True if any changes were made, False otherwise.
    """
    changed = False
    for unit in range(9):
        if unit_type == "row":
            values = [table[unit, col].get_candidate_values() for col in range(9)]
        elif unit_type == "column":
            values = [table[row, unit].get_candidate_values() for row in range(9)]
        elif unit_type == "block":
            block_row = unit // 3
            block_col = unit % 3
            values = [
                table[3 * block_row + row, 3 * block_col + col].get_candidate_values()
                for row in range(3)
                for col in range(3)
            ]
        else:
            raise ValueError("unit_type must be 'row', 'column', or 'block'.")

        unique_values = appears_once(values)
        for unique_value in unique_values:
            changed = True
            idx = [unique_value in k for k in values].index(True)
            if unit_type == "row":
                row, col = unit, idx
            elif unit_type == "column":
                row, col = idx, unit
            elif unit_type == "block":
                row = 3 * block_row + (idx // 3)
                col = 3 * block_col + (idx % 3)
            table.set_value(row, col, unique_value)
    return changed


def appears_once(values):
    all_values = [item for subset in values for item in subset]
    value_counts = Counter(all_values)
    return [value for value, count in value_counts.items() if count == 1]


def update(table):
    changed = False
    for row in range(9):
        for col in range(9):
            current_cell = table[row, col]

            if current_cell.value == 0 and len(current_cell.candidate_values) == 1:
                value = current_cell.get_candidate_values().pop()
                table.set_value(row, col, value)
                changed = True
    return changed
