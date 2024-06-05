# utils
import os
import json
import random

# constants
base_dir = os.path.join(os.path.dirname(__file__), '../data')
json_alunos = os.path.join(base_dir, 'alunos.json')

class Cor:
  AMARELO = '\033[93m'
  VERDE = '\033[92m'
  RESET = '\033[0m'

def ler_json():
  with open(json_alunos, 'r') as f:
    return json.load(f)

def atualizar_json(response):
  with open(json_alunos, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_aluno(user):
  alunos = ler_json()

  nome = input("DIGITE O NOME:\n>>> ")
  cpf = input("DIGITE O CPF:\n>>> ")
  nascimento = input("DIGITE A DATA DE NASCIMENTO NO FORMATO DD/MM/AAAA:\n>>> ")
  endereco = input("DIGITE O ENDEREÇO:\n>>> ")

  alunos.append({
    'id': random.randint(1, 1000),
    'nome': nome,
    'cpf': cpf,
    'endereco': endereco,
    'nascimento': nascimento,
    'id_do_responsavel': user['id']
  })

  atualizar_json(alunos)

def listar_alunos(user):
  alunos = ler_json()
  id_do_responsavel = int(user['id'])

  if alunos:
    for aluno in alunos:
      if aluno['id_do_responsavel'] == id_do_responsavel:
        print("*" * 50)
        print(f"ID: {aluno['id']}, NOME: {aluno['nome']}, CPF: {aluno['cpf']}, ENDEREÇO: {aluno['endereco']}, NASCIMENTO: {aluno['nascimento']}, ID DO RESPONSÁVEL: {aluno['id_do_responsavel']}")
        print("*" * 50)
        print("=" * 50)
      else:
       print(Cor.AMARELO + "NENENHUM ALUNO CADASTRADO." + Cor.RESET)
  else:
    print(Cor.AMARELO + "NENENHUM ALUNO CADASTRADO." + Cor.RESET)

def buscar_aluno(id, user):
  alunos = ler_json()
  id_do_aluno = int(id)
  id_do_responsavel = int(user['id'])

  for aluno in alunos:
    if aluno['id'] == id_do_aluno and aluno['id_do_responsavel'] == id_do_responsavel:

      print(f"ID: {aluno['id']}, NOME: {aluno['nome']}, CPF: {aluno['cpf']}, ENDEREÇO: {aluno['endereco']}, NASCIMENTO: {aluno['nascimento']}, ID DO RESPONSÁVEL: {aluno['id_do_responsavel']}")
    else:
      print(Cor.AMARELO + "NENHUM ALUNO ENCONTRADO." + Cor.RESET)

def atualizar_aluno(id, user):
  alunos = ler_json()
  id_do_aluno = int(id)
  id_do_responsavel = int(user['id'])

  for aluno in alunos:
    if aluno['id'] == id_do_aluno and aluno['id_do_responsavel'] == id_do_responsavel:
      aluno['nome'] = input("DIGITE O NOVO NOME:\n>>> ")
      aluno['cpf'] = input("DIGITE O NOVO CPF:\n>>> ")
      aluno['endereco'] = input("DIGITE O NOVO ENDEREÇO:\n>>> ")
      aluno['nascimento'] = input("DIGITE A NOVA DATA DE NASCIMENTO:\n>>> ")

      atualizar_json(alunos)
      print(Cor.VERDE + "ALUNO ATUALIZADO COM SUCESSO!" + Cor.RESET)
    else:
      print(Cor.AMARELO + "NENHUM ALUNO ENCONTRADO." + Cor.RESET)

def excluir_aluno(id, user):
  alunos = ler_json()
  id_do_aluno = int(id)
  id_do_responsavel = int(user['id'])

  for aluno in alunos:
    if aluno['id'] == id_do_aluno and aluno['id_do_responsavel'] == id_do_responsavel:
      alunos.remove(aluno)

      atualizar_json(alunos)

      print(Cor.VERDE + "ALUNO EXCLUÍDO COM SUCESSO!" + Cor.RESET)
    else:
      print(Cor.AMARELO + "NENHUM ALUNO ENCONTRADO." + Cor.RESET)