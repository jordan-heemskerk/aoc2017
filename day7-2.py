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
            tree[name] = (weight, children)
            continue

        leaf_match = leaf_parser.match(line)
        if leaf_match:
            match_groups = leaf_match.groups()
            name = match_groups[0]
            weight = int(match_groups[1])
            tree[name] = (weight,)

def get_parent(name):
    for key, value in tree.iteritems():
        if len(value) > 1 and name in value[1]:
            return key

    return None

current = tree.keys()[0]
while True:
    current_parent = get_parent(current)
    if current_parent is None:
        break
    current = current_parent

root = current 

class Done(Exception):
    
    def __init__(self,node_name, diff):
        super(Done, self).__init__()
        self.node_name = node_name
        self.diff = diff

def get_weight(name):

    my_weight = tree[name][0]
    child_weights = []
    if len(tree[name]) > 1:
        for child in tree[name][1]:
            child_weights.append(get_weight(child))
    
    weight_set = set(child_weights)
    if len(weight_set) > 1:
        for weight in weight_set:
            if child_weights.count(weight) == 1:
                other_weight = list(weight_set - set([weight]))[0]
                raise Done(tree[name][1][child_weights.index(weight)], weight - other_weight)
    
    return my_weight + sum(child_weights)

try:
    get_weight(root)
except Done as d:
    print "Node of interest", d.node_name
    print "Node weight", tree[d.node_name][0]
    print "Off by", d.diff
    print "Answer", tree[d.node_name][0] - d.diff
