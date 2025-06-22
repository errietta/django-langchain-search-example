from django.core.management.base import BaseCommand
from job.models import Job
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the Job model with fake data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of jobs to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']
        for _ in range(count):
            Job.objects.create(
                title=fake.job(),
                description=fake.paragraph(nb_sentences=5),
                company=fake.company(),
                location=fake.city(),
                salary=fake.random_number(digits=5, fix_len=True),
                is_active=fake.boolean(),
                apply_link=fake.url(),
                company_size_choice=fake.random_element(elements=['SMALL', 'MEDIUM', 'LARGE', 'ENTERPRISE']),
                remote=fake.random_element(elements=['REMOTE', 'ONSITE', 'HYBRID']),
            )
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} fake jobs.'))
