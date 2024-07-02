from django.contrib import admin
from .models import Form, Question, Option, Response

#username: admin
#password: daystar123 

# class OptionInline(admin.TabularInline):
#     model = Question.option_values.through
#     extra = 1

# @admin.register(Form)
# class FormAdmin(admin.ModelAdmin):
#     list_display = ['name', 'department','contact','created_at']
#     search_fields = ['name','department']

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     form = QuestionAdminForm
#     list_display = ['question_text','question_type','form']
#     inlines = [OptionInline]

#     class Media:
#         js = ('templates/admin.js')

# @admin.register(Option)
# class OptionAdmin(admin.ModelAdmin):
#     list_display = ['option_text']     

# @admin.register(Response)
# class ResponseAdmin(admin.ModelAdmin):
#     list_display = ['question', 'short_response_text','long_response_text','multiple_choice_option']               

# admin.site.register(Form)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Option)
# admin.site.register(Response)

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class FormAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Response)



