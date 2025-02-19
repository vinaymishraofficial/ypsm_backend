from django.shortcuts import render
from rest_framework import viewsets
from .models import Enquiry, Contact
from .serializers import EnquirySerializer, ContactSerializer

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Create your views here.
