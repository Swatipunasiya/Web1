from django.shortcuts import render, HttpResponseRedirect
from.forms import My_forms
from.models import Mymodel
# Create your views here.
def MyView(r):
    form= My_forms
    if r.method=='POST':
        form=My_forms(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/record')
    return render(r,'form.html',{'form':form})

def Myrecord(r):
    obj=Mymodel.objects.all()
    return render(r,'record.html',{'obj': obj})

def Delete(r,id):
    obj=Mymodel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/record')

def Update(r,id):
    obj = Mymodel.objects.get(id=id)
    form = My_forms
    if r.method == 'POST':
        form = My_forms(r.POST, r.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/record')
    return render(r, 'update.html', {'form': form})