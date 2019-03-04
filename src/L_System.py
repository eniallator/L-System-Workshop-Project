def parse(in_string, rule_set):
    out_string = ''
    for char in in_string:
        if char in rule_set:
            out_string += rule_set[char]
        else:
            out_string += char

    return out_string


def l_system(axiom, rule_set, iterations):
    curr_string = axiom
    for i in range(iterations):
        print(curr_string)
        curr_string = parse(curr_string, rule_set)
    print(curr_string)
    return curr_string
