from jobooker.models import Jobooker
from jobooker.serializer import JobookerSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

jobooker = Jobooker(firstName = "test_user2", owner_id=2)
jobooker.save()

jobooker2 = Jobooker(firstName = "test_user3", owner_id=1)
jobooker2.save()
