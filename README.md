# JungleLang (`.jgl`)

JungleLang é uma linguagem de programação esotérica criada para simular uma sintaxe inspirada na selva. O projeto inclui a documentação básica da linguagem, um tradutor de arquivos `.jgl` para Python e um programa de exemplo voltado para conscientização ambiental.

## Descrição resumida do que o programa faz

O programa `guardiaodafloresta.jgl` permite que o usuário digite o nome de um animal e receba:

- a identificação da espécie;
- um efeito narrativo com a "presença" do animal na floresta;
- a informação se ele está em perigo de extinção ou não dentro da lista usada no projeto;
- uma orientação sobre como agir ao encontrar esse animal.

O programa foi construído com uma lista de 20 animais e funciona como uma simulação educativa sobre preservação da fauna.

## Estrutura do projeto

- `guardiaodafloresta.jgl`: programa principal em JungleLang.
- `tradutor.py`: tradutor que converte arquivos `.jgl` em arquivos `.py`.
- `README.md`: documentação do projeto.

## Sintaxe básica da linguagem

### Tipos suportados

- `Monstro (Inteiro)`: números inteiros, como `0`, `1` e `99`.
- `Cipó (String)`: textos entre aspas duplas, como `"Olá, floresta"`.

### Comandos principais

| Comando em JungleLang | Equivalente em Python | Descrição |
| :--- | :--- | :--- |
| `NASCER variavel = valor` | `variavel = valor` | Declara e inicializa uma variável. |
| `RUGIR "texto" ou var` | `print("texto")` ou `print(var)` | Exibe algo na tela. |
| `CAÇAR variavel` | `variavel = input()` | Lê uma entrada do teclado. |
| `MUTAR var1 var2 var3` | `var1 = var2 + var3` | Soma dois valores. |
| `PERDER var1 var2 var3` | `var1 = var2 - var3` | Subtrai dois valores. |
| `ENQUANTO condicao` | `while condicao:` | Inicia um laço de repetição. |
| `FOME` | fim do bloco | Encerra um bloco iniciado por `ENQUANTO`. |

## Descrição do tradutor

O arquivo `tradutor.py` lê um programa escrito em JungleLang, converte cada comando para o equivalente em Python e gera automaticamente um novo arquivo `.py` pronto para execução.

Fluxo do tradutor:

1. Lê o arquivo `.jgl`.
2. Ignora linhas vazias e comentários.
3. Traduz comandos como `RUGIR`, `CAÇAR`, `NASCER` e `ENQUANTO`.
4. Ajusta a indentação dos blocos.
5. Salva o resultado com a extensão `.py`.

## Passos necessários para execução do programa

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Entrar na pasta do projeto

```bash
cd jungle-dev/jungle-lang-esolang
```

### 3. Traduzir o arquivo JungleLang para Python

```bash
python tradutor.py guardiaodafloresta.jgl
```

Esse comando gera o arquivo `guardiaodafloresta.py`.

### 4. Executar o programa traduzido

```bash
python guardiaodafloresta.py
```

## Importante

Arquivos `.jgl` não devem ser executados diretamente com Python. O comando abaixo gera erro:

```bash
python guardiaodafloresta.jgl
```

Isso acontece porque `RUGIR`, `NASCER`, `CAÇAR` e `ENQUANTO` são comandos da JungleLang, não comandos nativos do Python.

## Exemplo de uso

Ao executar o programa, o usuário informa um animal da lista, como:

```text
ariranha
```

Em seguida, o sistema mostra:

- a espécie identificada;
- uma descrição narrativa;
- o status de conservação dentro da lista adotada;
- a orientação de segurança e preservação.

## Requisitos

- Python 3 instalado na máquina.
- Terminal para executar os comandos.

## Observação final

O projeto tem foco didático. Ele demonstra:

- como criar uma linguagem simples com comandos próprios;
- como traduzir essa linguagem para Python;
- como aplicar a linguagem em um tema educativo ligado à preservação ambiental.
