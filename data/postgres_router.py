# -*- coding: utf-8 -*-
__author__ = 'yijingping'
class PostgresRouter(object):
    """
    A router to control all database operations on models in the
    postgres database.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read data models go to postgres.
        """
        if model._meta.app_label == 'data':
            return 'postgres'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write data models go to postgres.
        """
        if model._meta.app_label == 'data':
            return 'postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the data app is involved.
        """
        if obj1._meta.app_label == 'data' or \
           obj2._meta.app_label == 'data':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the data app only appears in the 'postgres'
        database.
        """
        if app_label == 'data':
            return db == 'postgres'
        return None