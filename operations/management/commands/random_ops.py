import random as r
from django.core.management.base import BaseCommand
from operations.models import Operation, Executor


def get_random_date() -> str:
    dd = r.randint(1, 30)
    mm = r.randint(1, 12)
    yyyy = r.randint(1990, 2022)
    hh = r.randint(0, 23)
    mnmn = r.randint(0, 59)
    ss = r.randint(0, 59)
    return f"{str(yyyy)}-{str(mm)}-{str(dd)} {str(hh)}:{str(mnmn)}:{str(ss)}"

class Command(BaseCommand):
    help = 'Создаёт 10 случайных операций со случайными значениями '\
        'приоритета, статуса, времени создания, исполнителей.'
        
    def handle(self, *args, **options):
        executors = Executor.objects.all()
        
        for _ in range(10):
            priority_ = r.randint(0, 100)
            status_ = r.choice(["created",
                              "launched",
                              "stopped"])
            date_created_ = get_random_date()
            executor_list_ = r.choices(executors,
                                      k=r.randint(0, len(executors)-1))
            operation = Operation(
                priority=priority_,
                status=status_,
                date_created=date_created_,
            )
            operation.save()
            operation.executor_list.add(*executor_list_)
