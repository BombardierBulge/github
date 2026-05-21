"""Moduł do konwersji liczb naturalnych na format binarny."""


def to_binary(number: int) -> str:
    """Konwertuje liczbę naturalną od 0 do 100 na postać binarną.

    Args:
        number (int): Liczba naturalna do konwersji.

    Raises:
        TypeError: Jeśli przekazany obiekt nie jest liczbą całkowitą.
        ValueError: Jeśli liczba wykracza poza zakres [0, 100].

    Returns:
        str: Reprezentacja binarna liczby.
    """
    # Sprawdzenie typu (w Pythonie bool jest podtypem int, więc musimy go wykluczyć)
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Wprowadzona wartość nie jest liczbą naturalną.")

    # Sprawdzenie zakresu 0 - 100
    if number < 0 or number > 100:
        raise ValueError("Liczba musi być w przedziale od 0 do 100.")

    # Konwersja na postać binarną za pomocą wbudowanej funkcji bin() i odcięcie prefiksu '0b'
    return bin(number)[2:]
