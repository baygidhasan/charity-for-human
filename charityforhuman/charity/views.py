from django.shortcuts import render
from charity.forms import CharityForm
def create (request):

    if request.method=="POST":
        pass
    else:
        form=CharityForm()

    return render(request,'create.html',{'form':form})