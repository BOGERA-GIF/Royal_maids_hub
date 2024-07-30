from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ContactForm

# def admission_form(request):
#     if request.method == 'POST':
#         form = AdmissionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Redirect to a success page
#     else:
#         form = AdmissionForm()
#     return render(request, 'admissions/admission_form.html', {'form': form})

# def success(request):
#     return render(request, 'admissions/success.html')


# from django.shortcuts import render, redirect
# from .forms import AdmissionForm

def application(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'application.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def about_view(request):
    return render(request, 'about.html')
def booking(request):
    return render(request, 'booking.html')
def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')