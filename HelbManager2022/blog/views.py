from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


from .models import Post
from .models import Task, Subtask
from django.views.generic.edit import UpdateView

from .forms import TaskForm, SubtaskForm

def home(request):
    context = {              # dictionnaire qui contient la liste des post qu'on veut passer
        'posts': Post.objects.all()
        }
    return render(request, 'blog/home.html', context)       # Objet context va etre accessible dans notre template


def status(request):
    context = {              # dictionnaire qui contient la liste des post qu'on veut passer
        'tasks': Task.objects.all(),
        'subtasks' : Subtask.objects.all(),
        'posts': Post.objects.all()
    }
    return render(request, 'blog/status.html', context)       # Objet context va etre accessible dans notre template


def post_detail(request):
    posts = Post.objects.filter(author=request.user)
    tasks = Task.objects.filter(post__in=posts)
    subtasks = Subtask.objects.filter(post__in=posts)
    context = {'posts': posts, 'tasks': tasks, 'subtasks': subtasks}

    return render(request, 'blog/post_detail.html', context)

# __________________ TASK VIEWS __________________________#

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'blog/listTask.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'blog/detailTask.html', {'task': task})

def task_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.post = post  # spécifiez le post associé à la tâche ici
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'blog/post_task.html', {'form': form})


def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task-list')

# __________________ SUBTASK VIEWS __________________________#

def subtask_list(request):
    subtasks = Subtask.objects.all()
    return render(request, 'blog/listSubtask.html', {'subtasks': subtasks})

def subtask_detail(request, subtask_id):
    subtask = Subtask.objects.get(id=subtask_id)
    return render(request, 'blog/detailSubtask.html', {'subtask': subtask})

def subtask_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = SubtaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.post = post  # spécifiez le post associé à la tâche ici
            subtask.save()
            return redirect('subtask-list')
    else:
        form = TaskForm()
    return render(request, 'blog/post_subtask.html', {'form': form})

def subtask_delete(request, subtask_id):
    subtask = Subtask.objects.get(id=subtask_id)
    subtask.delete()
    return redirect('subtask-list')
    
#________________________________________________________________#

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Django convention <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8

class PostListViewStatus(ListView):
    model = Post
    template_name = 'blog/status.html'  # Django convention <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'     # Django convention <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter()
        context['subtasks'] = Subtask.objects.all()

        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','collaborators', 'deadline']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','collaborators', 'deadline', 'project_finished']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})


