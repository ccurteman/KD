from django import forms

class MeleeAttack(forms.Form):
    name = forms.CharField(label='Melee Attack')
    # character = forms.ModelChoiceField(queryset=' ', empty_label=None)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['foo_select'].queryset = 