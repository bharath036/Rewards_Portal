from django.shortcuts import render, redirect
from home.models import *

# Create your views here.

def index(request):
    # Check if the request method is POST (i.e., form has been submitted)
    if request.method == "POST":
        # Get the description from the form input named 'description'
        appreciation = request.POST.get('appreciation')

        # Get the amount from the form input named 'amount'
        points = request.POST.get("points")

        # Fetch the current balance object with id=1, or create it if it doesn’t exist
        available_points, _ = AvailablePoints.objects.get_or_create(id=1)

        # Assume it's income by default
        points_type = "GIVE"

        # If the amount is negative, it's a DEBIT (i.e., an expense)
        if float(points) < 0:
            expense_type = "Take"

        # Create a new TrackingHistory entry with the data collected
        tracking_history = TrackingHistory.objects.create(
            points=points,
            points_type=points_type,
            available_points=available_points,
            appreciation = appreciation
        )

        # Update the current balance by adding the transaction amount
        available_points.availablepoints += float(tracking_history.points)
        available_points.save()  # Save the updated balance to the database

        # After adding the transaction, redirect to the homepage to avoid resubmission
        return redirect('home/')

    # If it's a GET request (initial page load), fetch current balance
    available_points, _ = AvailablePoints.objects.get_or_create(id=1)

    Received = 0  # To hold total income
    Sent = 0  # To hold total expense

    # Loop through all transactions to compute total income and expenses
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.points_type == "TAKE":  # If it's income
            Received += tracking_history.points
        else:  # If it's an expense
            Sent += tracking_history.points

    # Context dictionary to pass data to the HTML template
    context = {
        'Received': Received,
        'Sent': Sent,
        'transactions': TrackingHistory.objects.all(),  # All transaction history
        'available_points': available_points  # Latest balance
    }

    
    return render(request,'home.html',context)
