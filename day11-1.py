with open("input11.txt") as fh:
    instructions = fh.read().strip().split(",")

souths = len([i for i in instructions if i == "s"]) 
norths = len([i for i in instructions if i == "n"]) 
southeasts = len([i for i in instructions if i == "se"]) 
southwests = len([i for i in instructions if i == "sw"]) 
northeasts = len([i for i in instructions if i == "ne"]) 
northwests = len([i for i in instructions if i == "nw"]) 

delta_n = norths - souths
delta_ne = northeasts - southwests
delta_se = southeasts - northwests

print delta_n + max(delta_ne, delta_se)



