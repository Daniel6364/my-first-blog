#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)





# User._meta.get_fields()
# (<ManyToOneRel: admin.logentry>, 
# <ManyToOneRel: blog.post>, 
# <django.db.models.fields.AutoField: id>, 
# <django.db.models.fields.CharField: password>, 
# <django.db.models.fields.DateTimeField: last_login>,
# <django.db.models.fields.BooleanField: is_superuser>, 
# <django.db.models.fields.CharField: username>, 
# <django.db.models.fields.CharField: first_name>, 
# <django.db.models.fields.CharField: last_name>, 
# <django.db.models.fields.EmailField: email>, 
# <django.db.models.fields.BooleanField: is_staff>, 
# <django.db.models.fields.BooleanField: is_active>, 
# <django.db.models.fields.DateTimeField: date_joined>, 
# <django.db.models.fields.related.ManyToManyField: groups>, 
# <django.db.models.fields.related.ManyToManyField: user_permissions>)
