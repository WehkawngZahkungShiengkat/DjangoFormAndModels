import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level2_project.settings')

import django
django.setup()

import random
from L2prac_app.models import Uinfo
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_fn = fake_name[0]
        fake_ln = fake_name[1]
        fake_email = fakegen.email()


        user = Uinfo.objects.get_or_create(fname=fake_fn,lname=fake_ln,
                                            umail=fake_email)[0]


if __name__ == '__main__':
    print("populating data")
    populate(20)
    print("populating complete")
