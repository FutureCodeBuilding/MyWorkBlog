from django.db import models

# Create your models here.
class Processor(models.Model):
	# модель обработок и отчётов
    class Meta():
	    verbose_name = ""
	    verbose_name_plural = ""
	
    name = models.CharField("Наименование", max_length=100)
    description = models.CharField("Описание", max_length=2000)
    create = models.DateTimeField("Создан", auto_now_add=True)
    tested = models.BooleanField("Протестировано")
    binary = models.BinaryField("БинарныеДанные", upload_to="Processors/")

    def __str__(self):
        return self.name
