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
            # Mantém linhas que não correspondem a comandos mapeados (ex: funções nativas do Python utilizadas)
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