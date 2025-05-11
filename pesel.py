def verify_pesel(pesel: str) -> int:

    if len(pesel) != 11 or not pesel.isdigit():
        return 0

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * weights[i] for i in range(10))
    kontrolna = (10 - (suma % 10)) % 10

    return 1 if kontrolna == int(pesel[10]) else 0


if __name__ == "__main__":
    pesel_input = input("Wprowadź numer PESEL (11 cyfr): ")
    wynik = verify_pesel(pesel_input)
    if wynik == 1:
        print("PESEL jest poprawny.")
    else:
        print("PESEL jest niepoprawny.")