def ask_user(user_say):
	return(print)

while True:
	user_say = input('Как дела? ')
	if user_say == 'Хорошо':
		print('Рад за тебя!')
		break
	else:
		print('Жаль, что дела у тебя %s' % user_say)