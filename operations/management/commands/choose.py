from django.core.management.base import BaseCommand
from operations.models import Operation

class Command(BaseCommand):
    help = 'Исполняет метод `choose()`.'
    
    def handle(self, *args, **options):
        print(Operation.choose())
