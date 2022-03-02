from django.forms import ModelForm
from app.models import Member


class MemberForm(ModelForm):
	class Meta:
		model = Member
		fields = ('name','email','age',)
