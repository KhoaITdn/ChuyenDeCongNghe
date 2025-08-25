from django.core.management.base import BaseCommand, CommandError
from myapp.models import Entry

class Command(BaseCommand):
    help = 'Closes the specified entry for further modifications'

    def add_arguments(self, parser):
        parser.add_argument('entry_ids', nargs='+', type=int)
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete entry instead of closing it',
        )

    def handle(self, *args, **options):
        for entry_id in options['entry_ids']:
            try:
                entry = Entry.objects.get(pk=entry_id)
            except Entry.DoesNotExist:
                raise CommandError(f'Entry "{entry_id}" does not exist')

            if options['delete']:
                entry.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted entry "{entry_id}"'))
            else:
                entry.is_open = False
                entry.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully closed entry "{entry_id}"'))