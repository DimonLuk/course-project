from django.db.models import F
from django.contrib import admin
from .models import Warranty, MotherBoard, Computer, Trunk


class WarrantyDurationFilter(admin.SimpleListFilter):
    title = 'Warranty duration'
    parameter_name = 'Warranty duration'

    def lookups(self, request, queryset):
        data = Warranty.objects.all()
        days = []
        for i in data:
            tmp = i.duration
            days.append((tmp, tmp))
        return days

    def queryset(self, request, queryset):
        test = self.value()
        if test:
            result = list(filter(lambda x: x.duration == test, queryset))
            queryset = Warranty.objects.filter(pk__in=[x.pk for x in result])
        return queryset


class MotherBoardFilter(admin.SimpleListFilter):
    title = 'mother board'
    parameter_name = 'mother board'

    def lookups(self, request, queryset):
        data = MotherBoard.objects.all()
        result = []
        for i in data:
            tmp = '{}, {}, {}'.format(i.manufacturer, i.form_factor, i.socket)
            result.append((tmp, tmp))
        return result

    def queryset(self, request, queryset):
        test = self.value()
        if test:
            test = test.split(', ')
            queryset = queryset.filter(
                mother_board__manufacturer=test[0],
                mother_board__form_factor=test[1],
                mother_board__socket=test[2])
        return queryset


class TrunkFilter(admin.SimpleListFilter):
    title = 'trunk'
    parameter_name = 'trunk'

    def lookups(self, request, queryset):
        data = Trunk.objects.all()
        result = []
        for i in data:
            tmp = '{}, {}, {}'.format(i.manufacturer, i.form_factor,
                                      i.trunk_type)
            result.append((tmp, tmp))
        return result

    def queryset(self, request, queryset):
        test = self.value()
        if test:
            test = test.split(', ')
            queryset = queryset.filter(
                trunk__manufacturer=test[0],
                trunk__form_factor=test[1],
                trunk__trunk_type=test[2])
        return queryset
