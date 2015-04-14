from django import forms

from .models import Subscriber, InvitationToken


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        data = self.cleaned_data['email']

        if Subscriber.objects.filter(email=data).exists():
            raise forms.ValidationError('We already have this email in our waiting list')

        return data


class InvitationTokenCheckForm(forms.Form):
    code = forms.CharField(max_length=40, required=True)

    def clean_code(self):
        data = self.cleaned_data['code']

        if not InvitationToken.objects.filter(code=data, uses__gte=1).exists():
            raise forms.ValidationError('Unknown token')

        return data

    def use_token(self):
        token = InvitationToken.objects.get(code=self.cleaned_data['code'])
        token.uses -= 1
        token.save(update_fields=('uses',))
        return token


class ConfirmRedeemInvitation(forms.Form):
    confirmation = forms.BooleanField(initial=False,
                                      required=True,
                                      label='Are you sure you want to redeem this code')
