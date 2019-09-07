from django.contrib import admin

from django_rocket.models import InvitationToken, Subscriber


@admin.register(InvitationToken)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    date_hierarchy = 'created'


@admin.register(Subscriber)
class InvitationTokenAdmin(admin.ModelAdmin):
    list_display = ('created', 'token', 'uses')
