from django.shortcuts import render

# Create your views here.


from django.views import generic
from .models import Blog, UserProfile, Comment
from django.contrib.auth.models import User #Blog author or commenter


def index(request):
    return render(request,'index.html')
    

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

from django.shortcuts import get_object_or_404

class BlogByUserView(generic.ListView):
    model = Blog
    paginate_by = 5
    template_name ='blog/blogger_detail.html'
    
    def get_queryset(self):
        id = self.kwargs['pk']
        target_author=get_object_or_404(UserProfile, pk = id)
        return Blog.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        context = super(BlogByUserView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(UserProfile, pk = self.kwargs['pk'])
        return context
    
    

class BlogDetailView(generic.DetailView):
    model = Blog

    
class BloggerListView(generic.ListView):
    model = UserProfile
    paginate_by = 5
    template_name ='blog/blogger_list.html'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['description',]
    template_name = 'blog/comment_form.html'
    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self): 
        return reverse('blog_detail', kwargs={'pk': self.kwargs['pk'],})
