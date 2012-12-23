# coding: utf-8
from django.db.models.signals import post_save, post_delete
from django.db.utils import DatabaseError
from django.dispatch import receiver
from django.utils.timezone import now
from model_action_logger.models import ActionNote
import logging

logger = logging.getLogger('model_action_logger')


@receiver(post_save, dispatch_uid='model_action_logger.signals.save')
def save_object(sender, **kwargs):
    if sender != ActionNote:
        if kwargs['created']:
            note = 'created'
        else:
            note = 'changed'
        instance = kwargs.get('instance')
        if instance:
            id = instance.id
        else:
            id = 0
        try:
            ActionNote.objects.create(
                datetime=now(),
                note=note,
                app=sender.__module__,
                model=sender.__name__,
                object_id=id,
            )
        except DatabaseError as e:  # Probably syncd
            if str(e) == 'no such table: model_action_logger_actionnote':
                logger.warning(
                    "no such table: model_action_logger_actionnote\n"
                    "probably, we're just in syncdb"
                )
            else:
                raise


@receiver(post_delete, dispatch_uid='model_action_logger.signals.delete')
def delete_object(sender, **kwargs):
    if sender != ActionNote:
        note = 'deleted'
        instance = kwargs.get('instance')
        if instance:
            id = instance.id
        else:
            id = 0
        try:
            obj = ActionNote.objects.create(
                datetime=now(),
                note=note,
                app=sender.__module__,
                model=sender.__name__,
                object_id=id,
            )
        except DatabaseError as e:  # Probably syncd
            if str(e) == 'no such table: model_action_logger_actionnote':
                logger.warning(
                    "no such table: model_action_logger_actionnote\n"
                    "probably, we're just in syncdb"
                )
            else:
                raise

