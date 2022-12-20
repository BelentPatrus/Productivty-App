from django.shortcuts import render, redirect
from tasks.models import task


def home(request):
    if request.method == 'POST':
        description = request.POST['description']
        taskdata = task(description=description)
        taskdata.save()

    tasksdata = task.objects.all()

    context = {
        'tasks': tasksdata
    }

    return render(request, "index.html", context)


def delete_event(request, event_id):
    event = task.objects.get(pk=event_id)
    event.delete()
    return redirect('home')
