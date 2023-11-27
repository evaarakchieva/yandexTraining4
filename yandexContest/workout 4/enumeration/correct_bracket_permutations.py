# generation of all correct bracket ( [ permutations
# in lexicographical order
def generate_bracket_permutations(input_n, open_brackets, close_brackets, bracket_sequence):
    if len(bracket_sequence) == 2 * input_n:
        result.append(''.join(bracket_sequence))
        return None
    if open_brackets < input_n:
        close_brackets.append(')')
        bracket_sequence.append('(')
        generate_bracket_permutations(input_n, open_brackets + 1, close_brackets, bracket_sequence)
        close_brackets.pop()
        bracket_sequence.pop()
        close_brackets.append(']')
        bracket_sequence.append('[')
        generate_bracket_permutations(input_n, open_brackets + 1, close_brackets, bracket_sequence)
        close_brackets.pop()
        bracket_sequence.pop()
    if close_brackets:
        bracket = close_brackets.pop()
        bracket_sequence.append(bracket)
        generate_bracket_permutations(input_n, open_brackets, close_brackets, bracket_sequence)
        bracket_sequence.pop()
        close_brackets.append(bracket)

n = int(input())
if n % 2 == 0:
    result = []
    generate_bracket_permutations(n//2, 0, [], [])
    print('\n'.join(result))
