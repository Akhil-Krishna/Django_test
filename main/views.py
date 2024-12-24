from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'main/index.html')









#user login
# main/views.py
# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'main/sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = SignInForm()
    return render(request, 'main/sign_in.html', {'form': form})



def profile(request):

    context = {
        'user': request.user,
    }
    return render(request, 'main/profile.html', context)



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/notifications.html', {'notifications': user_notifications})

@login_required
def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications')


#notify user

from .utils import notify_user

def notify(request):
    # Some logic
    notify_user(request.user, "You have a new job notification", "http://example.com/job")
    
    
    
    
    
    
    

from .models import Person ,customuser

def explore(request):
    person = customuser.objects.all()
    return render(request, 'main/person.html', {'persons': person})
@login_required
def person_detail(request, person_id):
    person = get_object_or_404(customuser, pk=person_id)
    

    context = {
        'person': person,
    }
    return render(request, 'main/person_detail.html', context)




# views.py (where users start a course)





