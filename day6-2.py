ins = "10   3   15  10  5   15  5   15  9   2   5   8   5   2   3   6"

current_state = [int(k) for k in ins.split(" ") if k != ""]
nbuckets = len(current_state)


past_states = {}

steps = 0


while True:
    steps += 1
    past_states[hash(tuple(current_state))] = steps
    max_value = max(current_state)
    max_idx = current_state.index(max_value)

    current_state[max_idx] = 0

    for idx in range(max_value):
        mod_idx = (idx + max_idx + 1) % nbuckets
        current_state[mod_idx] += 1

    if hash(tuple(current_state)) in past_states:
        print steps - past_states[hash(tuple(current_state))] +1
        break

