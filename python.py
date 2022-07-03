import random

Loot = False
level = 0
exp = 250
required = 250
playerhp = 100
enemieshp = 100
inventory = {}
loots = ['Normal Chest','Rare Chest']
treasure = random.choice(loots)

def level():
  """Level Up"""
  global exp,required,level
  if exp >= required:
    required += 300
    level += 1


def enemies():
  """enemies"""
  print('Attack')
  plhp = random.randint(1,20)
  if plhp <= 14:
    playerhp -= plhp
  elif plhp >= 15:
    playerhp -= plhp
    print('Critical Hit!')
      
      
def player():
  print('Attack')
  emhp = range(1,20)
  if emhp <= 14:
    enemieshp -= emhp
  elif emhp >= 15:
    enemieshp -= emhp
    print('Critical Hit!')
      

def normal():
  if 'Coin' not in inventory:
    inventory['Coin'] = 5
  else:
    inventory['Coin'] += 5
  if 'Dagger' not in inventory:
    inventory['Dagger'] = 1
  else:
    inventory['Dagger'] += 1
  if 'Healing Potion' not in inventory:
    inventory['Healing Potion'] = 1
  else:
    inventory['Healing Potion'] += 1
  
  
def rare():
  if 'Coin' not in inventory:
    inventory['Coin'] = 26
  else:
    inventory['Coin'] += 26
  if 'Dagger' not in inventory:
    inventory['Dagger'] = 1
  else:
    inventory['Dagger'] += 1
  if 'Healing Potion' not in inventory:
    inventory['Healing Potion'] = 3
  else:
    inventory['Healing Potion'] += 3
  if 'Sword' not in inventory:
    inventory['Sword'] = 1
  else:
    inventory['Sword'] += 1
  
def clnormal():
  if 'Normal Chest' not in inventory:
    inventory['Normal Chest'] = 1
  else:
    inventory['Normal Chest'] += 1
  
  
def clrare():
  if 'Rare Chest' not in inventory:
    inventory['Rare Chest'] = 1
  else:
    inventory['Rare Chest'] += 1


def chest():
  global treasure,loots
  if treasure == loots[0]:
    normal()
  if treasure == loots[1]:
    rare()
    
def close():
  global treasure,loots
  if treasure == loots[0]:
    clnormal()
  if treasure == loots[1]:
    clrare()
  
  
def loot():
  while Loot:
    response = input('Do you want to open/keep the treasure ')
    if response == 'open':
      chest()
    elif response == 'close':
      close()
    else:
      continue