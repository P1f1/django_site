from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Кол-во',
        widget=forms.HiddenInput)

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)


class CartEditProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Кол-во')

    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
