from django.db import models


class Todo(models.Model):
    title = models.CharField(
        verbose_name='Название задачи',
        max_length=255
    )
    is_complete = models.BooleanField(
        verbose_name='Завершено',
        default=False
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        db_table = 'todos'
