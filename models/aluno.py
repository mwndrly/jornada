# models
from models.motorista import listar_motoristas

# utils
import os
import json

class cor:
  VERMELHO = '\033[91m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

base_dir = os.path.join(os.path.dirname(__file__), '../data')

json_alunos = os.path.join(base_dir, 'alunos.json')

def read_json():
  with open(json_alunos, 'r') as f:
    return json.load(f)

def update_json(response):
  with open(json_alunos, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_aluno():
  alunos = read_json()

  nome = input("DIGITE O NOME:\n>>> ")
  idade = input("DIGITE A IDADE:\n>>> ")
  cpf = input("DIGITE O CPF:\n>>> ")
  nascimento = input("DIGITE A DATA DE NASCIMENTO NO FORMATO DD/MM/AAAA:\n>>> ")
  telefone = input("DIGITE O NÚMERO DE TELEFONE:\n>>> ")
  endereco = input("DIGITE O ENDEREÇO:\n>>> ")
  email = input("DIGITE O EMAIL:\n>>> ")

  alunos.append({
    'cpf': cpf,
    'nome': nome,
    'idade': idade,
    'email': email,
    'endereco': endereco,
    'telefone': telefone,
    'nascimento': nascimento,
  })

  update_json(alunos)

def funcionalidades_alunos():
  go_on = True

  while go_on:
    print("\nFUNCIONALIDADES DO PERFIL ALUNO:\n")
    print("1 - LISTAR MOTORISTAS")
    print("2 - LISTAR ROTAS")
    print("3 - SAIR")

    option = input("\n>>> ")

    if option == '1':
      listar_motoristas()

    elif option == '2':
      print("to do")

    elif option == '3':
      go_on = False

      print("ATÉ MAIS!👋🏻")
      print(cor.CIANO + "USUÁRIO FEZ LOGOUT." + cor.RESET)

    else:
      print(cor.VERMELHO + "OPÇÃO INVÁLIDA" + cor.RESET)