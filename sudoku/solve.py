from collections import Counter

def solve(table):
    changed = update(table)
    while changed:
        changed = update(table)
    
    if not table.is_solved():
        fill_unique_value_row(table)

def fill_unique_value_row(table):
    for row in range(9):
        rows_values = [table[row, col_idx].get_candidate_values() for col_idx in range(9)]
        unique_values = appears_once(rows_values)
        pass

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
                    