from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'product'
    label = 'product'

    def ready(self):
        from . import signals
