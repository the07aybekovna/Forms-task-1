from django import forms


class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label="First Number")
    num2 = forms.FloatField(label="Second Number")

    OPERATIONS = [
        ("+", "Addition (+)"),
        ("-", "Subtraction (-)"),
        ("*", "Multiplication (*)"),
        ("/", "Division (/)"),
    ]

    operation = forms.ChoiceField(
        choices=OPERATIONS,
        label="Arithmetic Operations"
    )

    def clean(self):
        cleaned_data = super().clean()
        num2 = cleaned_data.get("num2")
        operation = cleaned_data.get("operation")

        if operation == "/" and num2 == 0:
            self.add_error("num2", "ZeroDivisionError")

        return cleaned_data