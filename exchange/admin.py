from django.contrib import admin
from .models import Exchange, ExchangeItem, Settlement

@admin.register(ExchangeItem)
class ExchangeItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'description')
    search_fields = ('name',)
    list_filter = ('unit',)


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('giver', 'receiver', 'item', 'quantity', 'value_estimate', 'timestamp')
    list_filter = ('giver', 'receiver', 'item')
    search_fields = ('giver__username', 'receiver__username', 'item__name')
    date_hierarchy = 'timestamp'



@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'amount_due', 'is_settled', 'settled_on')
    list_filter = ('user1', 'user2')
    search_fields = ('user1__username', 'user2__username')

    def is_settled(self, obj):
        return obj.settled_on is not None
    is_settled.boolean = True
    is_settled.short_description = "Settled?"
