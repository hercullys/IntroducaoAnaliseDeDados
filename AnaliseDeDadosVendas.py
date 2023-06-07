from sys import displayhook
import pandas as pd


# O pandas trabalha muito bem com analise de dados
# Trazer a base de dados
tabela = pd.read_excel("Vendas.xlsx")
displayhook(tabela)

# Calcular o faturamento total
faturamentoTotal = tabela["Valor Final"].sum()
print(faturamentoTotal)

# Analise topDown - faturamento por loja
faturamentoPorLoja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
displayhook(faturamentoPorLoja)

faturamentoPorProduto = tabela[["ID Loja","Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
displayhook(faturamentoPorProduto)
