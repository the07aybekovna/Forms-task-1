from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CalculatorForm

def index(request):
    return HttpResponse("<h1>Welcome to our calculator</h1>")

def calculator(request):
    if request.method == "POST":
        form = CalculatorForm(request.POST)

        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            operation = form.cleaned_data["operation"]

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            else:
                result = num1 / num2

            request.session["calculation"] = {
                "num1": num1,
                "num2": num2,
                "operation": operation,
                "result": result,
            }

            return redirect("calculator_result")

    else:
        form = CalculatorForm()

    return render(request, "calculator.html", {"form": form})


def calculator_result(request):
    calculation = request.session.get("calculation")

    if calculation is None:
        return redirect("calculator")

    return render(
        request,
        "calculator_result.html",
        {"calculation": calculation}
    )