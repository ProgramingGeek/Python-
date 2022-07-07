import random,time,sys,os

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
progress_items = '/storage/emulated/0/progress/items.json'
progress_level = '/storage/emulated/0/progress/level.json'
progress_exp = '/storage/emulated/0/progress/exp.json'


def wait():
    time.sleep(0.7)
  

def experience():
    global exp
    experienceup = random.randint(100,300)
    exp += experienceup
    levelup()
    
    
def levelup():
    """Level Up"""
    global exp,required,level
    if exp >= required:
        required += 300
        level += 1


def checkhp():
    """Check The Health"""
    global playerhp,enemieshp
    if playerhp <= 0:
        playerhp = 0
    if enemieshp <= 0:
        enemieshp = 0


def enemies():
    """enemies attack"""
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
    """player attack"""
    global enemieshp,playerhp
    emhp = random.randint(1,20)
    if playerhp > 0:
        print('Attack!\n')
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
  """normal chest"""
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
  """rare chest"""
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
  

def createprog():
    global progress_items,progress_level,progress_exp
    if os.path.exists(progress_items):
        print()
    else:
        with open(progress_items,'w') as f:
            f.write("")
    if os.path.exists(progress_level):
        print()
    else:
        with open(progress_level,'w') as ff:
            ff.write("")
    if os.path.exists(progress_exp):
        print()
    else:
        with open(progress_exp,'w') as fff:
        fff.write("")
    
    
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
    

def load():
    global progress_items,progress_level,progress_exp,exp,level
    createprog()
    with open(progress_items) as f:
        for line in f:
            k,v = f.strip()
            inventory[k] = v
    with open(progress_level) as ff:
        for lvl in ff:
            lvl = int(lvl)
            level += lvl
    with open(progress_exp) as fff:
        for expp in fff:
            expp = int(expp)
            exp += expp
        
    
def save():
    global exp,level,progress_items,progress_exp,progress_level
    if inventory > 0:
        with open(progress_items) as f:
            for k,v in inventory.items():
                i = f'{k},{int(v)}\n'
                f.write(i)
        with open(progress_exp) as ff:
            ff.write(exp)
        with open(progress_level) as fff:
            fff.write(level)
    
    
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
    elif response == "quit" or response == "q":
        sys.exit()
        
start()