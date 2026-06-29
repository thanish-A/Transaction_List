from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {
        'transactions': transactions
    })


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'transaction_form.html', {
        'form': form
    })


def edit_transaction(request, id):
    transaction = get_object_or_404(
        Transaction,
        id=id
    )

    if request.method == 'POST':
        form = TransactionForm(
            request.POST,
            instance=transaction
        )

        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(
            instance=transaction
        )

    return render(
        request,
        'transaction_form.html',
        {'form': form}
    )


def delete_transaction(request, id):
    transaction = get_object_or_404(
        Transaction,
        id=id
    )

    transaction.delete()

    return redirect('transaction_list')