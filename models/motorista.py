# models
from models.rotas import *

# utils
import os
import json
import random

# constants
base_dir = os.path.join(os.path.dirname(__file__), '../data')
json_motoristas = os.path.join(base_dir, 'motoristas.json')

class Cor:
  VERMELHO = '\033[91m'
  AMARELO = '\033[93m'
  VERDE = '\033[92m'
  RESET = '\033[0m'

def ler_json():
  with open(json_motoristas, 'r') as f:
    return json.load(f)

def atualizar_json(response):
  with open(json_motoristas, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_motorista(user):
  motoristas = ler_json()

  nome = input("DIGITE O NOME:\n>>> ")
  genero = input("DIGITE O GÊNERO:\n>>> ")
  cpf = input("DIGITE SEU CPF:\n>>> ")
  nascimento = input("DIGITE A DATA DE NASCIMENTO NO FORMATO DD/MM/AAAA:\n>>> ")
  telefone = input("DIGITE O NÚMERO DE TELEFONE:\n>>> ")
  endereco = input("DIGITE O ENDEREÇO:\n>>> ")

  if not user:
    email = input("DIGITE O EMAIL:\n>>> ")

  motoristas.append({
    'id': random.randint(1, 1000),
    'nome': nome,
    'cpf': cpf,
    'genero': genero,
    'telefone': telefone,
    'endereco': endereco,
    'nascimento': nascimento,
    'email': user['email'] or email,
    'id_usuario': user['id']
  })

  atualizar_json(motoristas)

def listar_motoristas():
  motoristas = ler_json()

  if motoristas:
    print(">>>>>>> LISTA DE MOTORISTAS <<<<<<<<")

    for motorista in motoristas:
      print("*" * 50)
      print(f"ID: {motorista['id']}, NOME: {motorista['nome']}, GENERO: {motorista['genero']}, CPF: {motorista['cpf']}, NASCIMENTO: {motorista['nascimento']}, TELEFONE: {motorista['telefone']}, ENDEREÇO: {motorista['endereco']}, EMAIL: {motorista['email']}")
      print("*" * 50)
      print("=" * 50)
  else:
    print(Cor.AMARELO + "NENENHUM MOTORISTA CADASTRADO." + Cor.RESET)

def buscar_motorista(id):
  motoristas = ler_json()
  id_do_motorista = int(id)

  if not motoristas:
    print(Cor.AMARELO + "NENHUM MOTORISTA CADASTRADO." + Cor.RESET)

  for motorista in motoristas:
    if motorista['id'] == id_do_motorista:

      print(Cor.VERDE + ">>>>>>> MOTORISTA ENCOTNRADO <<<<<<<<" + Cor.RESET)
      print(f"ID: {motorista['id']}, NOME: {motorista['nome']}, GENERO: {motorista['genero']}, CPF: {motorista['cpf']}, NASCIMENTO: {motorista['nascimento']}, TELEFONE: {motorista['telefone']}, ENDEREÇO: {motorista['endereco']}, EMAIL: {motorista['email']}")
    else:
      print(Cor.AMARELO + "NENHUM MOTORISTA ENCONTRADO." + Cor.RESET)

def funcionalidades_motoristas(user):
  while True:
    print("\nFUNCIONALIDADES DO PERFIL MOTORISTA:\n")
    print("1 - CADASTRAR ROTA")
    print("2 - LISTAR ROTAS")
    print("3 - BUSCAR ROTA")
    print("4 - EDITAR ROTA")
    print("5 - EXCLUIR ROTA")
    print("6 - V0LTAR AO MENU")

    option = input("\n>>> ")

    if option == '1':
      cadastrar_rota(user)

    elif option == '2':
      listar_rotas()

    elif option == '3':
      id_da_rota = input("QUAL O ID DA ROTA QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_rota(id_da_rota)

    elif option == '4':
      id_da_rota = input("QUAL O ID DA ROTA QUE VOCÊ DESEJA EDITAR?\n>>> ")

      editar_rota(id_da_rota)

    elif option == '5':
      id_da_rota = input("QUAL O ID DA ROTA QUE VOCÊ DESEJA DELETAR?\n>>> ")

      excluir_rota(id_da_rota)

    elif option == '6':
      break
    else:
      print(Cor.VERMELHO + "OPÇÃO INVÁLIDA" + Cor.RESET)