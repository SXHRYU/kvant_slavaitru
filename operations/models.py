from django.db import models
from django.forms import ValidationError
from django.utils import timezone

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Max, Min


class Operation(models.Model):
    priority = models.SmallIntegerField(
        blank=False,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
            ],
    )
    status = models.CharField(
        default="created",
        max_length=100,
        choices=[
            ("created", "создан"),
            ("launched", "запущен"),
            ("stopped", "остановлен"),
        ]
    )
    date_created = models.DateTimeField(
        default=timezone.now(),
        blank=True,
        null=True,
    )
    executor_list = models.ManyToManyField(
        "Executor",
        blank=True,
    )

    def __str__(self) -> str:
        return f"id: {self.id}"

    def _status_translate(status_: str) -> str:
        if not status_:
            return "created"
        elif status_.lower() == "создан":
            return "created"
        elif status_.lower() == "запущен":
            return "launched"
        elif status_.lower() == "остановлен":
            return "stopped"
        else:
            return status_

    @classmethod
    def create(cls) -> None:
        validated = False
        while not validated:
            priority_ = int(input("\nВведите приоритет операции (0-100):\n"))

            status_ = input('\nВведите статус операции (создан/запущен/остановлен)\n'\
                'или оставьте поле пустым (по умолчанию будет вариант "создан"):\n')
            translated_status = cls._status_translate(status_)

            date_created_ = input('\nВведите дату создания операции в формате "гггг-мм-дд чч:минмин[:сс]"\n'\
                'или оставьте поле пустым (по умолчанию будет текущее время):\n')
            if not date_created_:
                date_created_ = timezone.now()

            executor_list_ = list(map(int, input('\nВведите номера исполнителей через пробел '\
                'или оставьте поле пустым:\n').split()))

            operation = cls(
                priority=priority_,
                status=translated_status,
                date_created=date_created_,
            )
            try:
                operation.full_clean()
            except ValidationError as e:
                print(e)
                continue
            else:
                validated = True
        print("Операция создана успешно.")
        operation.save()
        operation.executor_list.add(*executor_list_)

    @classmethod
    def destroy(cls) -> None:
        validated = False
        repeat = False
        while not validated and not repeat:
            try:
                id_ = input("Введите ID операции, которую надо удалить, "\
                    "или нажмите [n/N], чтобы отменить удаление:\n")
                if id_.lower() != "n":
                    id_ = int(id_)
                    cls.objects.get(id=id_).delete()
                    print(f"Удалили операцию c ID={id_}.")
                else:
                    print("Удаление отменено.")
            except cls.DoesNotExist:
                print("\nТакого ID не существует. Попробуйте ещё раз.\n")
            else:
                validated = True

    @classmethod
    def choose(cls) -> int:
        created_or_stopped = cls.objects.exclude(
            status = "launched"
        )
        max_priority = created_or_stopped.aggregate(
            Max("priority"))["priority__max"]
        max_priority_operations = created_or_stopped.filter(
            priority=max_priority
        )

        min_date = max_priority_operations.aggregate(
            Min("date_created"))["date_created__min"]

        final_query_result = created_or_stopped.filter(
            priority=max_priority
        ).filter(
            date_created=min_date
        )

        return final_query_result

class Executor(models.Model):
    def __str__(self) -> str:
        return f"Executor {self.id}"
