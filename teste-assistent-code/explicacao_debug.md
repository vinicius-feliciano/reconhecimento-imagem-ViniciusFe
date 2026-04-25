# Análise de Erros - debug.py

Este documento identifica e explica os erros presentes no código `debug.py`, que implementa um sistema simples de cálculo de compras com impostos e descontos.

## Erros Identificados

### 1. Erro de Sintaxe - Aspas Faltando (Linha 6)

**Código Problemático:**
```python
item1 = float(input(Preço do item 1? ))
```

**Causa:**
- Falta de aspas ao redor da string `"Preço do item 1? "`
- Em Python, strings literais devem estar entre aspas simples (`'`) ou duplas (`"`)

**Erro Gerado:**
```
SyntaxError: invalid syntax
```

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### 2. F-String Não Declarada (Linha 23)

**Código Problemático:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Causa:**
- String com sintaxe de f-string (`{total_item2:.2f}`) mas sem o prefixo `f`
- Python trata como string literal comum, imprimindo o texto literalmente

**Saída Incorreta:**
```
Item 2:        R$ {total_item2:.2f}
```

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

### 3. Tipo de Dados Incompatível - String vs Número (Linhas 14, 27, 28)

**Códigos Problemáticos:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Causa:**
- `input()` sempre retorna uma string, mesmo que o usuário digite números
- Operações matemáticas (`/`, `*`) e comparações (`>`) com strings causam `TypeError`
- Formatação `.0f` em strings não funciona

**Erros Gerados:**
```
TypeError: unsupported operand type(s) for /: 'str' and 'int'
TypeError: '>' not supported between instances of 'str' and 'int'
ValueError: Unknown format code 'f' for object of type 'str'
```

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

### 4. Indentação Incorreta (Linha 28)

**Código Problemático:**
```python
if desconto_cupom > 0:
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Causa:**
- O `print` dentro do bloco `if` não está indentado
- Em Python, blocos de código (após `if`, `for`, etc.) devem ter indentação consistente

**Erro Gerado:**
```
IndentationError: expected an indented block
```

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

### 5. Formatação Redundante (Linha 31)

**Código Problemático:**
```python
print(f" TOTAL:         R$ {round(total, 2):.2f}")
```

**Causa:**
- `round(total, 2)` já arredonda para 2 casas decimais
- Aplicar `:.2f` novamente é redundante e pode causar problemas de precisão

**Correção Sugerida:**
```python
print(f" TOTAL:         R$ {total:.2f}")
```

---

## Código Corrigido Completo

```python
# SISTEMA DE CÁLCULO DE COMPRAS
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

---

## Lições Aprendidas

✅ **Sempre use aspas em strings literais**
✅ **Declare f-strings com prefixo `f`**
✅ **Converta inputs numéricos com `int()` ou `float()`**
✅ **Mantenha indentação consistente (4 espaços)**
✅ **Teste o código após correções**

O código agora está funcional e calcula corretamente totais de compras com impostos e descontos!