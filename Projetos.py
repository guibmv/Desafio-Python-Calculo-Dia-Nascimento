#Programa para calcular o dia que você nasceu
#A conta se resume no seguinte: Dia, Mês e Ano tem seus códigos, e o resultado do dia da semana se consiste na
#soma desses 3 codigós divido por 7, o resultado é o resto.
#Os codigos se constituem em:
#Dia: O código do dia é o próprio dia do mês.
#Mês: O código do mês são os números que estão listados logo abaixo, deles, janeiro e fevereiro mudam se o ano
#for bissexto, conforme também está listado abaixo
#Ano: Consiste na divisão exata dos ultimos 2 numeros por 4 e o resto da divisão por 7, considerando apenas os
#ultimos 2 dígitos do ano escolhido, OBS IMPORTANTE: se ano for sucessor do ano de 2000, devemos subtrair 1 do
#resultado final.
#LEMBRANDO QUE: Somente é funcional para os anos, de 1900 a 2099.

dia = int(input('Que dia você nasceu?\n'))
mes = int(input('Que mês você nasceu(em números)?\n'))
ano = int(input('Que ano você nasceu?\n'))

#CODIGO DO MES

if mes == 1:
    if ano % 4 == 0:
        codigo_mes = 0
    else:
        codigo_mes = 1
if mes == 2:
    if ano % 4 == 0:
        codigo_mes = 3
    else:
        codigo_mes = 4
if mes == 3:
    codigo_mes = 4
if mes == 4:
    codigo_mes = 0
if mes == 5:
    codigo_mes = 2
if mes == 6:
    codigo_mes = 5
if mes == 7:
    codigo_mes = 0
if mes == 8:
    codigo_mes = 3
if mes == 9:
    codigo_mes = 6
if mes == 10:
    codigo_mes = 1
if mes == 11:
    codigo_mes = 4
if mes == 12:
    codigo_mes = 6

#CODIGO DO ANO

if ano >= 2000:
    ano_part1 = ano - 2000
    ano_part2 = ano_part1 // 4
    ano_part3 = ano_part1 % 7
    codigo_ano = ano_part2 + ano_part3
    codigo_ano -= 1
else:
    ano_part1 = ano - 1900
    ano_part2 = ano_part1 // 4
    ano_part3 = ano_part1 % 7
    codigo_ano = ano_part2 + ano_part3

#RESULTADO FINAL

resultado_final = (dia + codigo_mes + codigo_ano) % 7

#RESPOSTA FINAL

if resultado_final == 0:
    print('Você nasceu no sábado xD')
if resultado_final == 1:
    print('Você nasceu no domingo xD')
if resultado_final == 2:
    print('Você nasceu na segunda-feira xD')
if resultado_final == 3:
    print('Você nasceu na terça-feira xD')
if resultado_final == 4:
    print('Você nasceu na quarta-feira xD')
if resultado_final == 5:
    print('Você nasceu na quinta-feira xD')
if resultado_final == 6:
    print('Você nasceu na sexta-feira xD')

if ano % 4 == 0:
    print('\nOBS: Você nasceu em um ano Bissexto :)')