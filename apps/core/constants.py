from django.utils.translation import ugettext_lazy as _

from djchoices import DjangoChoices, ChoiceItem


class TableShape(DjangoChoices):
    rectangle = ChoiceItem('rectangle', _('Rectangle'))
    oval = ChoiceItem('oval', _('Oval'))
