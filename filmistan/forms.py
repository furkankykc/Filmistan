from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class kayıtformu(UserCreationForm):
   class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email')

    def clean_email(self):

        if not self.cleaned_data['email']:
            raise forms.ValidationError(u'E-posta adresi girin.')
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(
                u'''
                Bu e-posta başka bir kullanıcı tarafından kullanılıyor.
                Başka bir e-posta kullanmayı deneyin.
                ''')
        return self.cleaned_data['email']
