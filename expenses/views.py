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
    # Initialize category totals
    categories = ["Food", "Transport", "Education", "Health", "Shopping", "Other"]
    data = {cat: 0 for cat in categories}

    expenses = Expense.objects.filter(user=request.user).order_by('-date', '-id')

    # Sum up amounts
    total = 0
    for expense in expenses:
        if expense.category in data:
            # Ensure amount is float for calculation
            amount = float(expense.amount)
            data[expense.category] += amount
            total += amount

    # Calculate percentages safely
    if total > 0:
        percentages = {cat: (amt / total) * 100 for cat, amt in data.items()}
    else:
        percentages = {cat: 0 for cat in data}

    return render(request, 'history.html', {
        'expenses': expenses,
        'categories': categories,
        'food_percentage': percentages['Food'],
        'transport_percentage': percentages['Transport'],
        'education_percentage': percentages['Education'],
        'health_percentage': percentages['Health'],
        'shopping_percentage': percentages['Shopping'],
        'other_percentage': percentages['Other']
    })
