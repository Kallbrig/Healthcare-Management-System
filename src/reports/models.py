from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.utils.timezone import now
from django.template.defaultfilters import slugify


# Models aparently have no way of filtering which users reports can be made for.
# The class below allows reports to be made for any user.
# This isn't problematic for now and can be used to promote scalability later.
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=now())
    end_date = models.DateField(default=now())
    health_service_income = models.PositiveIntegerField(default=0)
    patients_seen = models.SmallIntegerField()

    # When called, report will print out the name of the user (Doctor) it is associated with.
    def __str__(self):
        return self.user.__str__()

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})

# Filtering Example
# Aparently django doesn't have built in methods to prevent
# class Parent(models.Model):
#   name = models.CharField(max_length=255)
#   favoritechild = models.ForeignKey("Child", blank=True, null=True)
#
#   def save(self, force_insert=False, force_update=False):
#     if self.favoritechild is not None and self.favoritechild.myparent.id != self.id:
#       raise Exception("You must select one of your own children as your favorite")
#     super(Parent, self).save(force_insert, force_update)
