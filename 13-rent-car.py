# variaveis
dias_locados = int(input("Dias alugados"))
km_percorridos = float(input("Quantos km foram percorridos ?"))


# calculo do preco total
total = (dias_locados*60) + (km_percorridos*0.15)
print(f"o valor total a pagar é R${total:.2f} ")