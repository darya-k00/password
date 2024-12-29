def is_very_long(pin):
    return len(pin) >= 12


def has_digits(pin):
    return any(letter.isdigit() for letter in pin)


def has_upper_letters(pin):
    return any(letter.isupper() for letter in pin)


def has_lower_letters(pin):
    return any(letter.islower() for letter in pin)


def has_symbols(pin):
    return any(not letter.isalnum() for letter in pin)


def get_password_score(pin):
    score = 0
    functions = [
        is_very_long,
        has_digits,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    for function in functions:
        if function(pin):
            score += 2
    return score


def main():
    pin = input()
    score = get_password_score(pin)
    print(f"Рейтинг пароля: {score}")


if __name__ == "__main__":
    main()
