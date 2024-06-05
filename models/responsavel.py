# models
from models.aluno import *
from models.rotas import listar_rotas, buscar_rota
from models.motorista import listar_motoristas, buscar_motorista

# utils
import os
import json

# constants
base_dir = os.path.join(os.path.dirname(__file__), '../data')
json_responsaveis = os.path.join(base_dir, 'responsaveis.json')

class Cor:
  VERMELHO = '\033[91m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

def ler_json():
  with open(json_responsaveis, 'r') as f:
    return json.load(f)

def atualizar_json(response):
  with open(json_responsaveis, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_responsavel(user):
  responsaveis = ler_json()

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

  atualizar_json(responsaveis)

def listar_responsaveis():
  responsaveis = ler_json()

  if responsaveis:
    print(">>>>>>> LISTA DE RESPONSÁVEIS <<<<<<<<")

    for responsavel in responsaveis:
      print("*" * 50)
      print(f"NOME: {responsavel['nome']}, CPF: {responsavel['cpf']}, NASCIMENTO: {responsavel['nascimento']}, TELEFONE: {responsavel['telefone']}, ENDEREÇO: {responsavel['endereco']}, EMAIL: {responsavel['email']}")
      print("*" * 50)
      print("=" * 50)
  else:
    print(Cor.AMARELO + "NENENHUM RESPONSÁVEL CADASTRADO." + Cor.RESET)

def buscar_responsavel(id):
  responsaveis = ler_json()

  if not responsaveis:
    print(Cor.AMARELO + "NENHUM MOTORISTA CADASTRADO." + Cor.RESET)

  for responsavel in responsaveis:
    if responsavel['id'] == id:

      print(f"NOME: {responsavel['nome']}, CPF: {responsavel['cpf']}, NASCIMENTO: {responsavel['nascimento']}, TELEFONE: {responsavel['telefone']}, ENDEREÇO: {responsavel['endereco']}, EMAIL: {responsavel['email']}")
    else:
      print(Cor.AMARELO + "NENHUM RESPONSAVEL ENCONTRADO." + Cor.RESET)

def funcionalidades_responsaveis(user):
  while True:
    print("\nFUNCIONALIDADES DO PERFIL RESPONSAVEL:\n")
    print("1 - CADASTRAR ALUNO")
    print("2 - LISTAR ALUNOS")
    print("3 - BUSCAR ALUNO")
    print("4 - EDITAR ALUNO")
    print("5 - EXCLUIR ALUNO")
    print("6 - LISTAR ROTAS")
    print("7 - BUSCAR ROTA")
    print("8 - LISTAR MOTORISTAS")
    print("9 - BUSCAR MOTORISTA")
    print("10 - VOLTAR AO MENU")

    option = input("\n>>> ")

    if option == '1':
      cadastrar_aluno(user)

    elif option == '2':
      listar_alunos(user)

    elif option == '3':
      id_do_aluno = input("QUAL O ID DO ALUNO QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_aluno(id_do_aluno, user)

    elif option == '4':
      id_do_aluno = input("QUAL O ID DO ALUNO QUE VOCÊ DESEJA EDITAR?\n>>> ")

      atualizar_aluno(id_do_aluno, user)

    elif option == '5':
      id_do_aluno = input("QUAL O ID DO ALUNO QUE VOCÊ DESEJA EXCLUIR?\n>>> ")

      excluir_aluno(id_do_aluno, user)

    elif option == '6':
        listar_rotas()

    elif option == '7':
      id_da_rota = input("QUAL O ID DA ROTA QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_rota(id_da_rota)

    elif option == '8':
      listar_motoristas()

    elif option == '9':
      id_do_motorista = input("QUAL O ID DO MOTORISTA QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_motorista(id_do_motorista)

    elif option == '10':
      break
    else:
      print(Cor.VERMELHO + "OPÇÃO INVÁLIDA" + Cor.RESET)