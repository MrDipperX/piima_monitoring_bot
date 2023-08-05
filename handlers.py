from loader import bot

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, f"<b>Assalomu alaykum, {message.from_user.first_name}.</b>\nID raqamingizni "
                                           f"kiriting", parse_mode='html')


@bot.message_handler(content_types=['text'])
def mess(message):
    # if message.from_user.id == 963500369 or message.from_user.id == 532937483:
        try:
            photo_name = message.text.replace("_", "")
            if message.text is not None:
                bot.send_photo(message.from_user.id, open(f"photos/{photo_name}_.jpg", 'rb'))

        except FileNotFoundError:
            bot.send_message(message.from_user.id, "Bunday ID raqam yo'q, qaytatdan yozing!")

        except:
            bot.send_message(message.from_user.id, "Qayta urinib ko'ring!")