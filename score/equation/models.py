from django.db import models

from user.models import User

source_choices = (
    ("正确", "正确"),
    ("错误", "错误"),
    ("未完成", "未完成"),
)


# Create your models here.
class Equation(models.Model):
    class Meta:
        verbose_name = "加减法训练"
        verbose_name_plural = "加减法训练"

    EQ_user = models.ForeignKey(to=User, verbose_name="学生", blank=True, default="", on_delete=models.CASCADE)
    EQ_question = models.CharField(verbose_name="题目", max_length=128, blank=False, null=False, unique=False)
    EQ_answer = models.CharField(verbose_name="答案", max_length=128, blank=True, null=False)
    EQ_result = models.CharField(verbose_name="结果", choices=source_choices, max_length=128, blank=False, null=False)
    EQ_update_time = models.DateField(verbose_name="时间", blank=False, null=False, auto_now=True)

    def __str__(self):
        return self.EQ_user.US_name + self.EQ_question
