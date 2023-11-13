from rest_framework import serializers
from sites.models import SiteAvail

class SiteAvailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteAvail
        fields = "__all__"