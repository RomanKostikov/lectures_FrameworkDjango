# А чтобы получить пользователя по его ID, мы можем использовать следующий
# код в файле myapp2/management/commands/get_user.py:
from django.core.management.base import BaseCommand
from myapp_2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        user = User.objects.get(id=id)
        self.stdout.write(f'{user}')
# Метод add_arguments позволяет парсить командную строку. Мы получаем
# значение целого типа и сохраняем его по ключу id. Теперь обработчик handler
# может получить к идентификатору доступ через ключ словаря kwargs.
# Запустим команду
# python manage.py get_user 2
# В результате в консоли увидим информацию о нашем пользователе
# Username: John, email: john@example.com, age: 25
# Отлично работает. Но если капнуть глубже, есть нюанс.
