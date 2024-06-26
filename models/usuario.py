# utils
import os
import json
import random

# constants
base_dir = os.path.join(os.path.dirname(__file__), '../data')
json_usuarios = os.path.join(base_dir, 'usuarios.json')

def ler_json():
  with open(json_usuarios, 'r') as f:
    return json.load(f)

def atualizar_json(response):
  with open(json_usuarios, 'w') as f:
    json.dump(response, f, indent=2)

def autenticar_usuario():
  usuarios = ler_json()

  email = input('DIGITE O EMAIL: ')
  senha = input('DIGITE A SENHA: ')

  for usuario in usuarios:
    if usuario['email'] == email and usuario['senha'] == senha:
      return usuario
  return False

def cadastrar_usuario(tipo):
  usuarios = ler_json()

  email = input("DIGITE SEU EMAIL:\n>>> ")
  senha = input("DIGITE SUA SENHA:\n>>> ")

  usuario = {
    'id': random.randint(1, 1000),
    'email': email,
    'senha': senha,
    'tipo': tipo
  }

  usuarios.append(usuario)

  atualizar_json(usuarios)

  return usuario