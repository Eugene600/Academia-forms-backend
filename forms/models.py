from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    department = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class QuestionType(models.TextChoices):
    SHORT_PARAGRAPH = 'SHORT', 'Short Paragraph'
    LONG_PARAGRAPH = 'LONG', 'Long Paragraph'
    MULTIPLE_CHOICES = 'MULTIPLE', 'Multiple Choices'
    CHECKBOXES = 'CHECKBOX', 'Checkboxes'

class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    question_type = models.CharField(
        max_length=10,
        choices=QuestionType.choices,
        default=QuestionType.SHORT_PARAGRAPH
    )
    # Fields for options
    option_text = models.CharField(max_length=255, blank=True, null=True)
    option_values = models.ManyToManyField('Option', blank=True)

    def __str__(self):
        return self.question_text

class Option(models.Model):
    option_text = models.CharField(max_length=200)

    def __str__(self):
        return self.option_text

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Response data
    short_response_text = models.CharField(max_length=255, blank=True, null=True)
    long_response_text = models.TextField(blank=True, null=True)
    multiple_choice_option = models.ForeignKey(Option, blank=True, null=True, on_delete=models.CASCADE, related_name='multiple_choice_responses')
    checkbox_options = models.ManyToManyField(Option, blank=True, related_name='checkbox_responses')

    def get_response(self):
        if self.question.question_type == QuestionType.SHORT_PARAGRAPH:
            return self.short_response_text
        elif self.question.question_type == QuestionType.LONG_PARAGRAPH:
            return self.long_response_text
        elif self.question.question_type == QuestionType.MULTIPLE_CHOICES:
            return self.multiple_choice_option
        elif self.question.question_type == QuestionType.CHECKBOXES:
            return self.checkbox_options.all()
        return None
