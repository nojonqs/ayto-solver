from django.http import HttpResponse, HttpRequest, HttpResponseNotModified
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

import frontend.solver
from frontend.models import Person, Male, Female, NoMatch, PerfectMatch, BaseMatch


class MaleCreateView(CreateView):
    model = Male
    template_name = "person_create.html"
    success_url = reverse_lazy("person_overview")
    fields = ("name",)


class FemaleCreateView(CreateView):
    model = Female
    template_name = "person_create.html"
    success_url = reverse_lazy("person_overview")
    fields = ("name",)


class PersonOverview(ListView):
    model = Person
    template_name = "person_overview.html"
    context_object_name = "person_list"

    def get_queryset(self):
        return Person.objects.get_queryset()


class PersonDeleteView(DeleteView):
    model = Person
    template_name = "person_delete.html"
    success_url = reverse_lazy("person_overview")


class NoMatchCreateView(CreateView):
    model = NoMatch
    template_name = "match_create.html"
    success_url = reverse_lazy("match_overview")
    fields = ("male", "female")


class PerfectMatchCreateView(CreateView):
    model = PerfectMatch
    template_name = "match_create.html"
    success_url = reverse_lazy("match_overview")
    fields = ("male", "female")


class MatchOverview(ListView):
    model = BaseMatch
    context_object_name = "match_list"
    template_name = "match_overview.html"

    def get_queryset(self):
        return BaseMatch.objects.all()


class MatchDeleteView(DeleteView):
    model = BaseMatch
    template_name = "match_delete.html"
    success_url = reverse_lazy("match_overview")


def reset(request: HttpRequest, *args, **kwargs):
    print(request.build_absolute_uri())
    for m in BaseMatch.objects.all():
        m.delete()
    for p in Person.objects.all():
        p.delete()
    return HttpResponseNotModified()


def solve_matches(*args, **kwargs):
    people = Person.objects.all()
    matches = BaseMatch.objects.all()
    possibilities = frontend.solver.solve(people, matches)
    msg = f"<p>amount: {len(possibilities)}</p>"
    for possibility in possibilities:
        msg += f"<p>{possibility}</p>"
    return HttpResponse(msg)
