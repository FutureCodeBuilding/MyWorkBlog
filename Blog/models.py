from django.db import models
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

class Service:
    def safe_get(self, **kwargs):
        try:
            rez = self.objects.get(kwargs)
        except ObjectDoesNotExist:
            rez = None
        return rez

    def __new__(cls, *args, **kwargs):
        if cls is Service:
            return None

class Processor(models.Model, Service):
	# модель обработок и отчётов
    class Meta():
        verbose_name = "Обработка"
        verbose_name_plural = "Обработки"
	
    name = models.CharField("Наименование", max_length=100)
    description = models.CharField("Описание", max_length=2000)
    create = models.DateTimeField("Создан", auto_now_add=True)
    tested = models.BooleanField("Протестировано")
    binary = models.BinaryField("БинарныеДанные", upload_to="Processors/")
    author = models.ForeignKey("User", on_delete=models.SET_DEFAULT, default='getDefaultAuthor')

    def __str__(self):
        return self.name

class Configuration(models.Model, Service):
    # модель конфигураций
    class Meta():
        verbose_name = "Конфигурация"
        verbose_name_plural = "Конфигурации"

    shortname = models.CharField("Краткое наименование", max_length=10)
    fullname = models.CharField("Полное наименование", max_length=100)
    processors = models.ManyToManyField(Processor)

class User(models.Model, Service):
    #
    class Meta():
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    name = models.CharField("Наименование", max_length=100)
    accesslevel = models.IntegerField("Уровень доступа")

class Comment(models.Model, Service):
    class Meta():
        verbose_name = ""
        verbose_name_plural = ""

    parentid = models.ForeignKey("self", on_delete=models.CASCADE, blank=True)
    author = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    text = models.TextField("Текст")
    create = models.DateTimeField("Создан", auto_now_add=True)


# noinspection SyntaxError,SyntaxError
def getDefaultAuthor():
    defname = "<Пользователь по-умолчанию>"
    user = User.safe_get(name=defname)
    # noinspection SyntaxError
    if user == None:
        user = User()
        user.name = defname
        user.accesslevel = 9
        user.save()
    return user
