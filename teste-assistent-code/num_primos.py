"""Módulo para verificação de números primos."""


def is_prime(number: int) -> bool:
    """Verifica se um número inteiro é primo.

    Um número primo é aquele maior que 1 que não possui divisores
    positivos além de 1 e ele mesmo.

    Args:
        number: Número inteiro a ser verificado.

    Returns:
        True se o número é primo, False caso contrário.

    Raises:
        TypeError: Se o argumento não for um inteiro.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
    """
    if not isinstance(number, int):
        raise TypeError("O argumento deve ser um número inteiro.")

    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    # Verifica divisores ímpares até a raiz quadrada do número
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True


def main() -> None:
    """Executa testes da função is_prime com exemplos."""
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (20, False),
        (97, True),
        (1, False),
        (0, False),
        (-5, False),
    ]

    for number, expected in test_cases:
        result = is_prime(number)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_prime({number}) = {result}")


if __name__ == "__main__":
    main()