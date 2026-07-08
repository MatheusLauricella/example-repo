# Each inner list is one row of the minefield.
# "#" means a mine and "-" means a safe spot.
minesweeper = [["-", "#", "-", "#", "-"], ["#", "-", "-", "#", "#"], ["#", "-", "-", "-", "-"], ["#", "-", "-", "-", "#"]]


def count_adjacent_mines(minefield, row, col):
    # Count mines in the 8 surrounding cells.
    count = 0
    for row_offset in (-1, 0, 1):
        neighbor_row = row + row_offset
        if neighbor_row < 0 or neighbor_row >= len(minefield):
            continue

        for col_offset in (-1, 0, 1):
            neighbor_col = col + col_offset
            if row_offset == 0 and col_offset == 0:
                continue
            if neighbor_col < 0 or neighbor_col >= len(minefield[neighbor_row]):
                continue
            if minefield[neighbor_row][neighbor_col] == "#":
                count += 1

    return count


def sweep_mines(minefield):
    # Build a new board that keeps mines and replaces safe spots with counts.
    result = []

    for row in range(len(minefield)):
        swept_row = []
        for col in range(len(minefield[row])):
            if minefield[row][col] == "#":
                swept_row.append("#")
            else:
                swept_row.append(str(count_adjacent_mines(minefield, row, col)))
        result.append(swept_row)

    return result


print(sweep_mines(minesweeper))
