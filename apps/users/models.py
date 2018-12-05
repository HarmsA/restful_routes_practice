from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):

    def validate_update(self, form):
        '''Validates only if email is the same as original'''
        errors = []
        if len(form['f_name']) < 2:
            errors.append('First Name must have more than 2 characters')
        if len(form['l_name']) < 2:
            errors.append('Last Name must have more than 2 characters')
        return errors

    def validate(self, form):
        '''Validates new user objects creation and updated
        objects only when email is different from original
        in view update_user function'''
        errors = []
        if len(form['f_name'])<2:
            errors.append('First Name must have more than 2 characters')
        if len(form['l_name'])<2:
            errors.append('Last Name must have more than 2 characters')

        if not EMAIL_REGEX.match(form['email']):
            errors.append('Email must be valid')
        email_list = self.filter(email=form['email'])
        if len(email_list) > 0:
            errors.append('Email already in use')
        return errors

    def create_user(self, form):
        """Creates a brand new user"""
        user = self.create(
            f_name = form['f_name'].capitalize(),
            l_name = form['l_name'].capitalize(),
            email = form['email'],
        )
        return user

class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        f = f'{self.f_name} {self.l_name} {self.email}'
        return f