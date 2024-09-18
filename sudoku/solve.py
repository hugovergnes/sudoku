from collections import Counter


def solve(table):
    # First check the cells that only have one possible candidate value
    changed = update(table)
    while changed:
        changed = update(table)

    # Then do some solving. Check if the value can be in own place in the row, col and block
    if not table.is_solved():
        changed = True
        while changed:
            changed = False
            changed = changed or fill_unique_value_row(table)
            changed = changed or fill_unique_value_column(table)
            changed = changed or fill_unique_value_block(table)


def fill_unique_value_block(table):
    changed = False
    for row_block_idx in range(3):
        for col_block_idx in range(3):
            block_values = []
            for row_idx in range(3):
                block_values += [
                    table[
                        3 * row_block_idx + row_idx, 3 * col_block_idx + col_idx
                    ].get_candidate_values()
                    for col_idx in range(3)
                ]
            unique_values = appears_once(block_values)
            for unique_value in unique_values:
                changed = True
                idx = [unique_value in k for k in block_values].index(True)
                table.set_value(idx // 3, idx % 3, unique_value)
    return changed


def fill_unique_value_column(table):
    changed = False
    for col in range(9):
        col_values = [
            table[row_idx, col].get_candidate_values() for row_idx in range(9)
        ]
        unique_values = appears_once(col_values)
        for unique_value in unique_values:
            changed = True
            row_idx = [unique_value in k for k in col_values].index(True)
            table.set_value(row_idx, col, unique_value)
    return changed


def fill_unique_value_row(table):
    changed = False
    for row in range(9):
        rows_values = [
            table[row, col_idx].get_candidate_values() for col_idx in range(9)
        ]
        unique_values = appears_once(rows_values)
        for unique_value in unique_values:
            changed = True
            col_idx = [unique_value in k for k in rows_values].index(True)
            table.set_value(row, col_idx, unique_value)
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
