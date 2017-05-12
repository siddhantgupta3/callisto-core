from wizard_builder.models import (
    QuestionPage, SingleLineText, Choice, MultipleChoice,
    Conditional, FormQuestion, PageBase
)
from django.test import TestCase


class InheritenceTest(TestCase):

    def test_question_page_instance(self):
        page = QuestionPage.objects.create()
        SingleLineText.objects.create(page_id=page.id)
        question = FormQuestion.objects.first()
        self.assertTrue(isinstance(question.page, QuestionPage))

    def test_page_form_question_set_instance(self):
        page = QuestionPage.objects.create()
        SingleLineText.objects.create(page=page)
        question = PageBase.objects.first().formquestion_set.first()
        self.assertTrue(isinstance(question.page, SingleLineText))

    def test_choice_multiple_choice_instance(self):
        page = QuestionPage.objects.create()
        question = MultipleChoice.objects.create(page=page)
        Choice.objects.create(question=question)
        choice = FormQuestion.objects.first()
        self.assertTrue(isinstance(choice.question, MultipleChoice))

    def test_choice_multiple_choice_instance(self):
        page = QuestionPage.objects.create()
        question = MultipleChoice.objects.create(page=page)
        Conditional.objects.create(question_id=question.id, page_id=page.id)
        condition = Conditional.objects.first()
        self.assertTrue(isinstance(condition.question, MultipleChoice))
        self.assertTrue(isinstance(condition.page, QuestionPage))
