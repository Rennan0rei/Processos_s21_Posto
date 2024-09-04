from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

    def abastecer_por_valor_com_aditivo(self, valor):
        valor_com_aditivo = valor * 1.05
        litros = valor_com_aditivo / self.valor_litro
        if litros > self.quantidade_disponivel:
            return -1
        self.quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro_com_aditivo(self, litros):
        if litros > self.quantidade_disponivel:
            return -1
        valor_com_aditivo = litros * self.valor_litro * 1.05
        self.quantidade_disponivel -= litros
        return valor_com_aditivo
