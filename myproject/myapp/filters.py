import django_filters
from .models import Stage


class StageFilter(django_filters.FilterSet):
     class Meta:
        model = Stage
        fields = ['nom', 'Grade','faculté','critérs'] 