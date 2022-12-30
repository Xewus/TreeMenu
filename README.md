# TreeMenu (TestTask)
Приложение для встраивания древовидного меню в ваш прoект.


Показывает все вышестояшие, соседние и один уровень нижестоящих пунктов относительно выбраного пункта.

Для вывода желаемого пункта меню на произвольной странице, необходимо в контексте передать переменную "catalog", содержащую уникальную ссылку желаемого пункта. Без этого действия будут выведены пункты меню первого уровня.

Передача имени пункта меню без установления ограничения на его уникальность не желательна, так как одинаковые имена могут быть у разных категорий, например, "колёса" есть у машин, тележек, в аптеках и т.д.


Для примера в репозитории имеется небольшая БД и пустое приложение.

Данное решение в 1 SQL-запрос не самое лучшее для миллонов записей в БД (если вообще имеет смысл в таком случае использование подобного решения). Для больших БД лучше использовать дополнительную таблицу с храненнием списка родительских пунктов.

***
## Задание
Нужно сделать `Djang-арр`, который будет реализовывать древовидное меню, соблюдая
следующие условия:

1) Меню реализовано через template_tag;

2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под
выделенным пунктом тоже развернут;

3) Хранится в БД;

4) Редактируется в стандартной админке Django;

5) Активный пункт меню определяется исходя из URL текущей страницы;

6) Меню на одной странице может быть несколько, они определяются по названию;

7) При клике на меню происходит переход по заданному в нем URL. Он может быть задан как
явным образом, так и через named URL:

8) На отрисовку каждого меню требуется ровно 1 запрос к БД.

Нужен `Django-app`, который позволяет вносить в БД меню (одно или несколько) через
админку, и нарисовать на любой нужной странице меню по названию.

{% draw_menu ‘name_menu' %}

При выполнении задания из библиотек следует использовать только `Django` и стандартную
библиотеку `Python`.
***
Пример главной страницы со списком меню:
![index page](https://github.com/Xewus/TreeMenu/blob/main/index.png)
***
Подтверждение получения данных в 1 запрос к БД:
![sql example](https://github.com/Xewus/TreeMenu/blob/main/sql.png)
***
Пример админки:
![admin page](https://github.com/Xewus/TreeMenu/blob/main/admin.png)
***
### Инструкция по встраиванию

Скачать код:
```
git@github.com:Xewus/DimaTechLTD.git
```
Скопировать папку `*/Menu/menus` с приложением в ваш проект на одном уровне с остальными приложениями
и вписать приложение в `INSTALLED_APPS`:
```
INSTALLED_APPS = [
    ...
    'menus',
    ...
]
```
Настроить директории шаблонов:
```
TEMPLATES_DIR = BASE_DIR / 'templates'
TEMPLATES_MENU = BASE_DIR / 'menus/templates'
TEMPLATES = [
    {
        ...
        'DIRS': [TEMPLATES_DIR, TEMPLATES_MENU],
...
```
Добавить `url-роутер` приложения в начало главного `url-роутера`:
```
urlpatterns = [
    path('menu/', include('menus.urls', namespace='menus')),
    path('admin/', admin.site.urls),
    ...
    path('', include('example_app.urls', namespace='example_app'))
    ...
]
```
Применить миграции:
```
python manage.py migrate
```
Вписать в нужных местах  HTMLстраницы загрузку и использование тэга:
```
...
{% load menu_tags %}
...
{% draw_menu catalog %}
...
```

