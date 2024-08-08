from django.contrib import admin

# Register your models here.

from Home.models import Survey, Question, Choice, Submission, estadocasino

class QuestionInline(admin.TabularInline):
  model = Question
  show_change_link = True

class ChoiceInline(admin.TabularInline):
  model = Choice


class SurveyAdmin(admin.ModelAdmin):
  inlines = [
    QuestionInline
  ]

class QuestionAdmin(admin.ModelAdmin):
  inlines = [
    ChoiceInline
  ]

class SubmissionAdmin(admin.ModelAdmin):
  list_display = ('id', 'status')


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)

#########################################################################################################################

class estadocasinoinline(admin.ModelAdmin):
  model = estadocasino
  show_change_link = True

class estadocasinoAdmin(admin.ModelAdmin):
  inlines = [
    estadocasinoinline
  ]

admin.site.register(estadocasino)
