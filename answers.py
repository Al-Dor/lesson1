#def get_answer(question_dictionary, question):
#   return question_dictionary[question]

answers = { 'Привет': 'И тебе привет',\
            'Как дела?': 'Лучше всех',\
            'Когда в отпуск': 'Еще нескоро'}


# while True:
#   user_question = input('О чем хочешь спросить? ')
#   if user_question == 'Пока':
#       print('Увидимся')
#       break
#   elif answers.get(user_question) is None:
#       print('Не поняла тебя, уточни')
#   else: 
#       print(answers.get(user_question))

def get_answer(user_question, answers):
    return answers.get(user_question, 'Не поняла тебя, уточни')

if __name__ == '__main__':
    while True:
        user_question = input('О чем хочешь спросить? ')
        answer = get_answer(user_question, answers)
        print(answer)

        if user_question == 'Пока':
            print('Увидимся')
            break





# (вопрос, словарь) -> get_answer -> ответ
