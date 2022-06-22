from django.db import models

# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename= "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class register(models.Model):
    name=models.TextField(max_length=191)
    email=models.EmailField(unique=True, max_length=191)
    phone_no=models.BigIntegerField()
    password=models.CharField(max_length=800)

    def _str_(self):
            return self.name

    def isExists(self):
        if register.objects.filter(email=self.email):           #return true or false
            return True
        else:
            return False

    