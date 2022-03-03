from django.forms import ModelForm
from app.models import Member, Product


class MemberForm(ModelForm):
	class Meta:
		model = Member
		fields = ('name','email','age',)
class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ('name','description','prix','stock','image')
