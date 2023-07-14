from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstName']) < 2:
            errors["firstName"] = "First Name should be at least 2 characters"
        if len(postData['lastName']) < 2:
            errors["lastName"] = "Last Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 6:
            errors["password"] = "Password should be at least 6 characters"
        

        return errors
    
class User(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    objects = UserManager()

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title