from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    STATUS_CHICES=(
        ('d','‍‍\یش نویس'),
        ('p','منتشر شده')
    )
    title=models.CharField(max_length=200,verbose_name="عنوان")
    slug=models.SlugField(max_length=100,unique=True,verbose_name="آدرس ")
    desc=models.TextField(verbose_name="محتوا")
    thumbnail=models.ImageField(upload_to="media/images",verbose_name="تصویر ")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHICES,verbose_name="وضعیت")
    
    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
    def __str__(self) :
        return self.title