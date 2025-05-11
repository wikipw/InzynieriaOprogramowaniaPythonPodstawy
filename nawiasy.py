def check_parentheses(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    user_input = input("Wprowadź ciąg znaków do sprawdzenia nawiasów: ")
    wynik = check_parentheses(user_input)
    if wynik:
        print("Nawiasy są poprawnie sparowane.")
    else:
        print("Nawiasy są niepoprawne.")