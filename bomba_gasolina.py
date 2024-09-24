from bomba_combustivel import BombaCombustivel

class BombaGasolina(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

    def abastecer_por_valor_com_aditivo(self, valor):
        valor_com_aditivo = self.get_valor_litro() * 1.05  # Cálculo do preço com aditivo
        litros = valor / valor_com_aditivo  # Quantidade de litros com base no valor pago

        if litros > self.get_quantidade_disponivel():  # Usando o get da classe pai
            return -1  # Não há combustível suficiente

        # Atualiza a quantidade disponível
        self.set_quantidade_disponivel(self.get_quantidade_disponivel() - litros)
        return litros

    def abastecer_por_litro_com_aditivo(self, litros):
        if litros > self.get_quantidade_disponivel():  # Usando o get da classe pai
            return -1  # Não há combustível suficiente
        
        valor_com_aditivo = litros * self.get_valor_litro() * 1.05  # Cálculo do valor com aditivo
        self.set_quantidade_disponivel(self.get_quantidade_disponivel() - litros)
        return valor_com_aditivo

    def abastecer_por_litro(self, litros):
        if litros > self.get_quantidade_disponivel():  # Usando o get da classe pai
            print("Não há combustível suficiente.")
            return -1  # Não há combustível suficiente
        
        # Lógica para continuar o abastecimento
        print(f"Abastecido {litros} litros de gasolina.")
        self.set_quantidade_disponivel(self.get_quantidade_disponivel() - litros)  # Atualiza a quantidade
        return litros
