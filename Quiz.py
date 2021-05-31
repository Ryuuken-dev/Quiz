from random import choice


class Quiz:
    def __init__(self):
        self.rnd_qte = []
        self.correct_answers = 0
        self.questions_collection = []

    def get_items(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            items = [item.strip('\n') for item in file if item != '\n']
        self.questions_collection = items

    @property
    def _rand_qte(self):
        question = choice(self.questions_collection)
        return question

    @staticmethod
    def _get_answer():
        users_answer = input('Twoja odpowiedź: ')
        return users_answer

    def _check_answer(self, question: list, users_answer: str):
        correct_answer = int(question[1])
        if users_answer.capitalize() == question[correct_answer] or int(users_answer) == correct_answer:
            self.correct_answers += 1
            print('Poprawna odpowiedź!')
            return False
        else:
            print('Niepoprawna odpowiedź!')
            return True

    @staticmethod
    def _show_question(question: list):
        return f'Pytanie: {question[0]}\n\n1. {question[2]}\n2. {question[3]}\n3. {question[4]}\n'

    def __repr__(self):
        is_done = False
        self.get_items('pytania.csv')
        while not is_done and len(self.questions_collection) != len(self.rnd_qte):
            random_question = self._rand_qte
            if random_question in self.rnd_qte:
                continue
            self.rnd_qte.append(random_question)
            question = random_question.split(';')
            print(self._show_question(question))
            is_done = self._check_answer(question, self._get_answer())

        if len(self.questions_collection) == self.correct_answers:
            return 'Gratulacje! Wygrywasz!'

        return f'Zdobyłeś {self.correct_answers} punktów'
















