from django.core.management import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Updater



class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        pass