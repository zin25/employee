from django.contrib import admin
from .models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html

class CandidateAdmin(admin.ModelAdmin):
  radio_fields = {"smoker": admin.HORIZONTAL}
  form = CandidateForm
  exclude = ['status']
  list_filter = ['Situation']
  list_display = ['name', 'job', 'email', 'created_at', 'status', '_']
  search_fields = ['firstname', 'lastname', 'email', 'Situation']
  list_per_page = 10

  #Read Only field
  readonly_fields = ['experience', 'gender', 'firstname', 'lastname', 'job', 'email', 
  'phone', 'salary', 'birth', 'personality', 'smoker', 'file', 'image', 'frameworks', 
  'languages', 'databases', 'libraries', 'mobile', 'others', 'message', 'status_course',
  'started_course', 'finished_course', 'course', 'institution', 'about_course', 'started_job',
  'finished_job', 'company', 'position', 'about_job', 'employed', 'remote', 'travel']

  #Fieldset
  fieldsets = [
    # HR Operations
    ("HR OPERATIONS", {"fields": ['Situation', 'company_note']}),
    # Personal
    ("Personal", {"fields": ['experience', 'gender', 'job', 'email', 'phone', 
    'salary', 'birth', 'personality', 'smoker', 'file', 'image', 'message']}),
    #Skills
    ("Skills", {"fields": ['frameworks', 'languages', 'databases', 'libraries', 'mobile', 'others']}),
    #Education
    ("Education", {"fields": ['status_course', 'started_course', 'finished_course', 
    'course', 'institution', 'about_course']}),
    #Professional
    ("Professional", {"fields": ['started_job', 'finished_job', 'company', 'position', 
    'about_job']}),
    #Note
    ("Note", {"fields": ['employed', 'remote', 'travel']}),
  ]

  #func to hide name 
  def get_fields(self, request, obj = None):
    fields = super().get_fields(request, obj)
    if obj:
      fields.remove('firstname')
      fields.remove('lastname')
    return fields

  # Function to change the icon
  def _(self, obj):
    if obj.Situation == 'Accepted':
      return True
    elif obj.Situation == 'Pending':
      return None
    else:
      return False
  _.boolean = True

  # Func to color the text
  def status(self, obj):
    if obj.Situation == 'Accepted':
      color = '#28a745'
    elif obj.Situation == 'Pending':
      color = '#fea95e'
    else:
      color = 'red'
    return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.Situation))
  status.allow_tags = True

admin.site.register(Candidate, CandidateAdmin)