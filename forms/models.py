from django import forms
from django.db import models
from django.core.validators import MinLengthValidator


class Form(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=200)
    contact = models.CharField(
        max_length=10,     
        validators=[MinLengthValidator(10)],
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class QuestionType(models.TextChoices):
    SHORT_PARAGRAPH = 'SHORT', 'Short Paragraph'
    LONG_PARAGRAPH = 'LONG', 'Long Paragraph'
    MULTIPLE_CHOICES = 'MULTIPLE', 'Multiple Choices'
    CHECKBOXES = 'CHECKBOX', 'Checkboxes'

class Question(models.Model):
    FORMATS = (
        ('short_answer', 'Short Answer'),
        ('long_answer', 'Long Answer'),
        ('single_choice', 'Single Choice'),
        ('multiple_choice', 'Multiple Choice'),
    )
    form = models.ForeignKey(Form,related_name='questions' ,on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(
        max_length=20,
        choices=FORMATS
    )
    # Fields for options

    def __str__(self):
        return self.question_text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options',on_delete=models.CASCADE)
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #will add user later
    
    
#This is a custom admin forms to handle the conditional display of fields based on the question type selected
#Learning purposes, to be deleted later
# class QuestionAdminForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['form', 'question_text', 'question_type', 'option_text', 'option_values']
#         #Just learnt about these two, will use later
#         # labels = {"first_name": "First Name","last_name": "Last Name",}
#         # widgets = {"first_name": forms.TextInput(attrs={"class": "my-class"}),"last_name": forms.Textarea(attrs={"rows": 4, "cols": 15}),}


#         def __init__(self, *args, **kwargs):
#             super().__init__(*args,**kwargs)

#             self.fields['option_text'].widget = forms.HiddenInput()
#             self.fields['option_values'].widget = forms.HiddenInput()

#             if self.instance.pk:
#                 if self.instance.question_type in [QuestionType.MULTIPLE_CHOICES, QuestionType.CHECKBOXES]:
#                     self.fields['option_values'].widget = forms.CheckboxSelectMultiple()
#                 else:
#                     self.fields['option_text'].widget = forms.HiddenInput()
#                     self.fields['option_values'].widget = forms.HiddenInput()

