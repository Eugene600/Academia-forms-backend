# from django import forms
# from django.contrib import admin
# # from .models import Question, Option, QuestionType, ShortResponse, LongResponse, MultipleChoiceResponse, CheckboxResponse

# # class OptionInline(admin.TabularInline):
# #     model = Option
# #     extra = 1

# # class QuestionAdminForm(forms.ModelForm):
# #     class Meta:
# #         model = Question
# #         fields = '__all__'
    
# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         question_type = self.instance.question_type
# #         if question_type in [QuestionType.MULTIPLE_CHOICES, QuestionType.CHECKBOXES]:
# #             self.fields['options'] = forms.ModelMultipleChoiceField(
# #                 queryset=Option.objects.filter(question=self.instance),
# #                 widget=forms.CheckboxSelectMultiple
# #             )
# #         elif question_type == QuestionType.SHORT_PARAGRAPH:
# #             self.fields['response_text'] = forms.CharField(max_length=255)
# #         elif question_type == QuestionType.LONG_PARAGRAPH:
# #             self.fields['response_text'] = forms.CharField(widget=forms.Textarea)

# # class QuestionAdmin(admin.ModelAdmin):
# #     form = QuestionAdminForm
# #     inlines = [OptionInline]
# #     list_display = ('question_text', 'question_type')
    
# #     def save_formset(self, request, form, formset, change):
# #         instances = formset.save(commit=False)
# #         for instance in instances:
# #             instance.question = form.instance
# #             instance.save()
# #         formset.save_m2m()

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Option)
# admin.site.register(ShortResponse)
# admin.site.register(LongResponse)
# admin.site.register(MultipleChoiceResponse)
# admin.site.register(CheckboxResponse)
