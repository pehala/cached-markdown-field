from django.forms import ModelForm

from test_app.models import VerboseNameAndHelpDescription


class DescriptionForm(ModelForm):
    class Meta:
        model = VerboseNameAndHelpDescription
        fields = "__all__"
