from flutemusic import *
from flutemusic.forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout_then_login, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext

def index(request):
	return list(request)

def list(request):
	if 'id' in request.GET.keys() and request.GET['id'] != None:
		return view_piece(request)
	if 'orderby' in request.GET.keys() and request.GET['orderby'] != None:
		try:
			items = Piece.objects.all().order_by(request.GET['orderby'])
		except:
			items = Piece.objects.all().order_by('composer','date_written','title')
	else:
		items = Piece.objects.all().order_by('composer','date_written','title')
	return render_to_response('list.html', {
		'PAGE_TITLE' : 'Flute Repertoire Database',
		'items' : items,
	}, RequestContext(request))

@login_required
def add(request,itype,page_title):
	success_item = None
	success = None
	errors = None
	if request.method == "POST":
		form = itype(request.POST, request.FILES)
		try:
			form.save()
			success = " saved succesfully."
			success_item = str(form.instance)
			form = itype()			
		except:
			errors = "One or more errors occurred while saving."
	else:
		form = itype()		
	return render_to_response('form.html', {
		'PAGE_TITLE' : page_title,
		'form' : form,
		'success' : success,
		'success_item' : success_item,
		'errors' : errors,
	}, RequestContext(request))


@login_required
def manage_db(request):
	return render_to_response('manage_db.html', {
		'PAGE_TITLE' : 'Manage Database',
	}, RequestContext(request))

def view_biblio(request):
	if 'id' in request.GET.keys() and request.GET['id'] != None:
		return view_biblio_item(request)
	items = Bibliography.objects.all()
	return render_to_response('biblio.html', {
		'PAGE_TITLE' : 'Bibliography',
		'items' : items,
	}, RequestContext(request))

def view_biblio_item(request):
	item_id = request.GET['id']
	item = Bibliography.objects.get(id=item_id)
	return render_to_response('view_biblio.html', {
		'PAGE_TITLE' : str(item),
		'item' : item,
	}, RequestContext(request))

# ==================
# = Add Item Views =
# ==================

def add_piece(request):
	return add(request,PieceForm,'Add Piece')

def add_composer(request):
	return add(request,ComposerForm,'Add Composer')

def add_instrumentation(request):
	return add(request,InstrumentationForm,'Add Instrumentation')

def add_category(request):
	return add(request,CategoryForm,'Add Category')

def add_biblio(request):
	return add(request,BiblioForm,'Add Bibliography')

def view_piece(request):
	item_id = request.GET['id']
	item = Piece.objects.get(id=item_id)
	return render_to_response('view_piece.html', {
		'PAGE_TITLE' : str(item),
		'item' : item,
	}, RequestContext(request))

def login_view(request):
	errors = None
	if request.method == "POST":
		if request.POST['username'] != '' and request.POST['password'] != '':
			user = authenticate(username=request.POST['username'],password=request.POST['password'])
			if user is not None:
				login(request,user)
				request.session['curruser'] = user
				if 'next' in request.GET.keys() and request.GET['next'] != None:
					return HttpResponseRedirect(request.GET['next'])
				else:
					return HttpResponseRedirect('/')
			else:
				errors = 'Invalid username or password.'
		else:
			errors = 'Username and password cannot be blank.'
	
	return render_to_response('login.html', {
		'PAGE_TITLE' : 'Login',
		'errors' : errors,
	}, RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def delete(request,itype,redirect):
	if 'id' in request.GET.keys() and request.GET['id'] != None:
		id = request.GET['id']
		item = itype.objects.get(id=id)
		item.delete()
		return HttpResponseRedirect(redirect)


def delete_piece(request):
	return delete(request,Piece,'/')

def delete_biblio(request):
	return delete(request,Bibliography,'/biblio/')

def searchModel(modelType,query):
	results = []
	modType = modelType.__name__
	for item in modelType.objects.all():
		for v in item.__dict__.values():
			try: 
				if str(query).lower() in str(v).lower():
					tup = [modType,item]
					if tup not in results:
						results.append(tup)
			except:
				pass
	results.sort()
	return results


def search(request):
	query = None
	results = []
	if 'q' in request.GET.keys() and request.GET['q'] != None:
		query = request.GET['q']
		results.extend(searchModel(Piece,query))
		results.extend(searchModel(Composer,query))
		results.extend(searchModel(Category,query))
		results.extend(searchModel(Instrumentation,query))
		results.extend(searchModel(Bibliography,query))
		results.sort()
					
	return render_to_response('search/search.html', {
		'PAGE_TITLE' : 'Search',
		'results' : results,
	}, RequestContext(request))

def composers(request):
	if 'id' in request.GET.keys() and request.GET['id'] != None:
		return view_composer(request)
	items = Composer.objects.all()
	return render_to_response('composers.html', {
		'PAGE_TITLE' : 'Composers',
		'items' : items,
	}, RequestContext(request))

def instrumentation(request):
	if 'id' in request.GET.keys() and request.GET['id'] != None:
		return view_instrumentation(request)
	items = Instrumentation.objects.all()
	return render_to_response('instrumentation.html', {
		'PAGE_TITLE' : 'Instrumentation',
		'items' : items,
	}, RequestContext(request))

def view_instrumentation(request):
	iid = request.GET['id']
	i = Instrumentation.objects.get(id=iid)
	return render_to_response('view_composer.html', {
		'PAGE_TITLE' : i,
		'c' : i,
	}, RequestContext(request))

def view_composer(request):
	cid = request.GET['id']
	c = Composer.objects.get(id=cid)
	return render_to_response('view_composer.html', {
		'PAGE_TITLE' : c,
		'c' : c,
	}, RequestContext(request))