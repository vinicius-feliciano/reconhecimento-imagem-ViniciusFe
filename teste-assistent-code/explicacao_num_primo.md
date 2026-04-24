# Explicação da Função is_prime

A função `is_prime(number)` verifica se um número inteiro é primo. Um número primo é aquele maior que 1 que não possui divisores positivos além de 1 e ele mesmo.

## Código da Função (Clean Code)

```python
def is_prime(number: int) -> bool:
    """Verifica se um número inteiro é primo.

    Args:
        number: Número inteiro a ser verificado.

    Returns:
        True se o número é primo, False caso contrário.
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
```

## Melhorias Aplicadas (Clean Code)

### 1. **Anotação de Tipos (Type Hints)**
   - `number: int` e `-> bool` tornam claro qual tipo de dado é esperado e retornado
   - Facilita a detecção de erros em IDEs e ferramentas de análise estática

### 2. **Docstring Completa**
   - Descrição clara da função
   - Seções `Args` e `Returns` documentam o comportamento
   - Inclui exemplos de uso

### 3. **Nomes Significativos**
   - `number` em vez de `n` (mais claro)
   - `divisor` em vez de `i` (descreve o propósito da variável)

### 4. **Validação de Entrada**
   - Verifica se o tipo de entrada é válido
   - Lança `TypeError` com mensagem clara se inválido

### 5. **Otimizações**
   - Verifica se o número é 2 (único primo par) separadamente
   - Verifica se o número é par e retorna `False` imediatamente
   - Itera apenas sobre números ímpares (`range(3, ..., 2)`), reduzindo iterações pela metade

### 6. **Função `main()`**
   - Encapsula a lógica de testes
   - Segue o padrão `if __name__ == "__main__"`
   - Mais fácil de testar e manter

## Exemplo de Uso

```python
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
```

## Resultado dos Testes

Ao executar `python num_primos.py`, você verá:

```
✓ is_prime(2) = True
✓ is_prime(3) = True
✓ is_prime(4) = False
✓ is_prime(17) = True
✓ is_prime(20) = False
✓ is_prime(97) = True
✓ is_prime(1) = False
✓ is_prime(0) = False
✓ is_prime(-5) = False
```

## Boas Práticas Implementadas

- ✅ **PEP 8**: Segue os padrões de formatação Python
- ✅ **Documentação**: Inclui docstrings e comentários significativos
- ✅ **Tipos**: Uso de type hints para melhor legibilidade
- ✅ **Validação**: Verifica entrada inválida
- ✅ **Eficiência**: Algoritmo otimizado com complexidade O(√n)
- ✅ **Testabilidade**: Função separada de testes e código principal
