from django.contrib import admin

from django_rocket.models import Subscriber, InvitationToken


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    date_hierarchy = 'created'


class InvitationTokenAdmin(admin.ModelAdmin):
    list_display = ('created', 'token', 'uses')


admin.site.register(InvitationToken, InvitationTokenAdmin)
admin.site.register(Subscriber, SubscriberAdmin)