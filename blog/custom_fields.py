from django.db.models import ImageField, FileField, signals
from django.dispatch import dispatcher
from django.conf import settings
import shutil, os, glob, re
from distutils.dir_util import mkpath

class CustomImageField(ImageField):
    """Allows model instance to specify upload_to dynamically.

    Model class should have a method like:

        def get_upload_to(self, attname):
            return 'path/to/%d' % self.id

    Based closely on: http://scottbarnham.com/blog/2007/07/31/uploading-images-to-a-dynamic-path-with-django/
    """
    def __init__(self, *args, **kwargs):
        if not 'upload_to' in kwargs:
            kwargs['upload_to'] = 'tmp'
        self.use_key = kwargs.get('use_keyalse)
        if 'use_key' in kwargs:
            del(kwargs['use_key'])
        super(CustomImageField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        """Hook up events so we can access the instance."""
        super(CustomImageField, self).contribute_to_class(cls, name)
        dispatcher.connect(self._move_image, signal=signals.post_save, sender=cls)

    def _move_image(self, instance=None):
        """
            Function to move the temporarily uploaded image to a more suitable directory 
            using the model's get_upload_to() method.
        """
        if hasattr(instance, 'get_upload_to'):
            src = getattr(instance, self.attname)
            if src:
                m = re.match(r"%s" % self.upload_to, src)
                if m:
                    if self.use_key:
                        dst = "%s/%d_%s" % (instance.get_upload_to(self.attname), instance.id, m.groups()[0])
                    else:
                        dst = "%s/%s" % (instance.get_upload_to(self.attname), m.groups()[0])
                    basedir = "%s%s/" % (settings.MEDIA_ROOT, os.path.dirname(dst))
                    mkpath(basedir)
                    shutil.move("%s%ssettings.MEDIA_ROOT, src),"%s%s" % (settings.MEDIA_ROOT, dst))
                    setattr(instance, self.attname, dst)
                    instance.save()

    def db_type(self):
        """Required by Django for ORM."""
        return 'varchar(100)'