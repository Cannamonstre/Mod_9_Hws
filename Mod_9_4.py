import random


#  Lambda func chapter

first = 'Мама мыла раму'
second = 'Рамена мало было'

lambda_func = list(map(lambda letter1, letter2: letter1 == letter2, first, second))
print(f'{lambda_func} - is for Lambda func chapter')

#  Closure chapter


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='UTF-8') as file:  # Also creates a file if it doesn't exist
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything


write = get_advanced_writer('Mod_9_4_example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# __call__ method


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
