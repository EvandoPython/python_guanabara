prod = float(input("Qual o Preço do produto R$: "))
porc = 5
porc = prod * porc / 100
desc = prod - porc
print(f'O produto que custava {prod} na promoção com desconto de 5% vai custar {desc:.2f}')
