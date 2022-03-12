from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, modelformset_factory
from django.forms import ModelForm

from quiz.models import Choice, Question


class ChoicesInlineFormset(BaseInlineFormSet):
    def clean(self):
        # lst = []
        # for form in self.forms:
        #     if form.cleaned_data['is_correct']:
        #         lst.append(1)
        #     else:
        #         lst.append(0)

        num_correct_answers = sum([form.cleaned_data['is_correct'] for form in self.forms])

        # num_correct_answers = sum(lst)

        if num_correct_answers == 0:
            raise ValidationError('Необходимо выбрать как минимум 1 вариант')

        if num_correct_answers == len(self.forms):
            raise ValidationError('Не разрешено выбирать все варианты')


class QuestionInlineFormSet(BaseInlineFormSet):
    def clean(self):
        if not (self.instance.QUESTION_MIN_LIMIT <= len(self.forms) <= self.instance.QUESTION_MAX_LIMIT):
            raise ValidationError(
                f'Кол-во вопросов должно быть в диапазоне от {self.instance.QUESTION_MIN_LIMIT} до '
                f'{self.instance.QUESTION_MAX_LIMIT} включительно'
            )

        order_num_lst = [question.cleaned_data['order_num'] for question in self.forms]

        if min(order_num_lst) != 1:
            raise ValidationError(
                'Номера вопросов должны начинаться с первого'
            )

        if max(order_num_lst) > len(self.forms):
            raise ValidationError(
                'Номер вопроса не должен превышать кол-во вопросов в тесте'
            )

        if len(set(order_num_lst)) != len(self.forms):
            raise ValidationError(
                'Номера вопросов должны следовать один за другим и не должны повторяться'
            )


class ChoiceForm(ModelForm):
    is_selected = forms.BooleanField(required=False)

    class Meta:
        model = Choice
        fields = ['text', ]


ChoicesFormSet = modelformset_factory(
    model=Choice,
    form=ChoiceForm,
    extra=0
)
