# models
from models.aluno import *
from models.usuario import *
from models.motorista import *
from models.responsavel import *
from models.instituicao import *

# utils
import json
import os

class cor:
  VERMELHO = '\033[91m'
  VERDE = '\033[92m'
  AMARELO = '\033[93m'
  AZUL = '\033[94m'
  MAGENTA = '\033[95m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

# Define o diretório base para os arquivos JSON
base_dir = os.path.join(os.path.dirname(__file__), 'data')

# Garante que o diretório 'data' exista
os.makedirs(base_dir, exist_ok=True)

json_alunos = os.path.join(base_dir, 'alunos.json')
json_usuarios = os.path.join(base_dir, 'usuarios.json')
json_motoristas = os.path.join(base_dir, 'motoristas.json')
json_responsaveis = os.path.join(base_dir, 'responsaveis.json')
json_instituicoes = os.path.join(base_dir, 'instituicoes.json')

def start_app():
  load_files()
  login()

def load_files():
  files = [
    json_usuarios,
    json_alunos,
    json_motoristas,
    json_responsaveis,
    json_instituicoes
  ]

  for file in files:
    if not os.path.isfile(file):
      with open(file, 'w') as f:
        json.dump([], f)

def login():
  print(cor.CIANO + "=" * 55 + cor.RESET)
  print(cor.VERMELHO + " ---->>> BEM VINDO AO JORNADA <<<---- ")
  print("SELECIONE O QUE VOCÊ DESEJA:")
  print("1 - ENTRAR")
  print("2 - CADASTRAR CONTA ")
  print(cor.CIANO + "=" * 55 + cor.RESET)

  option = input("\n>>> ")

  if option == '1': login()

  elif option == '2': register()

  else:
    print(cor.VERMELHO + "OPÇÃO INVÁLIDA" + cor.RESET)
    login()

def register():
  print("\nMUITO BEM. VAMOS LÁ:")
  print("\nVOCÊ DESEJA CRIAR UMA CONTA COMO:")
  print("1 - MOTORISTA")
  print("2 - RESPONSÁVEL ")
  print("3 - INSTITUIÇÃO DE ENSINO ")

  account_type = input("\n>>> ")

  if account_type == '1':
    user = cadastrar_usuario("motorista")

    cadastrar_motorista(user)
    print(cor.VERDE + "\nMOTORISTA ADICIONADO COM SUCESSO!" + cor.RESET)
    funcionalidades_motoristas()

  elif account_type == '2':
    user = cadastrar_usuario("responsavel")

    cadastrar_responsavel(user)
    print(cor.VERDE + "\nRESPONSÁVEL ADICIONADO COM SUCESSO!" + cor.RESET)
    funcionalidades_responsaveis()

  elif account_type == '3':
    user = cadastrar_usuario("instituicao")

    cadastrar_instituicao(user)
    print(cor.VERDE + "\nINSTITUIÇÃO ADICIONADA COM SUCESSO!" + cor.RESET)
    funcionalidades_instituicoes()

  else:
    print(cor.VERMELHO + "OPÇÃO INVÁLIDA" + cor.RESET)

start_app()