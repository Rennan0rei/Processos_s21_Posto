from BombaEtanol import BombaEtanol
from BombaGasolina import BombaGasolina

# Criando as bombas
BombaEtanol = BombaEtanol(3.59, 1000)
BombaGasolina = BombaGasolina(4.89, 1000)

# Abastecendo com Etanol por valor
print(BombaEtanol.abastecer_por_valor(50))  # Saída: Quantidade de litros abastecidos

# Abastecendo com Gasolina por litros
print(BombaGasolina.abastecer_por_litro(20))  # Saída: Valor a ser pago

# Abastecendo com Gasolina com aditivo por valor
print(BombaGasolina.abastecer_por_valor_com_aditivo(50))  # Saída: Quantidade de litros abastecidos com aditivo

# Abastecendo com Gasolina com aditivo por litros
print(BombaGasolina.abastecer_por_litro_com_aditivo(20))  # Saída: Valor a ser pago com aditivo
