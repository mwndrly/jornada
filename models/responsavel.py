import os
import json

base_dir = os.path.join(os.path.dirname(__file__), '../data')

json_responsaveis = os.path.join(base_dir, 'responsaveis.json')

class cor:
  VERMELHO = '\033[91m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

def read_json():
  with open(json_responsaveis, 'r') as f:
    return json.load(f)

def update_json(response):
  with open(json_responsaveis, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_responsavel(user):
  responsaveis = read_json()

  nome = input("DIGITE O NOME:\n>>> ")
  cpf = input("DIGITE O CPF:\n>>> ")
  nascimento = input("DIGITE A DATA DE NASCIMENTO NO FORMATO DD/MM/AAAA:\n>>>")
  telefone = input("DIGITE O NÚMERO DE TELEFONE:\n>>> ")
  endereco = input("DIGITE 0 ENDEREÇO:\n>>> ")

  if not user:
    email = input("DIGITE O EMAIL:\n>>> ")

  responsaveis.append({
    'nome': nome,
    'cpf': cpf,
    'endereco': endereco,
    'telefone': telefone,
    'nascimento': nascimento,
    'email': user['email'] or email,
    'id_usuario': user['id'],
  })

  update_json(responsaveis)

def funcionalidades_responsaveis():
  go_on = True

  while go_on:
    print("\nFUNCIONALIDADES DO PERFIL RESPONSAVEL:\n")
    print("1 - BUSCAR ROTA")
    print("2 - LISTAR ROTAS")
    print("3 - BUSCAR MOTORISTA")
    print("4 - LISTAR MOTORISTAS")
    print("5 - CADASTRAR ALUNO")
    print("6 - BUSCAR ALUNO")
    print("7 - EXCLUIR ALUNO")
    print("8 - SAIR")

    option = input("\n>>> ")

    if option == '1': print("to do")

    elif option == '2': print("to do")

    elif option == '3': print("to do")

    elif option == '4': print("to do")

    elif option == '5': print("to do")

    elif option == '8':
      go_on = False

      print("ATÉ MAIS!👋🏻")
      print(cor.CIANO + "USUÁRIO FEZ LOGOUT." + cor.RESET)

    else:
      print(cor.VERMELHO + "OPÇÃO INVÁLIDA" + cor.RESET)