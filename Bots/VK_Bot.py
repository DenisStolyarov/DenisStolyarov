import vk_api,random
from class_vk_bot import VkBot
from vk_api.longpoll import VkLongPoll,VkEventType

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(1, 2147483647)})

token = "ca0db897c54de7cee72ae0f9fbe1b3dff5ba5b6362ef44fc717fd3f081b0da7584491bec953c0f2c4aa96"

#Авторизируем как сообщество
vk = vk_api.VkApi(token = token)

#Работа с сообщением
longpoll = VkLongPoll(vk)

#Основной цикл
print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)