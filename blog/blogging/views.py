# Create your views here.from django.shortcuts import render_to_response
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from blogging.models import Post, Author
 
def index(request):
    all_posts = Post.objects.all().order_by('-date')
    template_data = {'posts' : all_posts}
 
    return render_to_response('index.html', template_data)