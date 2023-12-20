cpf_user = '111444777'
nove_digitos = cpf_user[:9]
contador1 = 10


result1 = 0
for digito in nove_digitos:
    result1 += (int(digito) * contador1)
    contador1 -= 1
digito1 = ((result1 * 10) % 11)
digito1 = digito1 if digito1 <= 9 else 0
print(f'O primeiro digito é: {digito1}')


dez_digitos = nove_digitos + str(digito1)
contador = 11

result2 = 0
for digito in dez_digitos:
    result2 += (int(digito) * contador)
    contador -= 1
digito2 = result2 % 11
novo_digito = 11 - digito2
print(f'O segundo digito é: {novo_digito}')

cpf_completo = cpf_user + str(digito1) + str(novo_digito)
print(f'O CPF completo é: {cpf_completo}')
