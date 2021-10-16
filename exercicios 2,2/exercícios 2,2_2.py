#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%.
#O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional.
#Qual é o custo total de atacado para 60 cópias?

class livro:
    def __init__(self, preço, desconto):
        self.unidade = preço - (preço * (desconto/100))
        print(f'O preço do desconto é {self.unidade:.2f} reais')

    def transporte(self, primeiro, adicional):
        self.total = primeiro + (adicional * 59)
        print(f'o valor total do transporte para a biblioteca é {self.total} reais')

    def custo_total(self, atacado):
        self.atacado = atacado
        self.valor_pago = (self.unidade * self.atacado) + self.total
        print(f'Os livros no atacado custam {self.valor_pago:.2f} reais')

livros = livro(24.95, 40)
livros.transporte(3, .75)
livros.custo_total(60)


