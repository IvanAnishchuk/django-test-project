# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActionNote'
        db.create_table('model_action_logger_actionnote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('app', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
        ))


    def backwards(self, orm):
        # Deleting model 'ActionNote'
        db.delete_table('model_action_logger_actionnote')


    models = {
        'model_action_logger.actionnote': {
            'Meta': {'object_name': 'ActionNote'},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['model_action_logger']
