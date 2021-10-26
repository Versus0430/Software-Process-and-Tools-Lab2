import datetime
from io import BytesIO

from django.contrib import admin

# Register your models here.
from django.core.paginator import Paginator
from django.http import StreamingHttpResponse
from xlwt import Workbook

from equation.models import Equation


@admin.register(Equation)
class EquationAdmin(admin.ModelAdmin):
    list_display = ["EQ_user", "EQ_question", "EQ_answer", "EQ_result", "EQ_update_time"]

    list_filter = ["EQ_result", "EQ_user"]  # 筛选框

    search_fields = ["EQ_user__US_name"]

    list_per_page = 15
    paginator = Paginator

    def export_excel(self, request, queryset):
        # 导出excel表
        # 创建工作簿
        ws = Workbook(encoding='utf-8')
        # 添加第一页数据表
        w = ws.add_sheet(u"第一页")
        # 写入表头
        verbose_name_list = ['学生', '题目', '答案', '结果', '时间']
        for i in range(len(verbose_name_list)):
            w.write(0, i, verbose_name_list[i])

        # 写入数据
        excel_row = 1
        for equation in queryset:
            # 写入每一行对应的数据
            w.write(excel_row, 0, equation.EQ_user.US_name)
            w.write(excel_row, 1, equation.EQ_question)
            w.write(excel_row, 2, equation.EQ_answer)
            w.write(excel_row, 3, equation.EQ_result)
            w.write(excel_row, 4, equation.EQ_update_time)
            excel_row += 1

        # 实现下载
        output = BytesIO()
        ws.save(output)
        output.seek(0)
        response = StreamingHttpResponse(output)
        response['content_type'] = 'application/vnd.ms-excel'
        response['charset'] = 'utf-8'
        response['Content-Disposition'] = 'attachment; filename="{0}.xls"'.format(str(datetime.date.today()))
        return response

    export_excel.short_description = "导出所选记录"
    actions = [export_excel]
