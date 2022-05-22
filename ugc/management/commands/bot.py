from django.core.management.base import BaseCommand
from django.conf import settings
from ugc.models import Profile, Message
from telebot import *
import re

def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:

            error_message = f'Error start: {e}'
            print(error_message)
            raise e

    return inner

class Command(BaseCommand):
    help = 'Telegramm-bot'

    def handle(self, *args, **options):

        bot = TeleBot("5062500880:AAEVn2a03dwDJHfs3JupsO9udmn8CtBmld8")

        @log_errors
        @bot.message_handler(commands=['start'])
        def start(message):
            bot.send_message(message.chat.id, 'Welcome')

        @log_errors
        @bot.message_handler(commands=['count'])
        def do_count(message):
            p, _ = Profile.objects.get_or_create(external_id=message.from_user.id,defaults={'name': message.from_user.username,
                                                                                       'id': message.from_user.id,
                                                                                       'group': message.chat.id,
                                                                                       })
            atribut = Profile.objects.get()
            print(atribut)
            count = Message.objects.filter(profile=p).count()

            # b = f'{re.findall(r"#[-*[0-9]*]*#", a)}'

            bot.send_message(chat_id=message.chat.id,text=f"you use {count} messages",)

        @log_errors
        @bot.message_handler(content_types=['text'])
        def do_echo(message):

            p, _ = Profile.objects.get_or_create(external_id=message.from_user.id,defaults={'name':message.from_user.username,'username':message.from_user,
                                                                                       'group': message.chat.id,})

            m = Message(profile=p,text=message.text)
            m.save()


        bot.polling()
