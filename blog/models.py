from re import VERBOSE
from extensions.utils import jalali_converter
from django.db import models
from django.utils import timezone

# Create your models here.


class Catergory(models.Model):
    title=models.CharField(max_length=200,verbose_name="عنوان دسته بندی")
    slug=models.SlugField(max_length=100,unique=True,verbose_name="آدرس دسته بندی")
    status=models.BooleanField(default=True,verbose_name="نمایش داده شود؟")
    position=models.IntegerField(verbose_name="موقیعت")

    class Meta:
        verbose_name="دسته بندی"
        verbose_name_plural="دسته بندی ها"
        ordering=['position']

    def __str__(self) :
        return self.title







class Article(models.Model):
    STATUS_CHICES=(
        ('d','‍‍\یش نویس'),
        ('p','منتشر شده')
    )
    title=models.CharField(max_length=200,verbose_name="عنوان")
    slug=models.SlugField(max_length=100,unique=True,verbose_name="آدرس ")
    category=models.ManyToManyField(Catergory,verbose_name="دسته بندی",related_name="articles")
    desc=models.TextField(verbose_name="محتوا")
    thumbnail=models.ImageField(upload_to="media/images",verbose_name="تصویر ")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHICES,verbose_name="وضعیت")
    
    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
        ordering=['-publish']
    def __str__(self) :
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description="زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)