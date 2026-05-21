"""Moduł zawierający testy jednostkowe dla konwertera binarnego."""

import pytest
from binary_converter import to_binary


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (15, "1111"),
        (100, "1100100"),
    ],
)
def test_correct_conversion(number, expected):
    """Testuje poprawność konwersji prawidłowych liczb naturalnych."""
    assert to_binary(number) == expected


@pytest.mark.parametrize("invalid_number", [-1, 101, 500])
def test_range_validation(invalid_number):
    """Testuje, czy wyrzucany jest błąd ValueError dla liczb spoza zakresu 0-100."""
    with pytest.raises(ValueError):
        to_binary(invalid_number)


@pytest.mark.parametrize("non_natural", [1.5, "10", [10], None, True])
def test_natural_number_validation(non_natural):
    """Testuje, czy wyrzucany jest błąd TypeError dla wartości niebędących liczbami naturalnymi."""
    with pytest.raises(TypeError):
        to_binary(non_natural)
