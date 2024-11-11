from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'apps'

    def ready(self):
        from core import signals
