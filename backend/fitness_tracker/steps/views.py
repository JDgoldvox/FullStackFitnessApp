from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Question, StepCount

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     try:
#         question = get_object_or_404(Question, pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def viewSteps(request, date):
    obj = StepCount.objects.get(day=date)
    data = {
        "day": obj.day,
        "steps": obj.steps,
        "goal": obj.goal
    }
    return JsonResponse(data)

@login_required
def addStep(request):
    template = loader.get_template("steps/addStep.html")

    return HttpResponse(template.render(None, request))

@login_required
def createStep(request):
    new_step = StepCount.objects.create(day=request.POST["day"], steps=request.POST["steps"], goal=request.POST["goal"])

    data = {
        "day": new_step.day,
        "steps": new_step.steps,
        "goal": new_step.goal
    }

    return JsonResponse(data)

