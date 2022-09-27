import os.path

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Заполнение базы данных из фикстур"
    fixtures_dir = 'fixtures'
    loaddata_command = 'loaddata'
    filenames = [
        'ads.json',
        'categories.json'
    ]

    def handle(self, *args, **kwargs):
        for fixtures_filename in self.filenames:
            call_command(self.loaddata_command, os.path.join(self.fixtures_dir, fixtures_filename))
