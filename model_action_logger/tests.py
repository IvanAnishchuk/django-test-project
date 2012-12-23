from django.test import TestCase
from django_any import any_model
from account.models import Account
from model_action_logger.models import ActionNote
#from model_action_logger import signals


class NoteTest(TestCase):

    def test_create(self):
        obj = any_model(Account)
        count = ActionNote.objects.filter(
            app='account.models',
            model='Account',
            object_id=obj.id,
            note='created',
        ).count()
        self.assertTrue(count)

    def test_change(self):
        obj = any_model(Account)
        obj.jabber = 'test@test.com'
        obj.save()
        count = ActionNote.objects.filter(
            app='account.models',
            model='Account',
            object_id=obj.id,
            note='changed',
        ).count()
        self.assertTrue(count)

    def test_delete(self):
        obj = any_model(Account)
        obj_id = obj.id
        obj.delete()
        count = ActionNote.objects.filter(
            app='account.models',
            model='Account',
            object_id=obj_id,
            note='deleted',
        ).count()
        self.assertTrue(count)

