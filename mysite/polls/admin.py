from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ["question_text"]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)