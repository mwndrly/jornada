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
    'id': random.randint(1, 99),
    'nome': nome,
    'cpf': cpf,
    'endereco': endereco,
    'nascimento': nascimento,
    'id_do_responsavel': user['id']
  })

  atualizar_json(alunos)

def listar_alunos():
  alunos = ler_json()

  if alunos:
    print(">>>>>>> LISTA DE ALUNOS <<<<<<<<")

    for aluno in alunos:
      print("*" * 50)
      print(f"ID: {aluno['id']}, NOME: {aluno['nome']}, CPF: {aluno['cpf']}, ENDEREÇO: {aluno['endereco']}, NASCIMENTO: {aluno['nascimento']}, ID DO RESPONSÁVEL: {aluno['id_do_responsavel']}")
      print("*" * 50)
      print("=" * 50)
  else:
    print(Cor.AMARELO + "NENENHUM ALUNO CADASTRADO." + Cor.RESET)

def buscar_aluno(id):
  alunos = ler_json()
  id_do_aluno = int(id)

  for aluno in alunos:
    if aluno['id'] == id_do_aluno:

      print(f"ID: {aluno['id']}, NOME: {aluno['nome']}, CPF: {aluno['cpf']}, ENDEREÇO: {aluno['endereco']}, NASCIMENTO: {aluno['nascimento']}, ID DO RESPONSÁVEL: {aluno['id_do_responsavel']}")
    else:
      print(Cor.AMARELO + "NENHUM ALUNO ENCONTRADO." + Cor.RESET)

def excluir_aluno(id):
  alunos = ler_json()
  id_do_aluno = int(id)

  for aluno in alunos:
    if aluno['id'] == id_do_aluno:
      alunos.remove(aluno)

      atualizar_json(alunos)

      print(Cor.VERDE + "ALUNO EXCLUÍDO COM SUCESSO!" + Cor.RESET)
    else:
      print(Cor.AMARELO + "NENHUM ALUNO ENCONTRADO." + Cor.RESET)