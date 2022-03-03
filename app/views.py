from itertools import product
from django.shortcuts import render
from django.http import HttpResponse,response,Http404,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Product
from django.utils import timezone
from app.forms import MemberForm

# def index(request):
#     Question = Question.objects.all().order_by('id')
#     return render(request,'app/index.html',{'Questions':Question})

# Create your views here.


from django.views.generic import ListView #ajouter à


#liste
def index(request):
    products = Product.objects.all().order_by('id') #Obtenez de la valeur
    return render(request, 'app/index.html', {'products':products}) #Passer une valeur au modèle
    
#Liste (ajoutée pour la nation de la page)
class MemberList(ListView):
	model = Member #Modèle à utiliser
	context_object_name='products' #Paramètre de nom d'objet (la valeur par défaut est object_Ça devient une liste)
	template_name='app/index.html' #Spécifier une page de modèle
	paginate_by = 1 #Nombre de pages par page
    
#Nouveau et modifier
def edit(request, id=None):

	if id: #Lorsqu'il y a un identifiant (lors de l'édition)
		#Rechercher par identifiant et renvoyer les résultats ou erreur 404
		product = get_object_or_404(Product, pk=id)
	else: #Quand il n'y a pas d'identifiant (quand neuf)
		#Créer un membre
		product = Product()

	#Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
	if request.method == 'POST':
		#Générer un formulaire
		form = MemberForm(request.POST, instance=member)
		if form.is_valid(): #Enregistrer si la validation est OK
			member = form.save(commit=False)
			member.save()
			return redirect('app:index')
	else: #Au moment de GET (générer un formulaire)
		form = MemberForm(instance=member)
	
	#Afficher un nouvel écran / modifier l'écran
	return render(request, 'app/edit.html', dict(form=form, id=id))
#Effacer
#Détails (bonus)
#Détails (bonus)
def detail(request, id=None):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'app/detail.html', {'product':product})

def delete(request, id):
	# return HttpResponse("Effacer")
	member = get_object_or_404(Member, pk=id)
	member.delete()
	return redirect('app:index')

def chat(request, id=None):
    #member = get_object_or_404(Member, pk=id)
    return render(request, 'app/chat.html')