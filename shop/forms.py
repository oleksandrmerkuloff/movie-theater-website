from django import forms


class PaymentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Full Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'John Doe'}
        )
    )
    email = forms.EmailField(
        max_length=150,
        label='Email Address',
        widget=forms.EmailInput(
            attrs={'placeholder': 'you@example.com'}
        )
    )
    card_numeber = forms.CharField(
        max_length=30,
        label='Card number'
    )
    expiration_at = forms.CharField(
        max_length=10,
        label='Your card date',
        widget=forms.TextInput(
            attrs={'placeholder': 'MM/YY'}
        )
    )
    cvv_code = forms.CharField(
        max_length=5,
        label='CVV Code'
    )
    order_type = forms.ChoiceField(
        label='Delivery Option',
        initial='Choose order type',
        choices=[
            ('Food', 'Food'),
            ('Tickets', 'Tickets')
        ]
    )
