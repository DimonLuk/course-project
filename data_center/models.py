from django.db import models
from .constants import FORM_FACTORS, TRUNK_TYPES, SOCKETS, COMPONENT_STATE


class Warranty(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def get_duration(self):
        return str(self.end_date - self.start_date).split(',')[0]
    get_duration.short_description = 'Duration left'

    @property
    def duration(self):
        return str(self.end_date - self.start_date).split(',')[0]

    def __str__(self):
        return 'From: {} to: {}'.format(self.start_date, self.end_date)


class AbstractComponent(models.Model):
    manufacturer = models.CharField(max_length=30)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=10)
    state = models.CharField(max_length=7, choices=COMPONENT_STATE,
                             default='working')

    class Meta:
        abstract = True


class Trunk(AbstractComponent):
    form_factor = models.CharField(max_length=4, choices=FORM_FACTORS)
    trunk_type = models.CharField(max_length=10, choices=TRUNK_TYPES)
    height = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()

    def __str__(self):
        return 'Trunk: {}, {}, {}'.format(self.manufacturer,
                                          self.form_factor, self.trunk_type)


class MotherBoard(AbstractComponent):
    form_factor = models.CharField(max_length=4, choices=FORM_FACTORS)
    socket = models.CharField(max_length=7, choices=SOCKETS)
    max_pci_slots = models.IntegerField()
    used_pci_slots = models.IntegerField()
    installed_ram_capacity = models.IntegerField()
    max_ram_capacity = models.IntegerField()

    def __str__(self):
        return 'Mother board: {}, {}, {}'.format(self.manufacturer,
                                                 self.form_factor, self.socket)


class Computer(models.Model):
    trunk = models.OneToOneField(Trunk, on_delete=models.CASCADE)
    mother_board = models.OneToOneField(MotherBoard, on_delete=models.CASCADE)

    def __str__(self):
        return 'ID {}'.format(self.pk)
