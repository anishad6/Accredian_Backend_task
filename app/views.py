



from rest_framework import viewsets # all crud
from app.models import Referral
from app.serializers import ReferralSerializer

# Create your views here.

class ReferralListapis(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
