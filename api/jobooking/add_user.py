from django.contrib.auth.models import User

user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
user.last_name = 'Lennon'

user.save()


user = User.objects.create_user('tom','tom@thebeatles.com', 'tompassword')
user.last_name = 'Stark'

user.save()
