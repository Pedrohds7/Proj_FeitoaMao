from models import Cliente, session

# Consultar todos os clientes cadastrados
todos_clientes = session.query(Cliente).all()

# Exibir os dados de todos os clientes
for cliente in todos_clientes:
    print("ID:", cliente.id)
    print("Nome:", cliente.nome)
    print("Endereço:", cliente.endereco)
    print("Telefone:", cliente.telefone)
    print("CPF:", cliente.cpf)
    print("Email:", cliente.email)
    print("Senha:", cliente.senha)
    print("--------------------")