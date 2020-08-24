from django.contrib import admin
from cms.models import QuestionList , Log


# admin.site.register(QuestionList)

class QuestionListAdmin(admin.ModelAdmin):
    list_display = ('id',)  # 一覧に出したい項目
    list_display_links = ('id',)  # 修正リンクでクリックできる項目


admin.site.register(QuestionList, QuestionListAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('id',)  # 一覧に出したい項目
    list_display_links = ('id',)  # 修正リンクでクリックできる項目


admin.site.register(Log, LogAdmin)