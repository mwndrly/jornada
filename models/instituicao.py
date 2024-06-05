# models
from models.rota import listar_rotas, buscar_rota
from models.aluno import listar_alunos, buscar_aluno
from models.motorista import listar_motoristas, buscar_motorista
from models.responsavel import listar_responsaveis, buscar_responsavel

# utils
import os
import json
import random

# constants
base_dir = os.path.join(os.path.dirname(__file__), '../data')
json_instituicoes = os.path.join(base_dir, 'instituicoes.json')

class Cor:
  VERMELHO = '\033[91m'
  AMARELO = '\033[93m'
  VERDE = '\033[92m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

def ler_json():
  with open(json_instituicoes, 'r') as f:
    return json.load(f)

def atualizar_json(response):
  with open(json_instituicoes, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_instituicao(user):
  instituicoes = ler_json()

  nome = input("DIGITE O NOME DA INSTITUIÇÃO:\n>>> ")
  cnpj = input("DIGITE O CNPJ:\n>>> ")
  telefone = input("DIGITE UM TELEFONE PARA CONTATO:\n>>> ")
  endereco = input("DIGITE O ENDEREÇO:\n>>> ")

  instituicoes.append({
    'id': random.randint(1, 1000),
    'nome': nome,
    'cnpj': cnpj,
    'endereco': endereco,
    'telefone': telefone,
  })

  atualizar_json(instituicoes)

def listar_instituicoes():
  instituicoes = ler_json()

  if instituicoes:
    print(">>>>>>> LISTA DE INSTITUIÇÕES <<<<<<<<")

    for instituicao in instituicoes:
      print("*" * 50)
      print(f"ID: {instituicao['id']}, NOME: {instituicao['nome']}, CNPJ: {instituicao['cnpj']}, TELEFONE: {instituicao['telefone']}, ENDEREÇO: {instituicao['endereco']}")
      print("*" * 50)
      print("=" * 50)
  else:
    print(Cor.AMARELO + "NENHUMA INSTITUIÇÃO CADASTRADA." + Cor.RESET)

def buscar_instituicoes(id):
  instituicoes = ler_json()
  id_da_instituicao = int(id)

  if not instituicoes:
      print(Cor.AMARELO + "NENHUMA INSTITUIÇÃO CADASTRADA." + Cor.RESET)

  for instituicao in instituicoes:
    if instituicao['id'] == id_da_instituicao:
      print(Cor.VERDE + ">>>>>>> INSTITUIÇÃO ENCOTNRADA <<<<<<<<" + Cor.RESET)
      print(f"ID: {instituicao['id']}, NOME: {instituicao['nome']}, CNPJ: {instituicao['cnpj']}, TELEFONE: {instituicao['telefone']}, ENDEREÇO: {instituicao['endereco']}")
    else:
      print(Cor.AMARELO + "NENHUMA INSTITUIÇÃO ENCONTRADA." + Cor.RESET)

def funcionalidades_instituicoes(user):
  while True:
    print("\nFUNCIONALIDADES DO PERFIL INSTITUIÇÃO:\n")
    print("1 - LISTAR MOTORISTAS")
    print("2 - BUSCAR MOTORISTA")
    print("3 - LISTAR ALUNOS")
    print("4 - BUSCAR ALUNO")
    print("5 - LISTAR RESPONSÁVEIS")
    print("6 - BUSCAR RESPONSÁVEL")
    print("7 - LISTAR ROTAS")
    print("8 - BUSCAR ROTA")
    print("9 - V0LTAR AO MENU")

    option = input("\n>>> ")

    if option == '1':
      listar_motoristas()

    elif option == '2':
      id_do_motorista= input("QUAL O ID DO MOTORISTA QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_motorista(id_do_motorista)

    elif option == '3':
      listar_alunos()

    elif option == '4':
      id_do_aluno = input("QUAL O ID DO ALUNO QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_aluno(id_do_aluno)

    elif option == '5':
      listar_responsaveis()

    elif option == '6':
      id_do_responsavel = input("QUAL O ID DO RESPONSÁVEL QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_responsavel(id_do_responsavel)

    elif option == '7':
      listar_rotas()

    elif option == '8':
      id_da_rota = input("QUAL O ID DA ROTA QUE VOCÊ DESEJA BUSCAR?\n>>> ")

      buscar_rota(id_da_rota)

    elif option == '9':
      break
    else:
      print(Cor.VERMELHO + "OPÇÃO INVÁLIDA" + Cor.RESET)