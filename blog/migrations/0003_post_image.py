# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, verbose_name='Ссылка картинки', help_text='150x150px', upload_to='static/media/images/blog/%Y/%m/%d'),
        ),
    ]
