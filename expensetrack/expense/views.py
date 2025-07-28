from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
from django.utils import timezone

# Create your views here.
def index (request):
    expenses = Expense.objects.all().order_by('-id')
    today_total_expenses = Expense.objects.filter(created_at=timezone.now().date()).aggregate(total=Sum('amount'))['total'] or 0
    current_week_total_expenses = Expense.objects.filter(created_at__week=timezone.now().isocalendar()[1]).aggregate(total=Sum('amount'))['total'] or 0
    current_month_total_expenses = Expense.objects.filter(created_at__month=timezone.now().month).aggregate(total=Sum('amount'))['total'] or 0

    stats = {
        'today_total': today_total_expenses,
        'current_week_total': current_week_total_expenses,
        'current_month_total': current_month_total_expenses,
    }

    return render(request, 'expense/index.html', {'expenses': expenses, 'stats': stats})

def create (request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            form.user = request.user
            form.save()

            # Redirect to the index page after saving the form
            return redirect('expenses:index')
    else:
        form = ExpenseForm()
    return render(request, 'expense/create.html', {'form': form})

def edit (request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()

            # Redirect to the index page after saving the form
            return redirect('expenses:index')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense/edit.html', {'form': form})

def delete (request, pk):
    expense = get_object_or_404(Expense, pk=pk)

    if request.method == 'POST':
        expense.delete()

    # Redirect to the index page after saving the form
    return redirect('expenses:index')     