import pickle

class A:
    pass

class Human(A):
    pass


game_field = [
            [Human(), Human(), 0, 0],
            [Human(), Human(), 0, 0],
            [Human(), Human(), 0, 0],
            [Human(), Human(), 0, 0]]
human = Human()
test_list = {'score': 10, 'game_field': None, 'max_score': 1000}
with open('score', 'wb') as s_file:
    pickle.dump(game_field, s_file)

with open('score', 'rb') as s_file:
    text = pickle.load(s_file)
    print(text)
