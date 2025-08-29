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
  while True:
    opcao = menu()

if __name__ == "__main__":
  main()
