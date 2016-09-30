def get_answer(frase, prepared_frases):
return prepared_frases[frase]
answers = {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'пока': 'увидимся'}
print(get_answer('привет', answers))