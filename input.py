import re

pin = input()
score = 0


def increase_score(points):
    global score
    score += points


def is_very_long(pin):
    return any(len(pin) >= lenght for lenght in [12])


def has_digits(pin):
    return any(letter.isdigit() for letter in pin)


def has_upper_letters(pin):
    return any(letter.isupper() for letter in pin)


def has_lower_letters(pin):
    return any(letter.islower() for letter in pin)


def has_symbols(pin):
    return (not re.search(r"[~\!\@\#\$\%\^\&\*\(\)\_\+\{\}\"\:\;\'\[\]]", pin) for letter in pin)


def execute_functions(functions):
    for func in functions:
        if func(pin):
            increase_score(2)


functions_list = [
    is_very_long,
    has_digits,
    has_upper_letters,
    has_lower_letters,
    has_symbols
]

execute_functions(functions_list)
print(f"Рейтинг пароля: {score}")
