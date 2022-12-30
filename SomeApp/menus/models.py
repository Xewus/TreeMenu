from django.db.models import (PROTECT, CharField, ForeignKey, Model,
                              PositiveSmallIntegerField, Q)


class MenuItem(Model):
    name = CharField(
        verbose_name='Название',
        max_length=32,
        null=False,
        blank=False,
        db_index=True
    )
    level = PositiveSmallIntegerField(
        verbose_name='Уровень вложенности',
        null=False,
        blank=True,
        default=0
    )
    parent = ForeignKey(
        to='self',
        verbose_name='Родительское меню',
        related_name='submenu',
        on_delete=PROTECT,
        null=True,
        blank=True
    )
    url = CharField(
        verbose_name='Уникальная ссылка на меню',
        max_length=256,
        unique=True,
        null=False,
        blank=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return self.name

    def save(self, *a, **kw) -> None:
        if not self.parent:
            self.level = 0
            self.url = '/' + self.name
        else:
            self.level = self.parent.level + 1
            self.url = f'{self.parent.url}/{self.name}'

        return super().save(*a, **kw)

    @classmethod
    def get_start_menu(cls: 'MenuItem', name: str = '') -> list['MenuItem']:
        menu = MenuItem.objects.filter(level=0)

        if name:
            menu = menu.filter(name=name)

        return menu

    @classmethod
    def get_with_parents(cls: 'MenuItem', url: str) -> list['MenuItem']:
        db_urls = url.strip('/').split('/')

        if not db_urls:
            return []

        db_urls[0] = '/' + db_urls[0]

        for i in range(1, len(db_urls)):
            db_urls[i] = f'{db_urls[i - 1]}/{db_urls[i]}'

        return MenuItem.objects.filter(
            Q(parent__url__in=(db_urls)) | Q(url=db_urls[0])
        ).order_by('level')
