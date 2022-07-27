from django.core.management.base import BaseCommand
from operations.models import Executor

def mock_executor_data() -> None:
    for _ in range(10):
        executor = Executor()
        executor.save()

class Command(BaseCommand):
    help = 'Создаёт и записывает в базу 10 исполнителей.'

    def handle(self, *args, **options):
        mock_executor_data()
