from jobooker.models import Jobooker
from jobooker.serializer import JobookerSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

jobooker = Jobooker(firstName = "Danny")
jobooker.save()
serializer = JobookerSerializer(jobooker)
serializer.data

content = JSONRenderer().render(serializer.data)
content


from django.utils.six import BytesIO
stream = BytesIO(content)
data = JSONParser().parse(stream)
serializer = JobookerSerializer(data=data)


