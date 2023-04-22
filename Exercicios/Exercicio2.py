import sys
from Auxiliares import *


# --------------------------------------------------------------------------------
# Questao 2.1
# --------------------------------------------------------------------------------
def Questao21():
    imprimeQuestao(
        2.1, 'Qual o maior número representável em Python por aritmética de ponto flutuante no sistema que você está usando?')
    imprimeQuestao(
        2.1, '(DICA: use a biblioteca sys.float_info (https://docs.python.org/3/library/sys.html) para saber mais sobre como o seu sistema trabalha com o tipo "float")')
    # Resposta
    imprimeTitulo('Resposta')
    imprimeTitulo('Float Info')
    print(sys.float_info)
    imprimeTitulo('Maior Ponto Flutuante')
    print('O maior número representável em Pyton por aritmética de ponto flutuante no meu sistema é ', sys.float_info.max)
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.2
# --------------------------------------------------------------------------------


def Questao22():
    imprimeQuestao(
        2.2, 'O que acontece se chamar em Python um número maior que esse? Ou se fizer uma conta que resulte em um número maior que esse? (Dê um exemplo)')
    # Resposta
    imprimeTitulo('Resposta')
    imprimeTitulo(' Chamada com maior que o máximo 1.7976931348623157e+308')
    print(sys.float_info.max)
    print('1.[8]976931349623158e+308:', 1.8976931349623158e+308)
    print('1.79769313486231[60]+308:', 1.7976931348623160+308)
    print('Se chamar em Python um número maior do que o máximo, no expoente o resultado será "inf" (infinito)')
    print('Se chamar em Python um número maior do que o máximo, na mantissa, haverá overflow')

    imprimeTitulo('Soma com maior que o máximo,  1.7976931348623157e+308')
    print('1.7976931348623157e+308 + 10:', 1.7976931348623157e+308 + 10)
    print('1.7976931348623157e+308 + 1e23:', 1.7976931348623157e+308 + 1e23)
    print('Se fizer uma conta que resulte em um número maior do que o máximo o resultado será truncado para o valor máximo')
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.3
# --------------------------------------------------------------------------------


def Questao23():
    imprimeQuestao(
        2.3, 'Quantos dígitos são bem representados nesse sistema de aritmética de ponto flutuante? (DICA: use o sys.float_info)')
    # Resposta
    imprimeTitulo('Resposta')
    print('Segundo a função (sys.float_info), são ',
          str(sys.float_info.dig), ' dígitos.')
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.4
# --------------------------------------------------------------------------------


def Questao24():
    imprimeQuestao(
        2.4, 'Qual o resultado da conta 1.0e-23 + 1.0e-23? Justifique.')
    # Resposta
    imprimeTitulo('Resposta')
    print('1.0e-23 + 1.0e-23 = ', 1.0e-23 + 1.0e-23)
    print('Justificativa:')

    # O Número 1.0e-23 -> Representa-se em forma de float desta forma:
    # (−1)^0 × ​2^(00110010−01111111) ​× ​1.10000010110110110011010
    # Traduzindo decimal:
    # (−1)^0 × ​2^(50-127=-77)        ×​ 1.5111572742462158203125 = 1.0e-23
    #
    # O Número 2.0e-23 -> Representa-se em forma de float desta forma:
    # (−1)^0 × ​2^(00110011−01111111) ​× 1.10000010110110110011010
    # Traduzindo decimal :
    # (−1)^0 × ​2^(51-127=-76)        ×​ 1.5111572742462158203125 = 2.0e-23
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.5
# --------------------------------------------------------------------------------


def Questao25():
    imprimeQuestao(
        2.5, 'Qual o resultado da conta 1.0 + 1.0e-23? Justifique.')
    # Resposta
    imprimeTitulo('Resposta')
    print('1.0 + 1.0e-23 = ', 1.0 + 1.0e-23)
    print('Justificativa:')

    # O Número 1.0 -> Representa-se em forma de float desta forma:
    # sinal      expoente               mantissa
    # (−1)^0 × ​2^(01111111−01111111) ​× ​1.00000000000000000000000
    # Traduzindo decimal :
    # (−1)^0 × ​2^(0)                 ×​ 1.0 = 1.0
    #
    # O Número 1.0e-23 -> Representa-se em forma de float desta forma:
    # (−1)^0 × ​2^(00110010−01111111) ​× ​1.10000010110110110011010
    # Traduzindo decimal:
    # (−1)^0 × ​2^(50-127=-77)        ×​ 1.5111572742462158203125 = 1.0e-23
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.6
# --------------------------------------------------------------------------------


def Questao26():
    imprimeQuestao(
        2.6, 'Qual o resultado da conta 1.0e+14 + 1.0e-14? Justifique.')
    # Resposta
    imprimeTitulo('Resposta')
    print('1.0e+14 + 1.0e-14 = ', 1.0e+14 + 1.0e-14)
    print('Justificativa:')

    # O Número 1.0e+14 -> Representa-se em forma de float desta forma:
    # sinal      expoente               mantissa
    # (−1)^0 × ​2^(10101101−01111111) ​× ​1.01101011110011000100001
    # Traduzindo decimal :
    # (−1)^0 × ​2^(46)                ×​ 1.42108547687530517578125 = 1.0e+14
    #
    # O Número 1.0e-14 -> Representa-se em forma de float desta forma:
    # (−1)^0 × ​2^(01010000−01111111) ​× ​1.10000010110110110011010
    # Traduzindo decimal:
    # (−1)^0 × ​2^(-47)               ×​ 1.407374858856201171875 = 1.0e-14
    #
    # Resultado:
    # O Número 100000000376832.0 -> Representa-se em forma de float desta forma:
    # (−1)^0 × ​2^(10101101−01111111) ​× ​1.01101011110011000100001
    # Traduzindo decimal:
    # (−1)^0 × ​2^(46)                ×​ 1.42108547687530517578125 = 100000000376832.0
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.7
# --------------------------------------------------------------------------------


def Questao27():
    imprimeQuestao(
        2.7, 'Leia o tutorial https://docs.python.org/pt-br/3/tutorial/floatingpoint.html e comente por que o computador não consegue representar o número 0.1 exatamente. ')
    imprimeQuestao(
        2.7, 'Qual número aproximado é alocado na memória e usado nas contas?')
    # Resposta
    imprimeTitulo('Resposta')
    imprimeTitulo('Representação do número 0.1 =  1 / 10')
    print(1 / 10)
    print('Justificativa:')
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.8
# --------------------------------------------------------------------------------


def Questao28(nusp):
    imprimeQuestao(
        2.8, 'Escreva o seu número USP como um int em binário.')

    # Resposta
    imprimeTitulo('Resposta')
    numeroUspInt = int(nusp)
    print('Número USP Inteiro', numeroUspInt)
    print('Número USP Inteiro (binário)', bin(numeroUspInt))
    input("Press Enter to continue...")

# --------------------------------------------------------------------------------
# Questao 2.9
# --------------------------------------------------------------------------------


def Questao29(nusp):
    imprimeQuestao(
        2.9, 'Escreva o seu número USP como um double float em binário (explicite cada componente, incluindo sinal, mantissa e expoente, da forma:')
    imprimeQuestao(
        2.9, '(−1)X×​2(YYYYYYYYY−01111111)​×​1.ZZZZZZZZZZZ')

    # Resposta
    imprimeTitulo('Resposta')
    print('Número USP:', nusp)
    print('Sinal     expoente                     mantissa')
    print('(−1)0 × ​2(10000011001−01111111111) ​× ​1.1101010101100001001100110000000000000000000000000000')
    input("Press Enter to continue...")


# --------------------------------------------------------------------------------
# Ponto de Entrada do módulo
# --------------------------------------------------------------------------------


def Exercicio2(titulo, nusp):
    imprimeTitulo(titulo)

    # ----------------------------------------------------------------------------
    # Imprime mágic Number
    # ----------------------------------------------------------------------------
    print("nusp  =", nusp)
    magic_ilong, magic_ishort = MagicNumbers(nusp)
    print("magic_ilong  =", magic_ilong)
    print("magic_ishort =", magic_ishort)
    Questao21()
    Questao22()
    Questao23()
    Questao24()
    Questao25()
    Questao26()
    Questao27()
    Questao28(nusp)
    Questao29(nusp)

    imprimeTraco(180)
