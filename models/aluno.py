import os
import json

base_dir = os.path.join(os.path.dirname(__file__), '../data')

json_alunos = os.path.join(base_dir, 'alunos.json')

def read_json():
  with open(json_alunos, 'r') as f:
    return json.load(f)

def update_json(response):
  with open(json_alunos, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_aluno():
  alunos = read_json()

  nome = input("DIGITE O NOME:\n>>> ")
  idade = input("DIGITE A IDADE:\n>>> ")
  cpf = input("DIGITE SEU CPF:\n>>> ")
  nascimento = input("DIGITE O DIA DE SEU NASCIMENTO:\n>>> ")
  telefone = input("DIGITE SEU NÚMERO DE TELEFONE:\n>>> ")
  endereco = input("DIGITE SEU ENDEREÇO:\n>>> ")
  email = input("DIGITE SEU EMAIL:\n>>> ")

  alunos.append({
    'cpf': cpf,
    'nome': nome,
    'idade': idade,
    'email': email,
    'endereco': endereco,
    'telefone': telefone,
    'nascimento': nascimento,
  })

  update_json(alunos)