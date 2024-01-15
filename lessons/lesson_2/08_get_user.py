# Отлично работает. Но если капнуть глубже, есть нюанс.
# Получение объекта или None
# Если мы запустим прошлый пример с несуществующим в БД
# идентификатором, получим ошибку: myapp2.models.User.DoesNotExist: User
# matching query does not exist.
# Исправим наш код:
from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
# Во-первых обратите внимание на замену id на pk. Так команда Django ушла от
# конфликта между именем переменной и встроенной в Python функцией id().
# pk - primary key, первичный ключ в таблице, т.е. ID.
# Также для получения пользователя заменили метод get на filter, а далее к
# результату применяем метод first().
# ● Если в базе несколько записей, вернёт одна, первая из результата
# запроса
# ● Если запись одна, first вернёт эту единственную запись
# ● Если совпадений не найдено, вместо ошибки вернём None
# Рассмотрим работу с filter подробнее
