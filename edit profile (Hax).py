import pickle

with open('profile.dat','wb') as f:
    x={'health':100,'maxh':100, 'level':5, 'pot':0,'coins':1000, 'atk':70, 'def':50}
    pickle.dump(x,f)
