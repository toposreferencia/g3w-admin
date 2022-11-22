# coding=utf-8
""""

Keycloack app config

.. note:: This program is free software; you can redistribute it and/or modify
          it under the terms of the Mozilla Public License 2.0.

"""

__author__ = 'elpaso@itopen.it'
__date__ = '2021-10-19'
__copyright__ = 'Copyright 2021, Gis3W'


from django.apps import AppConfig
import os


class KeycloackConfig(AppConfig):
    name = 'keycloack'
    verbose_name = "keycloack"

    def ready(self):
        from django.conf import settings
        settings.TEMPLATES[0]['DIRS'].insert(
            0, os.path.join(os.path.dirname(__file__), 'templates'))

        settings.AUTHENTICATION_BACKENDS = list(
            settings.AUTHENTICATION_BACKENDS)
        settings.AUTHENTICATION_BACKENDS.append(
            'keycloack.overrides.oidc_auth_backend.KeyCloackAB')
        settings.AUTHENTICATION_BACKENDS.append(
            'keycloack.bearer_auth_backend.KeycloackBearerAB')
