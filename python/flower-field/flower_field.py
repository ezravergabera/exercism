def annotate(garden):
    lengths = {len(row) for row in garden}

    if len(lengths) > 1:
        raise ValueError("The board is invalid with current input.")
    
    new_garden = []
    
    for row_index, row in enumerate(garden):
        new_garden_row = ""
        for col_index, col in enumerate(row):
            count = 0
            if col == "*":
                new_garden_row += "*"

                continue

            if col == "·":
                # top left corner
                if col_index == 0 and row_index == 0:
                    if garden[0][1] == "*":
                        count += 1
                    if garden[1][0] == "*":
                        count += 1
                    if garden[1][1] == "*":
                        count += 1

                # top
                if col_index > 0 and col_index < len(row)-1 and row_index == 0:
                    if garden[row_index][col_index-1] == "*":
                        count += 1
                    if garden[row_index][col_index+1] == "*":
                        count += 1
                    if garden[row_index+1][col_index-1] == "*":
                        count += 1
                    if garden[row_index+1][col_index] == "*":
                        count += 1
                    if garden[row_index+1][col_index+1] == "*":
                        count += 1

                # top right corner
                if col_index == len(row)-1 and row_index == 0:
                    if garden[0][len(row)-2] == "*":
                        count += 1
                    if garden[1][len(row)-3] == "*":
                        count += 1
                    if garden[1][len(row)-2] == "*":
                        count += 1

                # left middle
            
            if count != 0:
                new_garden_row += f"{count}"
            else:
                new_garden_row = "·"

        new_garden.append(new_garden_row)
            
    return new_garden

gra = [
    "···", 
    "·*·", 
    "···"
]

print(annotate(gra))

# 0,0 0,1 0,2
# 1,0 1,1 1,2
# 2,0 2,1 2,2