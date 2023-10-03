from django.shortcuts import render, redirect
from .models import Task
from .forms import todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

# class lviews(ListView):
#     model = Task
#     template_name ='task.html'
#     context_object_name = 'obj'

class dviews(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'


class uviews(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('dviews', kwargs={'pk': self.object.id})


class delviews(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy("task")


def task(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
    return render(request, 'task.html', {'obj1': obj1})


#
# def delete(request,tid):
#     task=Task.objects.get(id=tid)
#     if request.method=='POST':
#         task.delete()
#         return redirect('/')
#     return render(request,'delete.html',{'task':task})
#
# def update(request,id):
#     task=Task.objects.get(id=id)
#     form=todoforms(request.POST or None,instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'update.html',{'task':task ,'form':form})

# def detail(request,id):
#     i=Task.objects.get(id=id)
#     return render(request,'detail.html',{'i':i})
