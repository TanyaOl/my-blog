
from django.db import models
from django.utils import timezone
from django.forms import ModelForm # импорт ModelForm


def approved_comments(self):
    return self.comments.filter(approved_comment=True)



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    #image = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d', help_text='150x150px', verbose_name='Ссылка картинки')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

   
   
    #def image_img(self):
    #    if self.image:
    #        return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
    #    else:
    #        return '(Нет изображения)'
    #image_img.short_description = 'Картинка'
    #image_img.allow_tags = True

    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

   

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text





        





