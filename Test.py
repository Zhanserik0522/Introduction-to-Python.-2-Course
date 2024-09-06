import telebot as tb
import webbrowser

bot = tb.TeleBot('6940779272:AAHDpHmZVpYJ7FJgDY7ebF4Hw-nfqFgmRrg')
markup = tb.types.InlineKeyboardMarkup()
markup.add(tb.types.InlineKeyboardButton('Go to the website', url='platonus.iitu.edu.kz'))
markup.add(tb.types.InlineKeyboardButton('Delete the photo', callback_data='delete'))
markup.add(tb.types.InlineKeyboardButton('Edit the text', callback_data='edit'))

@bot.message_handler(commands=['start'])
def main(message):
    if message.from_user.last_name is not None and  message.from_user.first_name is not None:
        bot.send_message(message.from_user.id, 'Hello {message.from_user.last_name} {message.from_user.first_name}',markup)
    elif message.from_user.last_name is None:
        bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}",reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Your first name or last name is missing",reply_markup=markup)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Help information",reply_markup=markup)


@bot.message_handler(commands=['date'])
def main(message):
    bot.send_message(message.chat.id, "20.06.2024 - the Date that I ve started learning to write ChatBots with telebot")


@bot.message_handler(commands=['site'])
def site(message):
    try:
        webbrowser.open('platonus.iitu.edu.kz')
    except Exception as e:
        bot.send_message(message.chat.id, f"Error opening website: {e}")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message,'Какое красивое фото')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback == 'edit':
        bot.edit_message_text(callback.message.chat.id, callback.message.message_id)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, f'Hello {message.from_user.last_name} {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message,f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
