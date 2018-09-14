import csv , sys , os

project_dir="E:\amit\Interview_Preparation\Python\Django\website\website"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'

import django

django.setup()

from webapp.models import employees

data= csv.reader(open("E:\\amit\\Interview_Preparation\\Python\\Django\\website\\webapp\\data.csv"),delimiter=",")

for row in data:
    if row[0]!='firstname':
        post = employees()
        post.firstname=row[0]
        post.lastname = row[1]
        post.emp_id = row[2]
        post.save()

