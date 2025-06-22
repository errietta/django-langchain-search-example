from django.core.management.base import BaseCommand
from job.models import School
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the School model with fake data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of schools to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']
        for _ in range(count):
            School.objects.create(
                name=fake.company() + ' School',
                address=fake.address(),
                city=fake.city(),
                website=fake.url(),
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} fake schools.'))
