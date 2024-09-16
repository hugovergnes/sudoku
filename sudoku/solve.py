def solve(table):
    changed = update(table)
    while changed:
        print('chnaged')
        changed = update(table)
    

def update(table):
    changed = False
    for row in range(9):
        for col in range(9):
            current_cell = table[row, col]

            if current_cell.value == 0 and len(current_cell.candidate_values) == 1:
                value = current_cell.get_candidate_values().pop()
                table.set_value(row, col, value)
                changed = True
                # current_cell.set_value(current_cell.candidate_values.pop())
    return changed

            # For each candidate value. If it is the only place it can be in the row, col or
            # block. Then you can set it safely.
            # for number in current_cell.get_candidate_values:
            #     if not can_be_elsewhere_in_row(table, number):
            #         current_cell.set_value(current_cell.get_candidate_values[0])
            #         # TODO: update candidate values for the other cells
            #     elif not can_be_elsewhere_in_col(table, number):
            #         current_cell.set_value(current_cell.get_candidate_values[0])
            #         # TODO: update candidate values for the other cells
            #     elif not can_be_elsewhere_in_block(table, number):
            #         current_cell.set_value(current_cell.get_candidate_values[0])
            #         # TODO: update candidate values for the other cells
                    