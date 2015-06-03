from jobs.models import Job
from jobs.serializer import JobSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

job1 = Job(job_reference="jobref1",job_title="jobtitle1",job_cost = 15.99, owner_id = 1)
job1.save()


job2 = Job(job_reference="jobref2",job_title="jobtitle2",job_cost = 16.99, owner_id = 2)
job2.save()


job3 = Job(job_reference="jobref3",job_title="jobtitle3",job_cost = 17.99, owner_id = 1)
job3.save()


