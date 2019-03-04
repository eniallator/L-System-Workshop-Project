from src.L_System import l_system

if __name__ == '__main__':
    axiom = 'A'
    rule_set = {
        'A': 'AB',
        'B': 'A'
    }
    iterations = 14
    l_system(axiom, rule_set, iterations)
