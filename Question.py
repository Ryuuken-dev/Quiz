

class Question:
    def __init__(self):
        self.collection = []

    def new_qet(self, question: str, _correct_answer_number: int, answers: tuple):
        one, two, three = answers
        question = f'{question};{_correct_answer_number};{one};{two};{three}'
        self.collection.append(question)

    def add_to_file(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for data in self.collection:
                    file.write(f'{data}\n')
        except FileNotFoundError:
            print(f'Plik {filename} nie istnieje!')


