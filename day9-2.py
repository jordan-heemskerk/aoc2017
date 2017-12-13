with open("input9.txt") as fh:
    stream = fh.read().strip()

group_depth = 0
cancels = 0
in_garbage = False
garbage_count = 0

for char in stream:

    if char == "!":
        cancels += 1
        continue

    if cancels % 2 == 1:
        cancels = 0
        continue

    cancels = 0

    if in_garbage:
        if char == ">":
            in_garbage = False
        else:
            garbage_count += 1
        continue

    if char == "<":
        in_garbage = True
        continue

    if char == "{":
        group_depth += 1
        continue

    if char == "}":
        group_depth -= 1
        continue

        
print garbage_count
    


