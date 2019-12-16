from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=300)
    primaryCategory=models.BooleanField(default=False)
    image=models.ImageField(blank=True,upload_to='cat_images/')
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title 


#product models

class Product(models.Model):
    mainimage=models.ImageField(upload_to='products/',blank=True)    
    name=models.CharField(max_length=300)
    slug=models.SlugField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    preview_text=models.TextField(max_length=200)
    detail_text=models.TextField(max_length=1000)
    price=models.FloatField()

    def __str__(self):
        return self.name