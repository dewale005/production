from django.shortcuts import render, redirect

from .forms import EmployeeForm
# Create your views here.
def apply(request):
    if  request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emloyee_item = form.save(commit=False)
            emloyee_item.save()
            return redirect('success/')
    else:
        form = EmployeeForm()
    return render(request, "apply.html", {'form':form})

def home(request):
    return render(request, "home.html")

def success(request):
    return render(request, "success.html")