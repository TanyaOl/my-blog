# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='150x150px', upload_to='images/blog/%Y/%m/%d', verbose_name='Ссылка картинки', blank=True),
        ),
    ]
