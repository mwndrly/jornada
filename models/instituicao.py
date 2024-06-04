# models
# from models.motorista import listar_motoristas

# utils
import os
import json

class Cor:
  VERMELHO = '\033[91m'
  AMARELO = '\033[93m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

base_dir = os.path.join(os.path.dirname(__file__), '../data')

json_instituicoes = os.path.join(base_dir, 'instituicoes.json')

def read_json():
  with open(json_instituicoes, 'r') as f:
    return json.load(f)

def update_json(response):
  with open(json_instituicoes, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_instituicao(user):
  instituicoes = read_json()

  nome = input("DIGITE O NOME DA INSTITUIÇÃO:\n>>> ")
  cnpj = input("DIGITE O CNPJ:\n>>> ")
  telefone = input("DIGITE UM TELEFONE PARA CONTATO:\n>>> ")
  endereco = input("DIGITE O ENDEREÇO:\n>>> ")

  instituicoes.append({
    'nome': nome,
    'cnpj': cnpj,
    'endereco': endereco,
    'telefone': telefone,
  })

  update_json(instituicoes)

def listar_instituicoes():
  instituicoes = read_json()

  if instituicoes:
    print(">>>>>>> LISTA DE INSTITUIÇÕES <<<<<<<<")

    for instituicao in instituicoes:
      print("*" * 50)
      print(f"NOME: {instituicao['nome']}, CNPJ: {instituicao['cnpj']}, TELEFONE: {instituicao['telefone']}, ENDEREÇO: {instituicao['endereco']}")
      print("*" * 50)
      print("=" * 50)
  else:
    print(Cor.AMARELO + "NENHUMA INSTITUIÇÃO CADASTRADA." + Cor.RESET)

def funcionalidades_instituicoes():
  go_on = True

  while go_on:
    print("FUNCIONALIDADES DO PERFIL INSTITUIÇÃO:\n")
    print("1 - LISTAR MOTORISTAS")
    print("2 - LISTAR ALUNOS")
    print("3 - SAIR")

    option = input("\n>>> ")

    if option == '1': print("a")

    elif option == '2': print("to do")

    elif option == '3':
      go_on = False

      print("ATÉ MAIS!👋🏻")
      print(Cor.CIANO + "USUÁRIO FEZ LOGOUT." + Cor.RESET)

    else:
      print(Cor.VERMELHO + "OPÇÃO INVÁLIDA" + Cor.RESET)