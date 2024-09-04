from bomba_etanol import BombaEtanol
from bomba_gasolina import BombaGasolina

def exibir_menu():
    "Exibe o menu de opções para o usuário."
    print("\nMenu:"
        "1. Abastecer Etanol por valor"
        "2. Abastecer Etanol por litro"
        "3. Abastecer Gasolina por valor"
        "4. Abastecer Gasolina por litro"
        "5. Abastecer Gasolina com aditivo por valor"
        "6. Abastecer Gasolina com aditivo por litro"
        "7. Mostrar status das bombas"
        "0. Sair"
          )

def main():
    "Função principal que executa o menu e gerencia a interação com o usuário."
    #Inicializa as bombas de combustível
    bomba_etanol = BombaEtanol(3.59, 1000)
    bomba_gasolina = BombaGasolina(4.89, 1000)
    
    while True:
        exibir_menu()  #Exibe o menu de opções
        escolha = input("Escolha uma opção: ")
        
        try:
            if escolha == '1':
                #Abastecer Etanol por valor
                valor = float(input("Digite o valor para abastecimento com Etanol: "))
                resultado = bomba_etanol.abastecer_por_valor(valor)
                if resultado == -1:
                    print("Quantidade de Etanol insuficiente.")
                else:
                    print(f"Abastecido {resultado:.2f} litros de Etanol.")
            
            elif escolha == '2':
                #Abastecer Etanol por litro
                litros = float(input("Digite a quantidade de litros para abastecimento com Etanol: "))
                resultado = bomba_etanol.abastecer_por_litro(litros)
                if resultado == -1:
                    print("Quantidade de Etanol insuficiente.")
                else:
                    print(f"Valor a ser pago: R$ {resultado:.2f}.")
            
            elif escolha == '3':
                #Abastecer Gasolina por valor
                valor = float(input("Digite o valor para abastecimento com Gasolina: "))
                resultado = bomba_gasolina.abastecer_por_valor(valor)
                if resultado == -1:
                    print("Quantidade de Gasolina insuficiente.")
                else:
                    print(f"Abastecido {resultado:.2f} litros de Gasolina.")
            
            elif escolha == '4':
                #Abastecer Gasolina por litro
                litros = float(input("Digite a quantidade de litros para abastecimento com Gasolina: "))
                resultado = bomba_gasolina.abastecer_por_litro(litros)
                if resultado == -1:
                    print("Quantidade de Gasolina insuficiente.")
                else:
                    print(f"Valor a ser pago: R$ {resultado:.2f}.")
            
            elif escolha == '5':
                #Abastecer Gasolina com aditivo por valor
                valor = float(input("Digite o valor para abastecimento com Gasolina com aditivo: "))
                resultado = bomba_gasolina.abastecer_por_valor_com_aditivo(valor)
                if resultado == -1:
                    print("Quantidade de Gasolina insuficiente.")
                else:
                    print(f"Abastecido {resultado:.2f} litros de Gasolina com aditivo.")
            
            elif escolha == '6':
                #Abastecer Gasolina com aditivo por litro
                litros = float(input("Digite a quantidade de litros para abastecimento com Gasolina com aditivo: "))
                resultado = bomba_gasolina.abastecer_por_litro_com_aditivo(litros)
                if resultado == -1:
                    print("Quantidade de Gasolina insuficiente.")
                else:
                    print(f"Valor a ser pago com aditivo: R$ {resultado:.2f}.")
            
            elif escolha == '7':
                #Mostrar status das bombas
                print(f"Etanol - Valor por litro: R$ {bomba_etanol.get_valor_litro():.2f}, Quantidade disponível: {bomba_etanol.get_quantidade_disponivel():.2f} litros")
                print(f"Gasolina - Valor por litro: R$ {bomba_gasolina.get_valor_litro():.2f}, Quantidade disponível: {bomba_gasolina.get_quantidade_disponivel():.2f} litros")
            
            elif escolha == '0':
                #Sair do programa
                print("Saindo...")
                break
            
            else:
                #Caso a opção escolhida não seja válida
                print("Opção inválida, tente novamente.")
        
        except ValueError: #Caso escreva uma letra na escolha da quantidade de litros
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()
