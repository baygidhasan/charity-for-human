from django.shortcuts import render,redirect
from charity.forms import CharityForm
from charity.models import Charity
def create (request):

    if request.method=="POST":
        form=CharityForm(request.POST)

        if form.is_valid():
            form.save()  #
            return redirect("/all-charity")
    else:
        form=CharityForm()

    return render(request,'create.html',{'form':form})
def show(request):
    charitys=Charity.objects.all()
    return render(request,"show.html",{'charitys':charitys})

def delete(request,id):
    charity = Charity.objects.get(id=id)
    charity.delete()
    return redirect("/all-charity")

