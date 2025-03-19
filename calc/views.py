from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {}
    return render(request, 'calc/calculator.html', context)

def profile(request):
    context = {}  # Initialize context

    if request.method == 'POST':
        number_one = request.POST.get('number_one')
        number_two = request.POST.get('number_two')
        operation = request.POST.get('operation')

        if number_one and number_two:  # Ensure both numbers are provided
            try:
                number_one = float(number_one)
                number_two = float(number_two)

                if operation == 'add':
                    result = number_one + number_two
                elif operation == 'subtract':
                    result = number_one - number_two
                elif operation == 'multiply':
                    result = number_one * number_two
                elif operation == 'divide':
                    if number_two == 0:
                        result = "Error: Division by zero"
                    else:
                        result = number_one / number_two
                else:
                    result = "Invalid operation"

                context['result'] = result

            except ValueError:
                context['result'] = "Error: Invalid input"
        else:
            context['result'] = "Error: Missing input"

    return render(request, 'calc/calculator.html', context)