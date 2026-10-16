from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if not {'limit', 'offset'} & request.query_params.keys():
            return None
        return super().paginate_queryset(queryset, request, view)
