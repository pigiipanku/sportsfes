from django.apps import AppConfig

import os

# Fetch the service account key JSON file contents
class SportsfesConfig(AppConfig):
    name = 'sportsfes'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    APP_DIR = os.path.join(BASE_DIR, name)

    def ready(self):

        pass