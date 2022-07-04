import random,time

game = False
Loot = False
level = 0
exp = 250
required = 250
playerhp = 100
enemieshp = 100
inventory = {}
loots = ['Normal Chest','Rare Chest']
treasure = random.choice(loots)


def wait():
  time.sleep(0.7)
  

def level():
  """Level Up"""
  global exp,required,level
  if exp >= required:
    required += 300
    level += 1


def checkhp():
  global playerhp,enemieshp
  if playerhp <= 0:
    playerhp = 0
  if enemieshp <= 0:
    enemieshp = 0


def enemies():
  """enemies"""
  global playerhp,enemieshp
  if enemieshp > 0:
    print('Attack!\n')
    plhp = random.randint(1,20)
    if plhp <= 14:
      playerhp -= plhp
      checkhp()
    elif plhp >= 15:
      playerhp -= plhp
      print('Critical Hit!')
      checkhp()
      
    print(f'Damage: {plhp}')
    print(f'PlayerHp: {playerhp}')
  
  
def player():
  global enemieshp,playerhp
  if playerhp > 0:
    print('Attack!\n')
    emhp = random.randint(1,20)
    if emhp <= 14:
      enemieshp -= emhp
      checkhp()
    elif emhp >= 15:
      enemieshp -= emhp
      print('Critical Hit!')
      checkhp()
    
    print(f'Damage: {emhp}')
    print(f'EnemiesHp: {enemieshp}')
      

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
  

def reset():
  global playerhp,enemieshp
  if playerhp <= 0 and playerhp >= 0:
    playerhp = 100
  if enemieshp <= 0 and enemieshp >= 0:
    enemieshp = 100
  
  
def loot():
  global Loot
  reset()
  Loot = True
  while Loot:
    response = input('Do you want to open/keep the treasure ').lower()
    if response == 'open':
      chest()
      Loot = False
    elif response == 'close':
      close()
      Loot = False
    

def start():
  while game:
    global enemieshp,playerhp
    response = input('Welcome to text game (Fight/f) (quit/q)').lower()
    if response == "fight" or response == "f":
      while enemieshp > 0 and playerhp > 0:
        fight = input('Attack/a').lower()
        if fight == "attack" or fight == 'a':
            player()
            wait()
            enemies()
      if enemieshp <= 0:
        loot()
      if enemieshp <= 0:
        print('You Win')
      if playerhp <= 0:
        print('You Lose')
        reset()
        
start()