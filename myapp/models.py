from django.db import models

# Create your models here.

class AuditEntry(models.Model):
    action_test_long_one_field_is_long = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)
    log_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

