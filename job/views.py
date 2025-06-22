from .models import Job, School
from rest_framework import generics
from .serializers import JobSerializer
from .serializers_school import SchoolSerializer
from langchain_search import LangChainSearchMixin

class JobListAPI(LangChainSearchMixin, generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



    def get(self, request, *args, **kwargs):
        import logging
        logger = logging.getLogger(__name__)
        logger.warning("Handling GET request for job list with LangChain search")
        return super().get(request, *args, **kwargs)

class SchoolListAPI(LangChainSearchMixin, generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

