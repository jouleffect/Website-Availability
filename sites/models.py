from django.db import models

class SiteAvail(models.Model):
    get_time = models.DateTimeField()
    url = models.CharField(max_length=100)
    regex = models.CharField(max_length=50,default='')
    status_code = models.CharField(max_length=10)
    time_elapsed = models.CharField(max_length=10)
    is_match_regex = models.BooleanField(default=False)

    def __str__(self):
        return self.url