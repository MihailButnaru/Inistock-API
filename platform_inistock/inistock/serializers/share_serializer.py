from rest_framework import serializers

from inistock.models.share_model import ShareModel


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareModel
        fields = [
            "company",
            "symbol",
            "shares",
            "type",
            "date",
            "price",
            "amount",
            "currency",
            "note",
        ]


class InputShareSerializer(serializers.Serializer):
    share = ShareSerializer(many=False, required=True)


class OutputShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareModel
        fields = [
            "share_id",
            "company",
            "symbol",
            "shares",
            "type",
            "date",
            "price",
            "amount",
            "currency",
            "note",
        ]
