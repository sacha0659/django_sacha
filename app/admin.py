from dataclasses import field
from django.contrib import admin

from .models import Question
from .models import Member

class QuestionAdmin(admin.ModelAdmin):
    fields = ['text']

admin.site.register(Question)
admin.site.register(Member)

# Register your models here.
