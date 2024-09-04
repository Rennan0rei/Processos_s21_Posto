from bomba_combustivel import BombaCombustivel

# Cria a classe BombaGasolina que armazena valor por litro e verifica a quantidade disponivel
class BombaGasolina(BombaCombustivel):
    def _init_(self, valor_litro, quantidade_disponivel):
        super()._init_(valor_litro, quantidade_disponivel)

    # Abastece com adtivo por valor
    def abastecer_por_valor_com_aditivo(self, valor):
        valor_com_aditivo = valor * 1.05
        litros = valor_com_aditivo / self.valor_litro
        #Verifica se o valor em litros não excede a quantidade disponivel no carro
        if litros > self.quantidade_disponivel:
            return -1
        self.quantidade_disponivel -= litros
        return litros
    
    # Abastece com adtivo por litro
    def abastecer_por_litro_com_aditivo(self, litros):
        
        if litros > self.quantidade_disponivel:
            return -1
        valor_com_aditivo = litros * self.valor_litro * 1.05
        self.quantidade_disponivel -= litros
        return valor_com_aditivo