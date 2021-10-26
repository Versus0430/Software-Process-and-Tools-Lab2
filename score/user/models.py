import datetime

from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生"

    rank_update_time = datetime.date.today()
    equation_num_rank_dict = {}
    right_radio_rank_dict = {}

    US_account = models.CharField(verbose_name="账号", max_length=128, blank=False, null=False, unique=True)
    US_password = models.CharField(verbose_name="密码", max_length=128, blank=False, null=False, unique=False)
    US_name = models.CharField(verbose_name="姓名", max_length=128, blank=False, null=False, unique=False)
    US_equation_num = models.PositiveIntegerField(verbose_name="做题量", default=0, blank=False, null=False)
    US_right_radio = models.DecimalField(verbose_name="正确率", decimal_places=2, max_digits=5, default=0.00, blank=False, null=False)

    def __str__(self):
        return self.US_name
