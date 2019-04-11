from django.shortcuts import render
from . import trs
from .models import User_detail
from .models import place
def index(request):
    return render(request,'index.html')
def load_form(request):
    name=request.POST['name']
    email=request.POST['email']
    d=User_detail()
    d.name=name
    d.email=email
    d.save()
    return render(request,'form.html')
def disp_res(request):
    age=request.POST['age']
    acc=request.POST['acc']
    occ=request.POST['occupation']
    mot=request.POST['m_o_t']
    dos=request.POST['dos']
    interest=request.POST['interest']
    age=int(age)
    dos=int(dos)
    if age>30:
        age=1
    else:
        age=0
    if acc== 'friends':
        acc=0
    else:
        acc=1
    if occ=='student':
        occ=0
    elif occ=='salaried':
        occ=1
    else:
        occ=2
    if mot=='feb' or mot == 'apr' or mot=='may' or mot=='mar':
        mot=0
    elif mot=='jun' and mot=='jul' and mot=='aug' and mot=='sept':
        mot=2
    else:
        mot=1
    if dos>7:
        dos=1
    else:
        dos=0
    if interest=='adventure':
        interest=0
    elif interest=='relaxation':
        interest=1
    else:
        interest=2
    y=trs.recommend(age,occ,acc,interest,mot,dos)
    if y==6:
        result='Leh Ladak'
    elif y==0:
        result='Andaman'
    elif y==1:
        result='Coorg'
    elif y==2:
        result='Darjeeling'
    elif y==3:
        result='Delhi'
    elif y==4:
        result='Goa'
    elif y==5:
        result='Jaipur'
    elif y==7:
        result='Manali'
    elif y==8:
        result='Munnar'
    elif y==9:
        result='Mysore'
    #context={'result':result}
    res=place.objects.get(pk=result)
    return render(request, 'result.html', {'name':res.name,'desc':res.desc,'img':res.img})