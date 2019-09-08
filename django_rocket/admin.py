from django.contrib import admin

from django_rocket.models import InvitationToken, Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('created', 'email')
    date_hierarchy = 'created'


@admin.register(InvitationToken)
class InvitationTokenAdmin(admin.ModelAdmin):
    list_display = ('created', 'code', 'uses')
