import os
os.environ.setdefault('DJANGO.SETTINGS.MODULE','first_project.settings')

import django

import random
from first_app.models import Topic,WebPage
from faker import Faker

fakegen=Faker()
topics=['Social','News','Market','Games']

def add_topic():
    t=Topic.objects,get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top=add_topic()
        furl=fakegen.url()
        fname=fakegen.company()

        webpg=WebPage.objects.get_or_create(topic=top,url=furl,name=fname)[0]

if __name__=='__main__':
    print('Populating')
    populate(20)
    print('Populating complete')