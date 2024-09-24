class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self.__valor_litro = valor_litro  # Encapsulado
        self.__quantidade_disponivel = quantidade_disponivel  # Encapsulado

    def abastecer_por_valor(self, valor):
        litros = valor / self.get_valor_litro()  # Chamando diretamente o método correto
        if litros > self.__quantidade_disponivel:
            return -1  # Não há combustível suficiente
        self.__quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        if litros > self.__quantidade_disponivel:
            return -1  # Não há combustível suficiente
        valor = litros * self.get_valor_litro()  # Chamando o método getter para valor_litro
        self.__quantidade_disponivel -= litros
        return valor

    def get_valor_litro(self):
        return self.__valor_litro  # Retornando o valor do atributo encapsulado

    def set_valor_litro(self, valor_litro):
        self.__valor_litro = valor_litro  # Corrigido para alterar o atributo privado

    def get_quantidade_disponivel(self):
        return self.__quantidade_disponivel

    def set_quantidade_disponivel(self, quantidade_disponivel):
        self.__quantidade_disponivel = quantidade_disponivel
