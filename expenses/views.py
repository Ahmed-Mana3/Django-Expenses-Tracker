from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Expense
from django.utils import timezone   
from datetime import date

@login_required
def index(request):
    total = 0
    expenses_today = Expense.objects.filter(user=request.user, date=timezone.now().date()).order_by('-date', '-id')
    for expense in expenses_today:
        expense.amount = float(expense.amount)
        total += expense.amount
    return render(request, 'index.html', {'expenses_today': expenses_today, 'total': total})


@login_required
def add(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        category = request.POST.get('category')
        user = request.user
        if request.POST.get('date'):
            date = request.POST.get('date')
        else:
            date = timezone.now().date()

        expense = Expense.objects.create(
            user = user,
            amount = amount,
            date = date,
            description = description,
            category = category
        )
        expense.save()
        return redirect('index')

    return render(request, 'add.html')


@login_required
def history(request):
    food = 0
    transport = 0
    education = 0
    health = 0
    shopping = 0
    other = 0
    total = 0
    expenses = Expense.objects.filter(user=request.user).order_by('-date', '-id')
    categories = ["Food", "Transport", "Education", "Health", "Shopping", "Other"]
    for category in categories:
            for expense in expenses:
                if expense.category == category:
                    if category == "Food":
                        food += expense.amount
                    elif category == "Transport":
                        transport += expense.amount
                    elif category == "Education":
                        education += expense.amount
                    elif category == "Health":
                        health += expense.amount
                    elif category == "Shopping":
                        shopping += expense.amount
                    elif category == "Other":
                        other += expense.amount
    total = food + transport + education + health + shopping + other
    if total > 0:
        food_percentage = (food / total) * 100
        transport_percentage = (transport / total) * 100
        education_percentage = (education / total) * 100
        health_percentage = (health / total) * 100
        shopping_percentage = (shopping / total) * 100
        other_percentage = (other / total) * 100
    else:
        food_percentage = 0
        transport_percentage = 0
        education_percentage = 0
        health_percentage = 0
        shopping_percentage = 0
        other_percentage = 0

    return render(request, 'history.html', {'expenses': expenses, 'categories': categories,
        'food_percentage': food_percentage,
        'transport_percentage': transport_percentage,
        'education_percentage': education_percentage,
        'health_percentage': health_percentage,
        'shopping_percentage': shopping_percentage,
        'other_percentage': other_percentage
    })
