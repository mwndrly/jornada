# utils
import os
import json
import random

base_dir = os.path.join(os.path.dirname(__file__), '../data')

json_usuarios = os.path.join(base_dir, 'usuarios.json')

def read_json():
  with open(json_usuarios, 'r') as f:
    return json.load(f)

def update_json(response):
  with open(json_usuarios, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_usuario(type):
  usuarios = read_json()

  email = input("DIGITE SEU EMAIL:\n>>> ")
  senha = input("DIGITE SUA SENHA:\n>>> ")

  usuario = {
    'id': random.randint(1, 99),
    'email': email,
    'senha': senha,
    'type': type
  }

  usuarios.append(usuario)

  update_json(usuarios)

  return usuario