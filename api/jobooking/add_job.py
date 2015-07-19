from jobs.models import Job
from jobs.serializer import JobSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

job1 = Job(short_description="job short description 1", title="jobtitle1", price=15.99, charge_type=0,confirmation_time=1440,owner_id=1, category_id=1, images_id=1)
job1.save()


job2 = Job(short_description="job short description 2", title="jobtitle2", price=25.99, charge_type=0,confirmation_time=1440,owner_id=1, category_id=1, images_id=2)
job2.save()

job3 = Job(short_description="job short description 3", title="jobtitle3", price=5.99, charge_type=1,confirmation_time=120,owner_id=1, category_id=2, images_id=3)
job1.save()



