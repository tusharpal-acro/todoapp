from django.db import models


# Create your models here.
class Category(models.Model):
    parentCategory = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
        
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    assigned_date = models.DateTimeField('date assigned')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
