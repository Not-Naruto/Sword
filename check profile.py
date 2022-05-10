import pickle
with open('profile.dat','rb') as f:
    a=pickle.load(f)

print(a)

print('''\nPROFILE:\n
Health = {}
Level = {}
Potions = {}
Coins = {}
ATK = {}
DEF = {}\n'''.format(a['health'],a['level'],a['pot'],a['coins'],a['atk'], a['def']))

