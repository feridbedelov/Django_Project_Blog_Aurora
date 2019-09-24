from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here./

def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html', {'form': form   } ) 


@login_required
def profile(request):

    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)


@login_required
def change_pass(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
        
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'users/change_pass.html',{'form':form})
