from importlib.util import resolve_name


class NotacaoPolonesaReversa():

    @staticmethod
    def valor_da_operacao(operacao):
        if(operacao == "+"):
            return 1
        if(operacao == "-"):
            return 1
        if(operacao == "*"):
            return 2
        if(operacao == "/"):
            return 2
        if(operacao == "^"):
            return 3


    @staticmethod
    def faz_operacao(operacao, n1, n2):
        if(operacao == "+"):
            return n1 + n2
        if(operacao == "-"):
            return n1 - n2
        if(operacao == "*"):
            return n1 * n2
        if(operacao == "/"):
            return n1 / n2
        if(operacao == "^"):
            return pow(n1, n2)


    def converte_para_npr(this, equacao):
        possiveis_numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        possiveis_operacoes = ["+", "-", "*", "/", "^"]

        #numero operacao

        equacaoFinal = []
        pilhaOperacoes = []

        # 1 + 1 + 1
        acumulado = ""
        for elemento in equacao:

            #Adiciona o numero ao acumulado
            if(str(elemento) in possiveis_numeros):
                acumulado = acumulado + elemento
            elif(str(elemento) in possiveis_operacoes):
                #Adiciona o acumulado na equacao
                equacaoFinal.append(float(acumulado))
                acumulado = ""

                if(len(pilhaOperacoes) == 0):
                    pilhaOperacoes.append(elemento)
                else:
                    valor_operacao_atual = this.valor_da_operacao(elemento)
                    operacao_anterior = pilhaOperacoes[len(pilhaOperacoes) -1]
                    valor_operacao_anterior = this.valor_da_operacao(operacao_anterior)

                    while(valor_operacao_atual <= valor_operacao_anterior):
                        valor_operacao_anterior = pilhaOperacoes.pop()
                        equacaoFinal.append(valor_operacao_anterior)

                        if(len(pilhaOperacoes) == 0):
                            break

                        operacao_anterior = pilhaOperacoes[len(pilhaOperacoes) -1]
                        valor_operacao_anterior = this.valor_da_operacao(operacao_anterior)

                    pilhaOperacoes.append(elemento)


        equacaoFinal.append(float(acumulado))
        while(len(pilhaOperacoes) > 0):
            equacaoFinal.append(pilhaOperacoes.pop())

        return equacaoFinal
                  

    def resolve_npr(this, npr):
        pilhaNumeros = []

        for elemento in npr:
            if(type(elemento) == type(1.0)):
                pilhaNumeros.append(elemento)
            else:
                numero2 = pilhaNumeros.pop()
                numero1 = pilhaNumeros.pop()
                resultado = this.faz_operacao(elemento, numero1, numero2)
                pilhaNumeros.append(resultado)
            
        return pilhaNumeros.pop()
p = NotacaoPolonesaReversa()

equacao = p.converte_para_npr("5+10*2-5*3")
print(equacao)
resultado = p.resolve_npr(equacao)
print(resultado)