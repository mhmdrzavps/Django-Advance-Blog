from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
# Create your models here.

class Post(models.Model):
    '''
    this is a class for define posts for blog app
    '''
    title = models.CharField(max_length = 250)
    content = models.TextField()
    image =models.ImageField(upload_to= 'blog/', default= 'images.png')
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey('Category', on_delete= models.SET_NULL, null= True)
    status = models.BooleanField(default= False)
    counted_view = models.IntegerField(default= 0)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now= True)
    published_date = models.DateTimeField(null= True)

    def __str__(self):
        return self.title

class Category(models.Model):

    name = models.CharField(max_length= 250)

    def __str__(self):
        return self.name