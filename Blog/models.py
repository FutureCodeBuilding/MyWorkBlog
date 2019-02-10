from django.db import models

# Create your models here.
class Processor(models.Model):
	# модель обработок и отчётов
    class Meta():
	    verbose_name = "Обработка"
	    verbose_name_plural = "Обработки"
	
    name = models.CharField("Наименование", max_length=100)
    description = models.CharField("Описание", max_length=2000)
    create = models.DateTimeField("Создан", auto_now_add=True)
    tested = models.BooleanField("Протестировано")
    binary = models.BinaryField("БинарныеДанные", upload_to="Processors/")

    def __str__(self):
        return self.name

class Configuration(models.Model):
    # модель конфигураций
    class Meta():
        verbose_name = "Конфигурация"
        verbose_name_plural = "Конфигурации"

    shortname = models.CharField("Краткое наименование", max_length=10)
    fullname = models.CharField("Полное наименование", max_length=100)
    processors = models.ManyToManyField(Processor)
