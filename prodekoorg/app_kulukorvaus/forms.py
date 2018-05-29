from django.forms import ModelForm, RadioSelect, Textarea

from .models import Kulukorvaus, KulukorvausPerustiedot


class KulukorvausPerustiedotForm(ModelForm):

    def __init__(self, *args, **kwargs):
        exclude = kwargs.pop('exclude', None)
        super(KulukorvausPerustiedotForm, self).__init__(*args, **kwargs)

        if 'position_in_guild' in self.fields:
            self.fields['position_in_guild'].widget = RadioSelect(
                choices=KulukorvausPerustiedot.POSITION_CHOICES)
        for visible in self.visible_fields():
            if not visible.name == 'position_in_guild':
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = KulukorvausPerustiedot
        exclude = ['created_by_user']
        # Override Textarea default height
        widgets = {
            'explanation': Textarea(attrs={'rows': 1, 'cols': 1}),
            'additional_info': Textarea(attrs={'rows': 1, 'cols': 1}),
        }
        help_texts = {
            'target': 'esim. "Ruokakulut", "Kahvia kiltikselle" tai "Kilometrikorvaus" ',
            'explanation': 'esim. "Syyssitsit", "Fuksiryhmätapaaminen" tai "Kiltahuoneen uudistaminen"',
        }


class KulukorvausForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(KulukorvausForm, self).__init__(*args, **kwargs)
        self.empty_permitted = False

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Kulukorvaus
        exclude = ['created_by_user']
        widgets = {
            'additional_info': Textarea(attrs={'rows': 1, 'cols': 1}),
        }
        help_texts = {
            'target': 'esim. "Ruokakulut", "Kahvia kiltikselle" tai "Kilometrikorvaus" ',
            'explanation': 'esim. "Syyssitsit", "Fuksiryhmätapaaminen" tai "Kiltahuoneen uudistaminen"',
        }