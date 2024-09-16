from django.shortcuts import render, redirect
from .models import Food,consume

# Create your views here.

def index(request):
        if request.method == "POST":
            data = request.POST["food_consumed"]
            consumed = Food.objects.get(name=data)
            user = request.user
            consumed = consume.objects.create(user=user,food_consumed = consumed)
            Foods = Food.objects.all()
            return redirect('index')
        else:
            Foods = Food.objects.all()
        consumed_food = consume.objects.filter(user=request.user)
        return render(request,'myapp/index.html',{"Foods":Foods,"consumed_food":consumed_food})

def delete_consume(request,id):
    consumed_food = consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')
    return render(request,"myapp/delete.html")

