from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from backend.common.rest.pagination import Pagination

__all__ = ['BaseViewSet']


class BaseViewSet(GenericViewSet):
    pagination_class = Pagination
    permission_classes = (IsAuthenticated,)
