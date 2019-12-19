from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import TableShape


class Table(models.Model):

    number = models.PositiveIntegerField(_('number'), unique=True)
    seats = models.PositiveIntegerField(_('seats number'))
    shape = models.CharField(
        _('shape'),
        max_length=20,
        choices=TableShape.choices
    )
    position_x = models.PositiveIntegerField(
        _('table position in the room X - % related to the room length'),
        validators=[MaxValueValidator(100)]
    )
    position_y = models.PositiveIntegerField(
        _('table position in the room Y - % related to the room width'),
        validators=[MaxValueValidator(100)]
    )
    length = models.PositiveIntegerField(
        _('table length in % related to the room length'),
        validators=[MaxValueValidator(100)]
    )
    width = models.PositiveIntegerField(
        _('table width in % related to the room width'),
        validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return 'Table #{}'.format(self.number)


class Order(models.Model):

    date = models.DateField(_('date'))
    table = models.ForeignKey(
        Table,
        verbose_name=_('table'),
        related_name='orders',
        on_delete=models.CASCADE
    )
    email = models.EmailField(_('email'))

    def __str__(self):
        return 'Table #{} order on {}'.format(self.table.number, self.date)
