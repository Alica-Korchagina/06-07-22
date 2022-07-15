def start(m):
    bot.send_message(m.chat.id, "Я на связи. Смогу рассмешить любого своими анекдотами!\nНапиши:\n/help - я помагаю. \nанекдот - высылаю анекдот")

def help(m):
    bot.send_message(m.chat.id, "Напиши: \nанекдот - высылаю анекдот \n")
