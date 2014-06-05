from django.contrib import admin

from django_rocket.models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    date_hierarchy = ('created',)


admin.site.register(Subscriber, SubscriberAdmin)