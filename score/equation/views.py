import datetime

from django.shortcuts import render

from user.models import User
from .forms import EquationForm, UserForm
from .models import Equation

import random


# Create your views here.
def login(request):
    if request.method == "GET":
        user_form = UserForm()
        return render(request, "login.html", locals())
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            student_username = user_form.cleaned_data["US_account"]
            student_password = user_form.cleaned_data["US_password"]

            student = User.objects.filter(US_account=student_username)

            if len(student) == 0:
                mes = "用户名不存在"
                return render(request, "exception.html", locals())
            else:
                student = student[0]
                if student_password != student.US_password:
                    mes = "密码错误"
                    return render(request, "exception.html", locals())

            # 获取个人统计信息并更新
            total_equation_num = len(Equation.objects.filter(EQ_user=student))
            wrong_equation_num = len(Equation.objects.filter(EQ_user=student, EQ_result="错误"))

            if total_equation_num != 0:
                right_radio = round((1 - float(wrong_equation_num) / total_equation_num) * 100, 2)
            else:
                right_radio = 0.00

            student.US_equation_num = total_equation_num
            student.US_right_radio = right_radio
            student.save()

            # 如果类总表不是最新的，就更新
            # if User.rank_update_time != datetime.date.today():
            temp_data = User.objects.values("US_name", "US_equation_num", "US_right_radio")
            equation_num_dict = {student["US_name"]: student["US_equation_num"] for student in temp_data}
            right_radio_dict = {student["US_name"]: student["US_right_radio"] for student in temp_data}

            sorted_equation_num_list = sorted(equation_num_dict.items(), key=lambda stu: (stu[1], stu[0]), reverse=True)
            sorted_right_radio_list = sorted(right_radio_dict.items(), key=lambda stu: (stu[1], stu[0]), reverse=True)

            User.equation_num_rank_dict = {sorted_equation_num_list[i][0]: i + 1 for i in range(len(sorted_equation_num_list))}
            User.right_radio_rank_dict = {sorted_right_radio_list[i][0]: i + 1 for i in range(len(sorted_right_radio_list))}
            User.rank_update_time = datetime.date.today()

            # 若要每天更新，就把上面那段放在for里面
            student_equation_num_rank = User.equation_num_rank_dict[student.US_name]
            student_right_radio_rank = User.right_radio_rank_dict[student.US_name]

            return render(request, "student.html", locals())


def exercise(request, account):
    number_1 = random.randint(0, 100)
    number_2 = random.randint(number_1, 100)
    number_3 = random.randint(0, 1)
    right_answer = 0

    if number_3 == 0:
        sign = '+'
        right_answer = str(number_1 + number_2)
    else:
        sign = '-'
        right_answer = str(number_2 - number_1)

    question = str(number_2) + sign + str(number_1) + "="
    equation_form = EquationForm()

    return render(request, "equation.html", locals())


def judge(request, account, question, right_answer):
    equation_form = EquationForm(request.POST)
    if equation_form.is_valid():
        student_answer = equation_form.cleaned_data["EQ_input"]

        try:
            if int(student_answer) == int(right_answer):
                result = "正确"
            else:
                result = "错误"
        except ValueError:
            return render(request, "ValueError.html", locals())

        today = datetime.date.today()

        student = User.objects.filter(US_account=account)
        if len(student) == 0:
            visitor = User.objects.filter(US_account="Unknown", US_password="000000", US_name="小明")
            if len(visitor) == 0:
                visitor = User(US_account="Unknown", US_password="000000", US_name="小明")
                visitor.save()
            else:
                visitor = visitor[0]
            student = visitor
        else:
            student = student[0]

        equation = Equation(EQ_user=student, EQ_question=question, EQ_answer=student_answer, EQ_result=result, EQ_update_time=today, )
        equation.save()

        # 学生信息更新
        total_equation_num = len(Equation.objects.filter(EQ_user=student))
        wrong_equation_num = len(Equation.objects.filter(EQ_user=student, EQ_result="错误"))
        if total_equation_num != 0:
            right_radio = round((1 - float(wrong_equation_num) / total_equation_num) * 100, 2)
        else:
            right_radio = 0.00

        student.US_equation_num = total_equation_num
        student.US_right_radio = right_radio
        student.save()

        return render(request, "result.html", locals())
    else:
        mes = "很抱歉系统出现错误"
        return render(request, "exception.html", locals())


def wrong_notebook(request, account):
    wrong_equation_list = Equation.objects.filter(EQ_user__US_account=account, EQ_result="错误")
    wrong_equation_book = [[wrong_equation.EQ_question, wrong_equation.EQ_answer, str(wrong_equation.EQ_update_time)] for
                           wrong_equation in wrong_equation_list]
    return render(request, "notebook.html", locals())
