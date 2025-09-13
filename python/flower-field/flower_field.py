def annotate(garden):
    if not garden:
        return []
    row_lengths = {len(row) for row in garden}
    if len(row_lengths) > 1:
        raise ValueError("The board is invalid with current input.")

    rows, cols = len(garden), len(garden[0])
    new_garden = []
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0),  (1,1)]

    for r in range(rows):
        new_row = ""
        for c in range(cols):
            if garden[r][c] == "*":
                new_row += "*"
            elif garden[r][c] == " ":
                count = 0
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if garden[nr][nc] == "*":
                            count += 1
                new_row += str(count) if count else " "
            else:
                raise ValueError("The board is invalid with current input.")
        new_garden.append(new_row)
    return new_garden