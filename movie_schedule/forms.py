from django import forms


class TicketPaymentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name on card")
    email = forms.EmailField(label="Email")
    card_number = forms.CharField(max_length=19, label="Card number")
    expiration_at = forms.CharField(max_length=5, label="MM/YY")
    cvv_code = forms.CharField(max_length=4, label="CVV")

    def clean_card_number(self):
        num = self.cleaned_data['card_number'].replace(' ', '')
        if not num.isdigit() or len(num) != 16:
            raise forms.ValidationError("Wrong card number!")
        return num
