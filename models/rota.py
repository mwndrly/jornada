# utils
import os
import json
import random

# constants
base_dir = os.path.join(os.path.dirname(__file__), '../data')
json_rotas = os.path.join(base_dir, 'rotas.json')

class Cor:
  VERMELHO = '\033[91m'
  AMARELO = '\033[93m'
  VERDE = '\033[92m'
  RESET = '\033[0m'

def ler_json():
  with open(json_rotas, 'r') as f:
    return json.load(f)

def atualizar_json(response):
  with open(json_rotas, 'w') as f:
    json.dump(response, f, indent=2)

def cadastrar_rota(user):
  rotas = ler_json()

  partida = input("DIGITE O PONTO DE PARTIDA:\n>>> ")
  chegada = input("DIGITE O PONTO DE CHEGADA:\n>>> ")

  rotas.append({
    'id': random.randint(1, 1000),
    'partida': partida,
    'chegada': chegada,
    'criada_por': user['id']
  })

  atualizar_json(rotas)
  print(Cor.VERDE + "ROTA CADASTRADA COM SUCESSO!" + Cor.RESET)

def listar_rotas():
  rotas = ler_json()

  if rotas:
    print(">>>>>>> LISTA DE ROTAS <<<<<<<<")

    for rota in rotas:
      print("*" * 50)
      print(f"ID: {rota['id']}, PARTIDA: {rota['partida']}, CHEGADA: {rota['chegada']}, CRIADA POR: {rota['criada_por']}")
      print("*" * 50)
      print("=" * 50)
  else:
    print(Cor.AMARELO + "NENENHUMA ROTA CADASTRADA." + Cor.RESET)

def buscar_rota(id):
  rotas = ler_json()
  id_da_rota = int(id)

  if not rotas:
      print(Cor.AMARELO + "NENHUMA ROTA CADASTRADA." + Cor.RESET)

  for rota in rotas:
    if rota['id'] == id_da_rota:
      print(Cor.VERDE + ">>>>>>> ROTA ENCOTNRADA <<<<<<<<" + Cor.RESET)
      print(f"ID: {rota['id']}, PARTIDA: {rota['partida']}, CHEGADA: {rota['chegada']}, CRIADA POR: {rota['criada_por']}")
    else:
      print(Cor.AMARELO + "NENHUMA ROTA ENCONTRADA." + Cor.RESET)

def editar_rota(id):
  rotas = ler_json()
  id_da_rota = int(id)

  if not rotas:
    print(Cor.AMARELO + "NENHUMA ROTA CADASTRADA." + Cor.RESET)

  for rota in rotas:
    if rota['id'] == id_da_rota:
      rota['partida'] = input("DIGITE O NOVO PONTO DE PARTIDA:\n>>> ")
      rota['chegada'] = input("DIGITE O NOVO PONTO DE CHEGADA:\n>>> ")

      atualizar_json(rotas)
      print(Cor.VERDE + "ROTA ATUALIZADA COM SUCESSO!" + Cor.RESET)
    else:
      print(Cor.AMARELO + "NENHUMA ROTA ENCONTRADA." + Cor.RESET)

def excluir_rota(id):
  rotas = ler_json()
  id_da_rota = int(id)

  if not rotas:
    print(Cor.AMARELO + "NENHUMA ROTA CADASTRADA." + Cor.RESET)

  for rota in rotas:
    if rota['id'] == id_da_rota:
      rotas.remove(rota)

      atualizar_json(rotas)

      print(Cor.VERDE + "ROTA EXCLUÍDA COM SUCESSO!" + Cor.RESET)
    else:
      print(Cor.AMARELO + "NENHUMA ROTA ENCONTRADA." + Cor.RESET)
