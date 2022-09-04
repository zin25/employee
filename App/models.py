from django.db import models
from multiselectfield import MultiSelectField

SITUATION = (
  ('Pending', 'Pending'),
  ('Accepted', 'Accepted'),
  ('Declined', 'Declined'),
)

PERSONALITY = (
  ('', 'Select a personality'),
  ('i am outgoing', 'I am outgoing'),
  ('i am sociable', 'I am sociable'),
  ('i am antisocial', 'I am antisocial'),
  ('i am discreet', 'I am discreet'),
  ('i am serious', 'I am serious'),
)

SMOKER = (
  ('1', 'Yes'),
  ('2', 'No'),
)

# MultiselectField Checkbox
FRAMEWORKS = (
  ('Laravel', 'Laravel'),
  ('Angular', 'Angular'),
  ('Django', 'Django'),
  ('Flask', 'Flask'),
  ('Vue', 'Vue'),
  ('Others', 'Others'),
)

LANGUAGES = (
  ('Python', 'Python'),
  ('JavaScript', 'JavaScript'),
  ('Java','Java'),
  ('Golang', 'Golang'),
  ('C++)', 'C++)'),
  ('Others', 'Others'),
)

DATABASES = (
  ('MySql', 'MySql'),
  ('Postgree','Postgree'),
  ('MongoDB','MongoDB'),
  ('Sqlite','SQLite'),  
  ('Oracle','Oracle'),
  ('Others', 'Others'),
)

LIBRARIES = (
  ('Ajax', 'Ajax'),
  ('Jquery', 'Jquery'),
  ('React.js','React.js'),
  ('Keras','Keras'),
  ('Tensorflow','Tensorflow'),
  ('Others', 'Others'),
)

MOBILE = (
  ('React Native', 'React Native'),
  ('Ionic', 'Ionic'),
  ('Flutter', 'Flutter'),
  ('Kivy', 'Kivy'),
  ('Xamarin', 'Xamarin'),
  ('Others', 'Others'),
)

OTHERS = (
  ('UML','UML'),
  ('Firebase','Firebase'),
  ('Docker','Docker'),
  ('GIT','GIT'),
  ('GraphQL','GraphQL'),
  ('Others', 'Others'),
)

STATUS_COURSE = (
  ('','Select Your Status'),
  ("I'm studying","I'm studying"),
  ('I took a break','I took a break'),
  ('Completed','Completed'),
)

# Create your models here.
class Candidate(models.Model):
  #Personal Card 1
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  job = models.CharField(max_length=5, verbose_name='Job Code')
  #age = models.CharField(max_length=2)
  birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Birthday')
  phone = models.CharField(max_length=25)
  personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
  salary = models.CharField(max_length=50, verbose_name='Salary Expectation')
  gender = models.CharField(max_length=10)
  experience = models.BooleanField(null=True)
  smoker = models.CharField(max_length=10, choices=SMOKER, default="")
  email = models.CharField(max_length=50)
  message = models.TextField(verbose_name='Presentation')
  file = models.FileField(upload_to='resume', blank=True, verbose_name='Resume')
  image = models.ImageField(upload_to='photo', blank=True, verbose_name='Photo')
  created_at = models.DateTimeField(auto_now_add=True)
  Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
  company_note = models.TextField(blank=True)
  # MultiselectField Checkbox
  # SKills Card 2
  frameworks = MultiSelectField(choices=FRAMEWORKS)
  languages = MultiSelectField(choices=LANGUAGES)
  databases = MultiSelectField(choices=DATABASES)
  libraries = MultiSelectField(choices=LIBRARIES)
  mobile = MultiSelectField(choices=MOBILE)
  others = MultiSelectField(choices=OTHERS)

  # Education Card 3
  institution = models.CharField(max_length=50)
  course = models.CharField(max_length=50)
  started_course = models.DateField(auto_now=False, auto_now_add=False)
  finished_course = models.DateField(auto_now=False, auto_now_add=False)
  about_course = models.TextField()
  status_course = models.CharField(max_length=50, null=True, choices=STATUS_COURSE)

  # Professional Card 4
  company = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  started_job = models.DateField(auto_now=False, auto_now_add=False)
  finished_job = models.DateField(auto_now=False, auto_now_add=False)
  about_job = models.TextField()
  employed = models.BooleanField(null=True, verbose_name="I am Employed")
  remote = models.BooleanField(null=True, verbose_name="I agree to work remotly")
  travel = models.BooleanField(null=True, verbose_name="I'm avaliable for travel")

  def __str__(self):
    return self.firstname

# Capital latter name lastname
  def clean(self):
    self.firstname = self.firstname.capitalize()
    self.lastname = self.lastname.capitalize()

#Concatenate F-Name and L-name in admin
  def name(obj):
    return "%s %s" % (obj.firstname, obj.lastname)

# Concatenate join name in admin
  def __str__(self):
    return self.firstname + " " + self.lastname