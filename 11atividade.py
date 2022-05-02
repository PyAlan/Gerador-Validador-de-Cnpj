
cnpj = '042520110001'
dig1 = 0
dig2 = 0

def sequencia(sequencia,cnpj):
    global mult
    sequence1,sequence2 = [a for a in range(sequencia,1,-1)],[a for a in range(9,1,-1)]
    sequence_uniao = sequence1 + sequence2
    mult = [int(x) * y for x,y in zip(cnpj,sequence_uniao)]

    return mult

def calculo(digito):

    conta = 11 - (soma % 11)
    if conta > 9:
        digito = 0
    else:
        digito = conta

    return str(digito)

soma = sum(sequencia(5,cnpj))

part1 = cnpj + calculo(dig1)

soma = sum(sequencia(6,part1))

new_cnpj = part1 + calculo(dig2)

print((f'{new_cnpj[:2]}.{new_cnpj[2:5]}.{new_cnpj[5:8]}/{new_cnpj[8:12]}-{new_cnpj[12:14]}'))
