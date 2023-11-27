def process_stack_of_brackets(bracket_sequence):
    stack = []
    for bracket in bracket_sequence:
        if not stack and bracket in (')',']','}'):
            return 'no'
        if bracket in ('(','[','{'):
            stack.append(bracket)
        elif bracket == ')' and stack[-1] == '(':
            stack.pop()
        elif bracket == ']' and stack[-1] == '[':
            stack.pop()
        elif bracket == '}' and stack[-1] == '{':
            stack.pop()
        else:
            return 'no'

    if len(stack) == 0:
        return 'yes'
    return 'no'

input_sequence = input()
print(process_stack_of_brackets(input_sequence))