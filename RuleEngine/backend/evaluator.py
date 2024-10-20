def evaluate_rule(ast, user_data):
    if ast['type'] == 'operand':
        return eval(ast['value'], {}, user_data)
    
    left_result = evaluate_rule(ast['left'], user_data)
    right_result = evaluate_rule(ast['right'], user_data)

    if ast['value'] == 'AND':
        return left_result and right_result
    elif ast['value'] == 'OR':
        return left_result or right_result
