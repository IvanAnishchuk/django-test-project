# coding: utf-8
from django.core.management.base import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):

    def handle(self, *args, **options):

        for model in get_models():
            print (
                '{model._meta.app_label}'
                '.{model._meta.module_name}'
            ).format(model=model), model.objects.all().count()
