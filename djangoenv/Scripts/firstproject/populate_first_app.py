import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
# Import settings
django.setup()

import random
from first_app.models import Topic,WebPage,AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top=add_topic()
        furl=fakegen.url()
        fname=fakegen.company()
        fdate=fakegen.date()

        webpg=WebPage.objects.get_or_create(topic=top,url=furl,name=fname)[0]
        accrec=AccessRecord.objects.get_or_create(name=webpg,date=fdate)[0]

if __name__=='__main__':
    print('Populating')
    populate(20)
    print('Populating complete')