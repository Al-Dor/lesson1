from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import answers
from answers import get_answer

def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)

    # get_answer = update.message.text
#    ans = answers.get(update.message.text)
#    if ans is None:
#       ans = "Моя твоя не понимать"
    ans = get_answer(update.message.text, answers)
    bot.sendMessage(update.message.chat_id, ans)

def count_my_words(bot, update):
    print('Запущен подсчет слов во фразе: %s' % update.message.text)
    count = 'В ней %s слов' % str(len(update.message.text.split()) - 1)
    bot.sendMessage(update.message.chat_id, text=count)


def main():
    updater = Updater("271776113:AAGOg75upLIMLKtwVTKFMhjINg-tnp2meoE")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler('count_my_words', count_my_words))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()