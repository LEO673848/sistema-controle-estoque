estoque = {}
 
while True:
print("\n=== CONTROLE DE ESTOQUE ===")
print("1 - Cadastrar produto")
print("2 - Entrada de mercadoria")
print("3 - Saída de mercadoria")
print("4 - Consultar estoque")
print("5 - Sair")
 
opcao = input("Escolha uma opção: ")
 
if opcao == "1":
produto = input("Nome do produto: ")
quantidade = int(input("Quantidade inicial: "))
estoque[produto] = quantidade
print("Produto cadastrado com sucesso!")
 
elif opcao == "2":
produto = input("Produto: ")
if produto in estoque:
quantidade = int(input("Quantidade a adicionar: "))
estoque[produto] += quantidade
print("Estoque atualizado!")
else:
print("Produto não encontrado.")
 
elif opcao == "3":
produto = input("Produto: ")
if produto in estoque:
quantidade = int(input("Quantidade a retirar: "))
if quantidade <= estoque[produto\]:
estoque[produto] -= quantidade
print("Saída registrada!")
else:
print("Quantidade insuficiente em estoque.")
oduto não encontrado.")
 
elif opcao == "4":
print("\n=== ESTOQUE ATUAL ===")
for produto, quantidade in estoque.items():
print(f"{produto}: {quantidade}")
 
elif opcao == "5":
print("Sistema encerrado.")
break
 
else:
print("Opção inválida.")
