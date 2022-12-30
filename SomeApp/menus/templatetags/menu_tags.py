from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

from ..models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_url: str = ''):
    if not menu_url:
        menus = MenuItem.get_start_menu()
    else:
        menus = MenuItem.get_with_parents(menu_url)

    if not menus:
        return 'There is nothing...'

    html_string = '<ul>\n'
    end_html_string = '</ul>\n'
    menu_line = '<li>\n<a href="%s">%s</a>\n</li>\n'
    level = 0
    defered = None

    view_url = reverse('menus:main_menu').rstrip('/')

    for menu in menus:
        if menu.level > level:
            if defered:
                html_string += defered
                defered = None

            level = menu.level
            html_string += '<ul>\n'
            end_html_string += '</ul>\n'

        if menu_url == menu.url[1:]:
            defered = menu_line % (
                view_url + menu.url, f'<h5>{menu.name}</h5>'
            )
            continue

        html_string += menu_line % (view_url + menu.url, menu.name)
    else:
        if defered:
            html_string += defered

    return mark_safe(html_string + end_html_string)
