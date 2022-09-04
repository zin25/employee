from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date
import datetime

# Every latters to lowercase
class Lowercase(forms.CharField):
  def to_python(self, value):
    return value.lower()

# To UpperCase
class Uppercase(forms.CharField):
  def to_python(self, value):
    return value.upper()

class CandidateForm(forms.ModelForm):

  #Valdations
  #First Name Capital first
  firstname = forms.CharField(
    label='First Name', min_length=3, max_length=50, 
    validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
    message="Only letters bro")],
    widget=forms.TextInput(attrs={
      'placeholder': 'First Name',
      'style': 'font-size: 13px; text-transform: capitalize'
      })
  )
  #last name capitalize
  lastname = forms.CharField(
    label='Last Name', min_length=3, max_length=50, 
    validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
    message="Only letters bro")],
    widget=forms.TextInput(attrs={
      'placeholder': 'Last Name',
      'style': 'font-size: 13px; text-transform: capitalize'
      })
  )
  #job uppercase
  job = Uppercase(
    label= 'Job Code',
    min_length=5, max_length=5,
    widget=forms.TextInput(attrs={
      'placeholder': 'Example: FR-22',
      'style': 'font-size: 13px; text-transform: uppercase',
      'data-mask': 'AA-00'
    })
  )
  #email lowercase
  email = Lowercase(
    label='Email Address', min_length=8, max_length=50, 
    validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
    message="Type Valid Email Address!")],
    widget=forms.TextInput(attrs={
      'placeholder': 'Email',
      'style': 'font-size: 13px; text-transform: lowercase'
    })
  )
  #age
  # age = forms.CharField(
  #   label='Your Age', min_length=2,
  #   validators=[RegexValidator(r'^[0-9]*$', 
  #   message="Input number and digits must 2")],
  #   widget=forms.TextInput(attrs={
  #     'placeholder': 'Age',
  #     'style': 'font-size: 13px'
  #     })
  # )
  #experience
  experience = forms.BooleanField(label='Experience', required=False)
  #message
  message = forms.CharField(
    label='About You', min_length=50, max_length=1000, 
    widget=forms.Textarea(
      attrs={
        'placeholder': 'Writte a little about yourself', 
        'rows': 6,
        'style':'font-size: 13px'
        }
      ),
  )

  # File Upload
  file = forms.FileField(
    label= 'Resume',
    widget=forms.ClearableFileInput(
      attrs={
        'style':'font-size: 13px',
        #'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document'
      }
    )
  )

  # Image Upload
  image = forms.FileField(
    label= 'Photo',
    widget=forms.ClearableFileInput(
      attrs={
        'style':'font-size: 13px',
        'accept': 'image/jpeg, image/png'
      }
    )
  )

  # Institution
  institution = forms.CharField(
    label='Institution',
    min_length=3,
    max_length=50,
    widget=forms.TextInput(attrs= {
      'style': 'font-size: 13px',
      'placeholder': 'Institution name',
    })
  )

  # Collage course
  course = forms.CharField(
    min_length=3,
    max_length=50,
    widget=forms.TextInput(attrs= {
      'style': 'font-size: 13px',
      'placeholder': 'Your collage course',
    }),
  )

  #about collage course
  about_course = forms.CharField(
    label='About You collage course', min_length=50, max_length=1000, 
    widget=forms.Textarea(
      attrs={
        'placeholder': 'Writte a little about your course', 
        'rows': 7,
        'style':'font-size: 13px'
        }
      ),
  )

  #about collage course
  about_job = forms.CharField(
    label='About You last job', min_length=50, max_length=1000, 
    widget=forms.Textarea(
      attrs={
        'placeholder': 'Tell us a little about what you did at the company...', 
        'rows': 7,
        'style':'font-size: 13px'
        }),
  )

  #Company (Last Company)
  company = forms.CharField(
    label = 'Last Company',
    min_length=3,
    max_length=50,
    widget=forms.TextInput(
      attrs={
        'placeholder': 'Company Name', 
        'rows': 7,
        'style':'font-size: 13px'
        }),
  )

  #Position
  position = forms.CharField(
    min_length=3,
    max_length=50,
    widget=forms.TextInput(
      attrs={
        'placeholder': 'Your occopation', 
        'rows': 7,
        'style':'font-size: 13px'
        }),
  )

  #Employed
  employed = forms.BooleanField(label= 'I am employed', required=False)
  remote = forms.BooleanField(label= 'I agree to remotely', required=False)
  travel = forms.BooleanField(label= "I'm available for travel", required=False)

  class Meta:
    model = Candidate
    exclude = ['created_at', 'Situation']
    #Label control
    labels = {
     'started_course':'Started',
     'finished_course':'Finished',
     'started_job':'Started',
     'finished_job':'Finished',
    }

    SALARY = (
      ('', 'Salary expectation (month)'),
      ('(Rp. 3.000.000 and Rp. 4.000.000)','(Rp. 3.000.000 and Rp. 4.000.000)'),
      ('(Rp. 5.000.000 and Rp. 6.000.000)','(Rp. 5.000.000 and Rp. 6.000.000)'),
      ('(Rp. 7.000.000 and Rp. 8.000.000)','(Rp. 7.000.000 and Rp. 8.000.000)'),
      ('(Rp. 9.000.000 and Rp. 10.000.000)','(Rp. 9.000.000 and Rp. 10.000.000)'),
    )

    # Gender Method
    GENDER = [('M', 'Male'),('F', 'Female')]

    #Outside Widget
    widgets = {
      #Birthday
      'birth': forms.DateInput(
        attrs={
          'style': 'font-size: 13px; cursor: pointer',
          'type': 'date',
          'onkeydown': 'return false', # Block typing 
          'min': '1950-01-01',
          'max': '2030-01-01',
        }
      ),

      #Started course
      'started_course': forms.DateInput(
        attrs={
          'style': 'font-size: 13px; cursor: pointer',
          'type': 'date',
          'onkeydown': 'return false', # Block typing 
          'min': '1950-01-01',
          'max': '2030-01-01',
        }
      ),

      #finished_course
      'finished_course': forms.DateInput(
        attrs={
          'style': 'font-size: 13px; cursor: pointer',
          'type': 'date',
          'onkeydown': 'return false', # Block typing 
          'min': '1950-01-01',
          'max': '2030-01-01',
        }
      ),

      #started_job
      'started_job': forms.DateInput(
        attrs={
          'style': 'font-size: 13px; cursor: pointer',
          'type': 'date',
          'onkeydown': 'return false', # Block typing 
          'min': '1950-01-01',
          'max': '2030-01-01',
        }
      ),

      #finished_job
      'finished_job': forms.DateInput(
        attrs={
          'style': 'font-size: 13px; cursor: pointer',
          'type': 'date',
          'onkeydown': 'return false', # Block typing 
          'min': '1950-01-01',
          'max': '2030-01-01',
        }
      ),

      #Phone
      'phone': forms.TextInput(
        attrs={
          'style':'font-size: 13px',
          'placeholder': 'Phone Number',
          'data-mask': '(+00)0000000000000'
        }
      ),
      #salary
      'salary': forms.Select(
        choices=SALARY,
        attrs={
            'class':'form-control',
            'style':'font-size: 13px'
        }
      ),
      'gender': forms.RadioSelect(choices=GENDER, attrs={'class':'btn-check'}),
      'smoker': forms.RadioSelect(choices=SMOKER, attrs={'class':'btn-check'}),
      'personality': forms.Select(attrs={'style':'font-size: 13px'}),
      'status_course': forms.Select(attrs={'style':'font-size: 13px'}),
    }

    #Super Func
    def __init__(self, *args, **kwargs):
      super(CandidateForm, self).__init__(*args, **kwargs)

      # Disable all inputs (By: ID/PK)
      # instance = getattr(self, 'instance', None)
      # array = ['experience', 'gender', 'firstname', 'lastname', 'job', 'email', 'phone', 'salary', 'birth', 'personality', 'smoker', 'file', 'image', 'frameworks', 'languages', 'databases', 'libraries', 'mobile', 'others', 'message', 'status_course','started_course', 'finished_course', 'course', 'institution', 'about_course', 'started_job','finished_job', 'company', 'position', 'about_job', 'employed', 'remote', 'travel']
      # for field in array:
      #   if instance and instance.pk:
      #     self.fields[field].disabled = True

      #Control Panel, Method for Control
      #Input required
      

      # Select Options
      #self.fields["personality"].choices = [('', 'Select a personality'),] + list(self.fields["personality"].choices)[1:]


      #Widget Control
      #self.fields['phone'].widget.attrs.update({'style':'font-size: 18px', 'placeholder': 'Number Phone'})
   
   # Disable all inputs (By: ID/PK)

   
    #End Super Func

    #Function To Prevent Duplicates
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if Candidate.objects.filter(email=email).exists():
      raise forms.ValidationError('Denied !{} is already used by another candidate.'.format(email))
    return email

    # Job COde
  def clean_job(self):
    job = self.cleaned_data.get('job')
    if job == 'FR-22' or job == 'BA-10' or job == 'FU-15':
      return job
    else:
      raise forms.ValidationError('This code is invalid')

    #Age
  # def clean_age(self):
  #   age = self.cleaned_data.get('age')
  #   if age < '18' or age > '40':
  #     raise forms.ValidationError('Age must be between 18 and 40')
  #   return age

    #Phone
  def clean_phone(self):
    phone = self.cleaned_data.get('phone')
    if len(phone) <= 15:
      raise forms.ValidationError('Phone must be at least 10 characters long')
    return phone

    # Image max 2MB
    # Image Upload
  def clean_image(self):
    image = self.cleaned_data.get('image')
    if image.size > 2 * 1048476:
      raise forms.ValidationError('maximum allowed is 2mb')
    return image

  def clean_birth(self):
    birth = self.cleaned_data.get('birth')
    #variable
    b = birth
    now = date.today()
    age = (now.year - b.year) - ((now.month, now.day) < (b.month, b.day))
    #Statement
    if age < 18 or age > 65:
      raise forms.ValidationError('age must be between 18 and 65')
    return birth

    #A Collage Start course
  def clean_started_course(self):
    started_course = self.cleaned_data.get('started_course')
    if started_course > datetime.date.today():
      raise forms.ValidationError('Future Date is invalid')
    return started_course

  def clean_finished_course(self):
    finished_course = self.cleaned_data.get('finished_course')
    if finished_course > datetime.date.today():
      raise forms.ValidationError('Future Date is invalid')
    return finished_course

    #Job Started and End
  def clean_started_job(self):
    started_job = self.cleaned_data.get('started_job')
    if started_job > datetime.date.today():
      raise forms.ValidationError('Future Date is invalid')
    return started_job

  def clean_finished_job(self):
    finished_job = self.cleaned_data.get('finished_job')
    if finished_job > datetime.date.today():
      raise forms.ValidationError('Future Date is invalid')
    return finished_job

  