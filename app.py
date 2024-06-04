# models
from models.aluno import *
from models.usuario import *
from models.motorista import *
from models.responsavel import *
from models.instituicao import *

# utils
import json
import os

# constants
BASE_DIR = os.path.join(os.path.dirname(__file__), 'data')
JSON_FILES = {
  'rotas': os.path.join(BASE_DIR, 'rotas.json'),
  'alunos': os.path.join(BASE_DIR, 'alunos.json'),
  'usuarios': os.path.join(BASE_DIR, 'usuarios.json'),
  'motoristas': os.path.join(BASE_DIR, 'motoristas.json'),
  'responsaveis': os.path.join(BASE_DIR, 'responsaveis.json'),
  'instituicoes': os.path.join(BASE_DIR, 'instituicoes.json')
}

class Cor:
  VERMELHO = '\033[91m'
  VERDE = '\033[92m'
  CIANO = '\033[96m'
  RESET = '\033[0m'

def garantir_diretorio(diretorio):
  os.makedirs(diretorio, exist_ok=True)

def inicializar_arquivos_json():
  for files in JSON_FILES.values():
    if not os.path.isfile(files):
      with open(files, 'w') as f:
        json.dump([], f)

def iniciar_aplicacao():
  garantir_diretorio(BASE_DIR)
  inicializar_arquivos_json()

  while True:
    exibir_menu_inicial()

    opcao = input("\n>>> ")

    if opcao == '1':
      login()
    elif opcao == '2':
      registrar_usuario()
    else:
      print(Cor.VERMELHO + "OPÇÃO INVÁLIDA" + Cor.RESET)

def exibir_menu_inicial():
  print(Cor.CIANO + "=" * 55)
  print(" ---->>> BEM VINDO AO JORNADA <<<---- ")
  print("SELECIONE O QUE VOCÊ DESEJA:")
  print("1 - ENTRAR")
  print("2 - CADASTRAR CONTA")
  print("=" * 55 + Cor.RESET)

def login():
  usuario_autenticado = autenticar_usuario()

  if usuario_autenticado:
    print(Cor.VERDE + "Autenticação bem-sucedida!" + Cor.RESET)

    listar_funcionalidades(usuario_autenticado)
  else:
    print(Cor.VERMELHO + "Autenticação falhou. Login ou senha incorretos." + Cor.RESET)

def registrar_usuario():
  print("\nMUITO BEM. VAMOS LÁ:")
  print("\nVOCÊ DESEJA CRIAR UMA CONTA COMO:")
  print("1 - MOTORISTA")
  print("2 - RESPONSÁVEL")
  print("3 - INSTITUIÇÃO DE ENSINO")

  tipo_conta = input("\n>>> ")

  if tipo_conta in ['1', '2', '3']:
    criar_conta(tipo_conta)
  else:
    print(Cor.VERMELHO + "OPÇÃO INVÁLIDA" + Cor.RESET)

def criar_conta(tipo_conta):
  tipos_conta = {
    '1': ('motorista', cadastrar_motorista, funcionalidades_motoristas),
    '2': ('responsavel', cadastrar_responsavel, funcionalidades_responsaveis),
    '3': ('instituicao', cadastrar_instituicao, funcionalidades_instituicoes)
  }

  tipo, cadastro_de_conta, funcionalidades_da_conta = tipos_conta[tipo_conta]

  usuario = cadastrar_usuario(tipo)

  cadastro_de_conta(usuario)
  print(Cor.VERDE + f"\n{tipo.upper()} ADICIONADO COM SUCESSO!" + Cor.RESET)
  funcionalidades_da_conta(usuario)

def listar_funcionalidades(usuario):
  tipos_conta = {
    'motorista': (funcionalidades_motoristas),
    'responsavel': (funcionalidades_responsaveis),
    'instituicao': (funcionalidades_instituicoes)
  }
  funcionalidades_da_conta = tipos_conta[usuario['tipo']]

  funcionalidades_da_conta(usuario)

iniciar_aplicacao()