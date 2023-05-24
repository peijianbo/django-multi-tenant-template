# -*- coding:utf-8 -*-
from django.conf import settings
from django.core.management.commands.migrate import Command as DjangoCommand

from itom_project.libs.utils.tenant_util import TenantUtil


class Command(DjangoCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--database',
            required=True,
            help='Nominates a database to synchronize, Defaults to all databases.',
        )
        parser.add_argument(
            '--skip-checks', action='store_true',
            help='Skip system checks.',
        )
        parser.add_argument(
            'app_label', nargs='?',
            help='App label of an application to synchronize the state.',
        )
        parser.add_argument(
            'migration_name', nargs='?',
            help='Database state will be brought to the state after that '
                 'migration. Use the name "zero" to unapply all migrations.',
        )
        parser.add_argument(
            '--noinput', '--no-input', action='store_false', dest='interactive',
            help='Tells Django to NOT prompt the user for input of any kind.',
        )
        parser.add_argument(
            '--fake', action='store_true',
            help='Mark migrations as run without actually running them.',
        )
        parser.add_argument(
            '--fake-initial', action='store_true',
            help='Detect if tables already exist and fake-apply initial migrations if so. Make sure '
                 'that the current database schema matches your initial migration before using this '
                 'flag. Django will only check for an existing table name.',
        )
        parser.add_argument(
            '--plan', action='store_true',
            help='Shows a list of the migration actions that will be performed.',
        )
        parser.add_argument(
            '--run-syncdb', action='store_true',
            help='Creates tables for apps without migrations.',
        )
        parser.add_argument(
            '--check', action='store_true', dest='check_unapplied',
            help='Exits with a non-zero status if unapplied migrations exist.',
        )

    def handle(self, *args, **options):
        database = options['database']
        if database == 'all':
            self.stdout.write(self.style.SUCCESS("Nominates all database to synchronize:"))
            for d in settings.DATABASES:
                self.stdout.write(self.style.SUCCESS(f'Sync {d}:'))
                TenantUtil.set_current_tenant(d)
                options['database'] = d
                super().handle(*args, **options)
                TenantUtil.release_current_tenant()
        else:
            TenantUtil.set_current_tenant(database)
            super(Command, self).handle(*args, **options)
            TenantUtil.release_current_tenant()
