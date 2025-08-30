LIMITE_SAQUE = 3
VALOR_MA_SAQUE = 500
AGENCIA = "0001"
def menu():
  menu = """\n
  ====================BEM VINDO AO MENU DO BANCO TABAJARA========================
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Novo usuário
  [5] Nova conta
  [6] Listar contas
  [7] Listar usuários
  [0] Sair
  ==>>>
  """
  return input(menu)

def main():
  """Função principal do sistema"""
  saldo = 0
  numeros_saques = 0
  extrato = ""
  usuarios = []
  contas = []


  while True:
    opcao = menu()
    match opcao:
      case "1":
        valor = float(input("Digite o valor do deposito: "))
        saldo,extrato = deposito(saldo,valor,extrato)
      case "4":
        usuarios = criar_usuario(usuarios)
      case "5":
        contas = criar_conta(usuarios,contas, AGENCIA)
      case "0":
        print("\nObrigado por utilizar o nossos serviços volte sempre!!")
        break
      case _:
        print("⚠️ Operação inválida! Selecione novamente.")

def criar_usuario(usuarios):
   """Cadastra um novo usuário no sistema"""
   cpf = input("Informe o CPF (somente número): ")
   usuario = filtrar_usuario(cpf, usuarios)
   if usuario:
    print("\n⚠️ Já existe usuário com esse CPF!")
    return
   nome = input("Digite nome completo: ")
   data_nascimento = input("Digite a data de nascimento no formato dia/mes/ano: ")
   endereco = input("Digite o endereço completo (logradouro, nº, bairro, cidade/sigla do estado): ")
   usuarios.append({ "nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
   print("✅ Usuário criado com sucesso!")
   return usuarios


def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuarios,contas,AGENCIA):
  """Cria uma nova conta bancária"""
  cpf = input("Digite o CPF")
  usuario_filtrado = filtrar_usuario(cpf, usuarios)
  if usuario_filtrado:
    numero_conta = len(contas) + 1
    conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario_filtrado }
    contas.append(conta)
    print(f"✅ Conta criada com sucesso!")
    print(f"Agência: {AGENCIA}")
    print(f"Conta: {numero_conta}")
    print(f"Titular: {usuario_filtrado['nome']}")
  else:
    print("\n⚠️ Usuário não encontrado! Cadastre o usuário primeiro.")
  return contas



    

if __name__ == "__main__":
  main()
