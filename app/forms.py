from dataclasses import fields
from pyexpat import model
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

class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('stock',)