from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CreateCustomUserForm(UserCreationForm):
  class Meta(UserCreationForm):
      model = CustomUser
      fields = (
        'username', 
        'email',
        'first_name',
        'last_name',
        )

class EditCustomUserForm(UserChangeForm):
  class Meta:
      model = CustomUser
      fields = (
        'username', 
        'email',
        'first_name',
        'last_name',
        )