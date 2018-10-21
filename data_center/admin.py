from django.contrib import admin
from .filters import WarrantyDurationFilter, MotherBoardFilter, TrunkFilter
from .models import Trunk, Warranty, MotherBoard, Computer


class TrunkAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'warranty', 'form_factor', 'state',
                    'trunk_type', 'width', 'height', 'length')
    list_filter = ('manufacturer', 'state', 'warranty',
                   'form_factor', 'trunk_type')


class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'get_duration')
    list_filter = ('start_date', 'end_date', WarrantyDurationFilter)


class MotherBoardAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'warranty', 'form_factor', 'state',
                    'used_pci_slots', 'installed_ram_capacity')
    list_filter = ('manufacturer', 'warranty', 'form_factor', 'state',
                   'used_pci_slots', 'installed_ram_capacity')


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'mother_board', 'trunk')
    list_filter = ('id', MotherBoardFilter, TrunkFilter)


admin.site.register(Trunk, TrunkAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(MotherBoard, MotherBoardAdmin)
admin.site.register(Computer, ComputerAdmin)
