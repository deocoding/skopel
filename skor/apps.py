from django.apps import AppConfig


class SkorConfig(AppConfig):
    name = 'skor'

    def ready(self):
        import skor.signals
