from django.core.management.base import BaseCommand, CommandError
from myapp.models import Person  # chỉnh lại tên app và model cho đúng

class Command(BaseCommand):
    help = 'Example command: update or delete Persons by id'

    def add_arguments(self, parser):
        # Nhận một hoặc nhiều id của Person
        parser.add_argument('person_ids', nargs='+', type=int)

        # Tùy chọn để delete thay vì cập nhật
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete persons instead of updating',
        )

    def handle(self, *args, **options):
        for person_id in options['person_ids']:
            try:
                person = Person.objects.get(pk=person_id)
            except Person.DoesNotExist:
                raise CommandError(f'Person with id {person_id} does not exist.')

            if options['delete']:
                person.delete()
                self.stdout.write(self.style.SUCCESS(f'Deleted Person {person_id}'))
            else:
                # Ví dụ cập nhật trường first_name, last_name (chỉnh hoặc bỏ tùy yêu cầu)
                person.first_name = person.first_name + '_updated'
                person.save()
                self.stdout.write(self.style.SUCCESS(f'Updated Person {person_id}'))
