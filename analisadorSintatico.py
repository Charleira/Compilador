class AnalisadorSintatico:
    def __init__(self):
        self.rotulo = 1
        self.token = None

    def lexico(self):
        # Implemente a função léxico aqui
        pass

    def insere_tabela(self, lexema, tipo, valor1, valor2):
        # Implemente a função insere_tabela aqui
        pass

    def analisa_bloco(self):
        self.lexico()
        self.analisa_et_variaveis()
        self.analisa_subrotinas()
        self.analisa_comandos()

    def analisa_et_variaveis(self):
        if self.token.simbolo == 'svar':
            self.lexico()
            while self.token.simbolo == 'sidentificador':
                self.analisa_variaveis()
                if self.token.simbolo == 'spontvirg':
                    self.lexico()
                else:
                    print("ERRO")

    def analisa_subrotinas(self):
        flag = 0
        if self.token.simbolo in ['sprocedimento', 'sfuncao']:
            auxrot = self.rotulo
            self.gera('', 'JMP', self.rotulo, '')
            self.rotulo += 1
            flag = 1

        while self.token.simbolo in ['sprocedimento', 'sfuncao']:
            if self.token.simbolo == 'sprocedimento':
                self.analisa_declaracao_procedimento()
            else:
                self.analisa_declaracao_funcao()

            if self.token.simbolo == 'sponto_virgula':
                self.lexico()
            else:
                print("ERRO")

        if flag == 1:
            self.gera(auxrot, None, '', '')  # inicio do principal

    def analisa_declaracao_procedimento(self):
        # Implemente a função analisa_declaracao_procedimento aqui
        pass

    def analisa_declaracao_funcao(self):
        # Implemente a função analisa_declaracao_funcao aqui
        pass

    def analisa_expressao(self):
        # Implemente a função analisa_expressao aqui
        pass

    def analisa_expressao_simples(self):
        # Implemente a função analisa_expressao_simples aqui
        pass

    def analisa_termo(self):
        # Implemente a função analisa_termo aqui
        pass

    def analisa_fator(self):
        # Implemente a função analisa_fator aqui
        pass

def main():
    analisador = AnalisadorSintatico()
    analisador.lexico()
    if analisador.token.simbolo == 'sprograma':
        analisador.lexico()
        if analisador.token.simbolo == 'sidentificador':
            analisador.insere_tabela(analisador.token.lexema, "nomedeprograma", "", "")
            analisador.lexico()
            if analisador.token.simbolo == 'spontovirgula':
                analisador.analisa_bloco()
                if analisador.token.simbolo == 'sponto':
                    # Implemente a verificação do fim do arquivo ou comentário aqui
                    print("Sucesso")
                else:
                    print("ERRO")
            else:
                print("ERRO")
        else:
            print("ERRO")
    else:
        print("ERRO")

if __name__ == "__main__":
    main()
