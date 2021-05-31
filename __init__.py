from Question import Question
from Quiz import Quiz


qte = Question()
qte.new_qet('Stolica Peru', 2, ('Sztokholm', 'Lima', 'Barcelona'))
qte.new_qet('Stolica Hiszpanii', 3, ('Petersburg', 'Kopenhaga', 'Barcelona'))
qte.new_qet('Stolica Białorusi', 3, ('Moskwa', 'Kijów', 'Mińsk'))
qte.new_qet('Stolica Belgii', 2, ('Canberra', 'Bruksela', 'Berno'))
qte.new_qet('Stolica Kanady', 1, ('Ottawa', 'Bruksela', 'Berno'))
qte.new_qet('Stolica Szwecji', 1, ('Sztokholm', 'Berlin', 'Mińsk'))
qte.new_qet('Stolica Finlandii', 3, ('Ottawa', 'Lima', 'Helsinki'))
qte.new_qet('Stolica Francji', 3, ('Ateny', 'Sztokholm', 'Paryż'))
qte.add_to_file('pytania.csv')

run_quiz = Quiz()
print(run_quiz)