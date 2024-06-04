# models
from models.instituicao import listar_instituicoes

# utils
import os
import json
import random

# Define o diretório base para os arquivos JSON
base_dir = os.path.join(os.path.dirname(__file__), '../data')

json_motoristas = os.path.join(base_dir, 'motoristas.json')

class cor:
  VERMELHO = '\033[91m'
  AMARELO = '\033[93m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

def read_json():
  with open(json_motoristas, 'r') as f:
    return json.load(f)

def update_json(response):
  with open(json_motoristas, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_motorista(user):
  motoristas = read_json()

  nome = input("DIGITE O NOME:\n>>>")
  genero = input("DIGITE O GÊNERO:\n>>>")
  cpf = input("DIGITE SEU CPF:\n>>>")
  nascimento = input("DIGITE A DATA DE NASCIMENTO NO FORMATO DD/MM/AAAA:\n>>>")
  telefone = input("DIGITE O NÚMERO DE TELEFONE:\n>>>")
  endereco = input("DIGITE O ENDEREÇO:\n>>>")

  if not user:
    email = input("DIGITE O EMAIL:\n>>> ")

  motoristas.append({
    'id': random.randint(1, 99),
    'nome': nome,
    'cpf': cpf,
    'genero': genero,
    'telefone': telefone,
    'endereco': endereco,
    'nascimento': nascimento,
    'email': user['email'] or email,
    'id_usuario': user['id']
  })

  update_json(motoristas)

def listar_motoristas():
  motoristas = read_json()

  if motoristas:
    print(">>>>>>> LISTA DE MOTORISTAS <<<<<<<<")

    for motorista in motoristas:
      print("*" * 50)
      print(f"NOME: {motorista['nome']}, IDADE: {motorista['idade']}, CPF: {motorista['cpf']}, NASCIMENTO: {motorista['nascimento']}, TELEFONE: {motorista['telefone']}, ENDEREÇO: {motorista['endereco']}, EMAIL: {motorista['email']}")
      print("*" * 50)
      print("=" * 50)
  else:
    print(cor.AMARELO + "NENENHUM MOTORISTA CADASTRADO." + cor.RESET)

def buscar_motorista(id):
  found = False
  motoristas = read_json()

  for motorista in motoristas:
    if motorista['id'] == id:
      found = True

      print(f"NOME: {motorista['nome']}, IDADE: {motorista['idade']}, CPF: {motorista['cpf']}, NASCIMENTO: {motorista['nascimento']}, TELEFONE: {motorista['telefone']}, ENDEREÇO: {motorista['endereco']}, EMAIL: {motorista['email']}")
  if not found:
    print(cor.AMARELO + "NENHUM MOTORISTA ENCONTRADO." + cor.RESET)

def funcionalidades_motoristas():
  go_on = True

  while go_on:
    print("\nFUNCIONALIDADES DO PERFIL MOTORISTA:\n")
    print("1 - LISTAR INSTITUIÇÕES DE ENSINO")
    print("2 - CADASTRAR ROTA")
    print("3 - LISTAR ROTAS")
    print("4 - EXCLUIR ROTA")
    print("5 - BUSCAR ALUNO")
    print("6 - SAIR")

    option = input("\n>>> ")

    if option == '1': listar_instituicoes()

    elif option == '2': print("to do")

    elif option == '3': print("to do")

    elif option == '4': print("to do")

    elif option == '5': print("to do")

    elif option == '6':
      go_on = False

      print("ATÉ MAIS!👋🏻")
      print(cor.CIANO + "USUÁRIO FEZ LOGOUT." + cor.RESET)

    else:
      print(cor.VERMELHO + "OPÇÃO INVÁLIDA" + cor.RESET)