# JungleLang (`.jgl`) 🐒🌴

A **JungleLang** é uma linguagem de programação esotérica (Esolang) de propósito geral desenvolvida para programadores que decidiram largar a civilização e codificar como nativos da selva. 

Este projeto conta com a documentação completa da sintaxe, um tradutor automatizado para Python e três programas funcionais de demonstração.

---

## 🗂️ 1. Documentação da Linguagem

### Tipos Suportados
* **Monstro (Inteiro):** Números inteiros (ex: `99`, `1`, `0`).
* **Cipó (String):** Cadeias de caracteres delimitadas por aspas duplas (ex: `"Hello World!"`).

### Tabela de Sintaxe e Comandos

| Comando em JungleLang | Equivalente em Python | Descrição |
| :--- | :--- | :--- |
| `NASCER variavel = valor` | `variavel = valor` | Declara e inicializa uma variável. |
| `RUGIR "texto" ou var` | `print("texto")` ou `print(var)` | Exibe algo na tela com quebra de linha. |
| `CAÇAR variavel` | `variavel = input()` | Lê uma entrada de texto do teclado. |
| `MUTAR var1 var2 var3` | `var1 = var2 + var3` | Soma dois valores e armazena no primeiro. |
| `PERDER var1 var2 var3` | `var1 = var2 - var3` | Subtrai dois valores e armazena no primeiro. |
| `ENQUANTO var1 > var2` | `while var1 > var2:` | Inicia um laço de repetição baseado em condição. |
| `FOME` | *(Redução de indentação)* | Encerra o bloco de código do `ENQUANTO`. |

---

## 💻 2. Código do Tradutor (`tradutor.py`)

O tradutor foi desenvolvido em **Python**. Ele faz a análise linha por linha do arquivo `.jgl`, substitui os tokens pelos equivalentes em Python, gerencia o nível de indentação dos blocos e gera um arquivo `.py` pronto para execução.

```python
import sys

def traduzir(arquivo_jgl):
    if not arquivo_jgl.endswith('.jgl'):
        print("Erro: O arquivo de origem deve ter a extensão .jgl")
        return

    try:
        with open(arquivo_jgl, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo_jgl} não encontrado.")
        return

    codigo_python = []
    nivel_indentacao = 0

    for linha in linhas:
        linha_limpa = linha.strip()
        
        # Ignora linhas vazias ou comentários
        if not linha_limpa or linha_limpa.startswith('#'):
            continue
        
        indent = "    " * nivel_indentacao
        
        # Comando: FOME (Fim de bloco)
        if linha_limpa == "FOME":
            nivel_indentacao = max(0, nivel_indentacao - 1)
            continue

        # Comando: NASCER (Declaração)
        if linha_limpa.startswith("NASCER "):
            partes = linha_limpa.replace("NASCER ", "", 1)
            codigo_python.append(f"{indent}{partes}")
            
        # Comando: RUGIR (Print)
        elif linha_limpa.startswith("RUGIR "):
            conteudo = linha_limpa.replace("RUGIR ", "", 1)
            codigo_python.append(f"{indent}print({conteudo})")
            
        # Comando: CAÇAR (Input)
        elif linha_limpa.startswith("CAÇAR "):
            var = linha_limpa.replace("CAÇAR ", "", 1)
            codigo_python.append(f"{indent}{var} = input()")
            
        # Comando: MUTAR (Soma: MUTAR resultado valor1 valor2)
        elif linha_limpa.startswith("MUTAR "):
            partes = linha_limpa.split()
            if len(partes) == 4:
                codigo_python.append(f"{indent}{partes[1]} = {partes[2]} + {partes[3]}")
                
        # Comando: PERDER (Subtração: PERDER resultado valor1 valor2)
        elif linha_limpa.startswith("PERDER "):
            partes = linha_limpa.split()
            if len(partes) == 4:
                codigo_python.append(f"{indent}{partes[1]} = {partes[2]} - {partes[3]}")
                
        # Comando: ENQUANTO (While)
        elif linha_limpa.startswith("ENQUANTO "):
            condicao = linha_limpa.replace("ENQUANTO ", "", 1)
            codigo_python.append(f"{indent}while {condicao}:")
            nivel_indentacao += 1
            
        else:
            codigo_python.append(f"{indent}{linha_limpa}")

    # Salva o arquivo traduzido para .py
    arquivo_saida = arquivo_jgl.replace('.jgl', '.py')
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write("\n".join(codigo_python))
    
    print(f"Sucesso! Arquivo traduzido gerado: {arquivo_saida}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python tradutor.py programa.jgl")
    else:
        traduzir(sys.argv[1])
```

## 📝 3. Programas de Demonstração

### 🔹 Programa 1: Hello World
Apenas exibe a mensagem clássica na tela usando as regras da linguagem.

<details>
  <summary>📄 Ver código em JungleLang (.jgl)</summary>

```text
RUGIR "Hello World!"

print("Hello World!")

NASCER qut = 99
NASCER um = 1
ENQUANTO qut > 0
    RUGIR qut
    RUGIR "garrafas de cerveja na selva!"
    PERDER qut qut um
FOME
RUGIR "Fim do estoque!"

qut = 99
um = 1
while qut > 0:
    print(qut)
    print("garrafas de cerveja na selva!")
    qut = qut - um
print("Fim do estoque!")

RUGIR "Digite um numero para calcular o fatorial:"
CAÇAR entrada
NASCER numero = int(entrada)

NASCER resultado = 1
NASCER um = 1

ENQUANTO numero > 1
    NASCER temp = resultado
    NASCER copia_numero = numero
    PERDER copia_numero copia_numero um
    
    ENQUANTO copia_numero > 0
        MUTAR resultado resultado temp
        PERDER copia_numero copia_numero um
    FOME
    
    PERDER numero numero um
FOME

RUGIR "O fatorial selvagem desse numero eh:"
RUGIR resultado

print("Digite um numero para calcular o fatorial:")
entrada = input()
numero = int(entrada)
resultado = 1
um = 1
while numero > 1:
    temp = resultado
    copia_numero = numero
    copia_numero = copia_numero - um
    while copia_numero > 0:
        resultado = resultado + temp
        copia_numero = copia_numero - um
    numero = numero - um
print("O fatorial selvagem desse numero eh:")
print(resultado)


