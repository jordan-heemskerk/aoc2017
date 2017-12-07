import re

leaf_parser = re.compile(r"(\w+) \((\d+)\)")
branch_parser = re.compile(r"(\w+) \((\d+)\) -> (.*)")


tree = {}
with open("input7.txt") as fh:
    for line in fh:
        branch_match = branch_parser.match(line)

        if branch_match:
            match_groups = branch_match.groups()
            name = match_groups[0]
            weight = int(match_groups[1])
            children = match_groups[2].split(", ")
            tree[name] = children

def get_parent(name):
    for key, value in tree.iteritems():
        if name in value:
            return key

    return None


current = tree.keys()[0]
while True:
    current_parent = get_parent(current)
    if current_parent is None:
        break
    current = current_parent


print current
