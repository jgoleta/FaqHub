from django.shortcuts import render

def dashboard(request):
    # Hardcoded professor data
    professors = [
        {
            'name': 'Ian Vance',
            'department': 'TER SCIENCE',
            'status': 'Available',
            'status_color': 'green',
            'last_seen': 'Just now',
            'room': 'RM 402',
            'note': '',
        },
        {
            'name': 'Marisa Clara Santos',
            'department': 'BUSINESS & TECH',
            'status': 'Busy',
            'status_color': 'orange',
            'last_seen': '2 mins ago',
            'room': '',
            'note': 'In a meeting until 3 PM',
        },
        {
            'name': 'Marcus Wu',
            'department': 'ADMISSION OFFICE',
            'status': 'Virtual only',
            'status_color': 'blue',
            'last_seen': '1 hour ago',
            'room': '',
            'note': 'Remote – book a Zoom slot',
        },
        {
            'name': 'Dr. Sarah Jenkins',
            'department': 'ADMISSION OFFICE',
            'status': 'On leave',
            'status_color': 'gray',
            'last_seen': 'Yesterday',
            'room': '',
            'note': 'Returns next Monday',
        },
    ]

    context = {
        'professors': professors,
        #add more
    }
    return render(request, 'dashboard.html', context)

def login_page(request):
    return render(request, 'login.html')

def landing_page(request):
    return render(request, 'landing.html')