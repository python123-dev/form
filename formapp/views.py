from django.shortcuts import render
#from .models import customer
from .forms import customerform


# Create your views here.
# username : dforms
# password : django123
def index(request):
    form = customerform()
    if request.method == 'POST':
        print(request.POST)
        form = customerform(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', {'form': form})
