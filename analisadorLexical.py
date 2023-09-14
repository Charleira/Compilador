def exportar_tokens_para_arquivo(tokens, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.write("Lexema | Simbolo\n")
        arquivo_saida.write("-" * 30 + "\n")
        for token in tokens:
            arquivo_saida.write(f"{token[1]} | {token[0]}\n")

def analisador_lexical(teste, nome_arquivo_saida):
    lista_tokens = []
    
    # Dicionário de mapeamento de lexemas para símbolos
    tabela_de_tokens = {
        "programa": "sprograma",
        "início": "sinício",
        "fim": "sfim",
        "procedimento": "sprocedimento",
        "funcao": "sfuncao",
        "se": "sse",
        "entao": "sentao",
        "senao": "ssenao",
        "enquanto": "senquanto",
        "faca": "sfaca",
        ":=": "satribuicao",
        "escreva": "sescreva",
        "leia": "sleia",
        "var": "svar",
        "inteiro": "sinteiro",
        "booleano": "sbooleano",
        "verdadeiro": "sverdadeiro",
        "falso": "sfalso",
        "div": "sdiv",
        "e": "se",
        "ou": "sou",
        "nao": "snao",
        ".": "sponto",
        ";": "sponto_virgula",
        ",": "svirgula",
        "(": "sabre_parenteses",
        ")": "sfecha_parenteses",
        ">": "smaior",
        ">=": "smaior_igual",
        "=": "sig",
        "<": "smenor",
        "<=": "smenor_igual",
        "!=": "sdiferente",
        "+": "smais",
        "-": "smenos",
        "*": "smult"
    }
    
    with open(teste, 'r') as arquivo:
        caractere = arquivo.read(1)  # Lê o próximo caractere do arquivo
        while caractere:
            while (caractere == "{" or caractere == " ") and not caractere.isspace():
                if caractere == "{":
                    temp_token = "{"
                    caractere = arquivo.read(1)
                    while caractere != "}" and caractere:
                        temp_token += caractere
                        caractere = arquivo.read(1)
                    temp_token += "}"
                    lista_tokens.append(("TipoToken", temp_token))  # Insere na lista de tokens
                while caractere.isspace() and not caractere.isspace():
                    caractere = arquivo.read(1)
            
            if not caractere.isspace() and caractere != "":
                temp_token = caractere

                # Verifica se o caractere é um dígito
                if temp_token.isdigit():
                    while True:
                        caractere = arquivo.read(1)
                        if caractere.isdigit():
                            temp_token += caractere
                        else:
                            break
                    lista_tokens.append(("NUMERO", temp_token))

                # Verifica se o caractere é uma letra (identificador ou palavra reservada)
                elif temp_token.isalpha():
                    while True:
                        caractere = arquivo.read(1)
                        if caractere.isalnum() or caractere == "_":
                            temp_token += caractere
                        else:
                            break

                    # Verifica se é uma palavra reservada ou operador
                    if temp_token in tabela_de_tokens:
                        lista_tokens.append((tabela_de_tokens[temp_token], temp_token))
                    else:
                        lista_tokens.append(("IDENTIFICADOR", temp_token))

                # Outros caracteres especiais (como operadores)
                elif temp_token in tabela_de_tokens:
                    lista_tokens.append((tabela_de_tokens[temp_token], temp_token))
                else:
                    lista_tokens.append(("CARACTER_ESPECIAL", temp_token))
                
            caractere = arquivo.read(1)
    
    exportar_tokens_para_arquivo(lista_tokens, nome_arquivo_saida)

if __name__ == "__main__":
    nome_arquivo_entrada = "teste_6.txt"  # Substitua pelo nome do seu arquivo de entrada
    nome_arquivo_saida = "tokens_6.txt"  # Nome do arquivo de saída
    analisador_lexical(nome_arquivo_entrada, nome_arquivo_saida)
