"""Módulo para cálculo de estatísticas básicas de uma lista de números."""

from typing import Tuple


def calculate_statistics(numbers: list[float]) -> Tuple[float, float, float, float]:
    """Calcula estatísticas de uma lista de números.

    Retorna a soma total, média aritmética, valor máximo e mínimo.

    Args:
        numbers: Lista de números (inteiros ou floats).

    Returns:
        Tupla contendo (total, média, máximo, mínimo).

    Raises:
        ValueError: Se a lista estiver vazia.
        TypeError: Se algum elemento não for numérico.

    Examples:
        >>> calculate_statistics([23, 7, 45, 2, 67, 12, 89, 34, 56, 11])
        (346, 34.6, 89, 2)
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    try:
        total = sum(numbers)
        average = total / len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
    except TypeError as error:
        raise TypeError("Todos os elementos devem ser numéricos.") from error

    return total, average, maximum, minimum


def display_statistics(total: float, average: float, maximum: float, minimum: float) -> None:
    """Exibe as estatísticas de forma formatada.

    Args:
        total: Soma total dos valores.
        average: Média aritmética.
        maximum: Valor máximo.
        minimum: Valor mínimo.
    """
    print(f"Total:     {total}")
    print(f"Média:     {average}")
    print(f"Máximo:    {maximum}")
    print(f"Mínimo:    {minimum}")


def main() -> None:
    """Função principal que executa o programa."""
    # Lista de dados para análise
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    # Calcula as estatísticas
    total, average, maximum, minimum = calculate_statistics(numbers)

    # Exibe os resultados
    display_statistics(total, average, maximum, minimum)


if __name__ == "__main__":
    main()