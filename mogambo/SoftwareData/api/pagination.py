from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class SoftwareListOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 20
