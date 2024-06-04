# models
from models.aluno import *
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
json_motoristas = os.path.join(base_dir, 'motoristas.json')
json_responsaveis = os.path.join(base_dir, 'responsaveis.json')
json_instituicoes = os.path.join(base_dir, 'instituicoes.json')

def start_app():
  load_files()
  login()

def load_files():
  files = [json_alunos, json_motoristas, json_responsaveis, json_instituicoes]

  for file in files:
    if not os.path.isfile(file):
      with open(file, 'w') as f:
        json.dump([], f)

def login():
  print(cor.CIANO + "=" * 55 + cor.RESET)
  print(cor.VERMELHO + " ---->>> BEM VINDO AO SISTEMA JORNADA <<<---- ")
  print("        SELECIONE O QUE VOCÊ DESEJA:")
  print("          1 - ENTRAR")
  print("          2 - CADASTRAR CONTA ")
  print(cor.CIANO + "=" * 55 + cor.RESET)

  option = input("\n>>> ")

  if option == '1':
    print("to do login")

  elif option == '2':
    register()

  else:
    print("Opção inválida.")
    login()

def register():
  print("\nMUITO BEM. VAMOS LÁ:")
  print("\nVOCÊ DESEJA CRIAR UMA CONTA COMO:")
  print("1 - ALUNO ")
  print("2 - MOTORISTA")
  print("3 - RESPONSÁVEL ")
  print("4 - INSTITUIÇÃO DE ENSINO ")

  account_type = input("\n>>> ")

  if account_type == '1':
    cadastrar_aluno()
    print(cor.VERDE + "\nALUNO ADICIONADO COM SUCESSO!" + cor.RESET)

  elif account_type == '2':
    cadastrar_motorista()
    print(cor.VERDE + "\nMOTORISTA ADICIONADO COM SUCESSO!" + cor.RESET)

  elif account_type == '3':
    cadastrar_responsavel()
    print(cor.VERDE + "\nRESPONSÁVEL ADICIONADO COM SUCESSO!" + cor.RESET)

  elif account_type == '4':
    cadastrar_instituicao()
    print(cor.VERDE + "\nINSTITUIÇÃO ADICIONADA COM SUCESSO!" + cor.RESET)

start_app()