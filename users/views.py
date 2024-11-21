from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect  
from .models import User  
from .forms import UserForm  
# Create your views here.


def user_list(request):  
    users = User.objects.all()  
    return render(request, 'users/user_list.html', {'users': users})  

def user_create(request):  
    if request.method == 'POST':  
        form = UserForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('user_list')  
    else:  
        form = UserForm()  
    return render(request, 'users/user_form.html', {'form': form})  

def user_update(request, pk):  
    user = get_object_or_404(User, pk=pk)  
    if request.method == 'POST':  
        form = UserForm(request.POST, instance=user)  
        if form.is_valid():  
            form.save()  
            return redirect('user_list')  
    else:  
        form = UserForm(instance=user)  
    return render(request, 'users/user_form.html', {'form': form})  

def user_delete(request, pk):  
    user = get_object_or_404(User, pk=pk)  
    if request.method == 'POST':  
        user.delete()  
        return redirect('user_list')  
    return render(request, 'users/confirm_delete.html', {'user': user})