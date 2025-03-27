import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    completed = django_filters.BooleanFilter()
    due_date = django_filters.DateFromToRangeFilter() 
    priority = django_filters.ChoiceFilter(choices=Task.PRIORITY_CHOICES)
    user = django_filters.NumberFilter(field_name="user__id")

    class Meta:
        model = Task
        fields = ['name', 'completed', 'due_date', 'priority', 'user']

