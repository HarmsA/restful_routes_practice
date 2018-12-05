from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import User


# Create your views here.
def index(request):
    """Renders all users in a user list"""
    all_users = User.objects.all()

    context = {
        'all_users':all_users
    }
    return render(request, 'users/users_list.html', context)


def new(request):
    return render(request, 'users/new.html')

def update_user(request, id):
    '''Gets user from Edit.html and verifies if email is the same,
    if it is, validates at models.validate_update, else goes to
    models.validate.
    Then if errors are found it displays the errors, else saves the
    new values for the user and displays them.'''

    if User.objects.get(id=id).email==request.POST['email']:
        errors = User.objects.validate_update(request.POST)
    else:
        errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        user = User.objects.get(id=id)
        user.l_name = request.POST['l_name'].capitalize()
        user.f_name = request.POST['f_name'].capitalize()
        user.email = request.POST['email']
        user.save()


    context = {
        'id': id,
        'f_name': User.objects.get(id=id).f_name,
        'l_name': User.objects.get(id=id).l_name,
        'email': User.objects.get(id=id).email,
        'created': User.objects.get(id=id).updated_at
    }
    return render(request, 'users/edit.html', context)

def create_verify(request):
    '''Creates a user object from user_list.html verifies
    the data in User.objects.validate in the models.py file.
    Then creates the user objects from User.objects.create_user in the
    models.py file'''
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
    return redirect('/users/new')

def show(request, id):
    '''creates a temp dict object to render the specific id
    of the user clicked on for more detailed info'''
    context = {
        'id' : id,
        'f_name': User.objects.get(id=id).f_name,
        'l_name': User.objects.get(id=id).l_name,
        'email': User.objects.get(id=id).email,
        'created': User.objects.get(id=id).created_at,
    }
    return render(request,'users/user.html', context)

def delete(request, id):
    """Deletes specific user object"""
    dead = User.objects.get(id=id)
    dead.delete()
    return redirect('/users/index/')

def edit(request, id):
    '''creates a temp dict object to render the specific id
    of the user clicked on to edit user'''
    context = {
        'id' : id,
        'f_name': User.objects.get(id=id).f_name,
        'l_name': User.objects.get(id=id).l_name,
        'email': User.objects.get(id=id).email,
        'created': User.objects.get(id=id).created_at,
    }
    return render(request, 'users/edit.html', context)
