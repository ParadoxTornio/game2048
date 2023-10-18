import pickle

with open('game.save', 'rb') as s_file:
    text = pickle.load(s_file)
    print(text)
