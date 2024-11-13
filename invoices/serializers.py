from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(ModelSerializer):
    quantity = serializers.IntegerField(min_value=0)

    class Meta:
        model = InvoiceDetail
        fields = ["id", "description", "quantity", "price", "line_total"]

    def validate(self, data):
        if data["quantity"] <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        if data["price"] <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return data


class InvoiceSerializer(ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ["id", "invoice_number", "customer_name", "date", "details"]

    def create(self, validated_data):
        details_data = validated_data.pop("details")
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice

    def update(self, instance, validated_data):
        details_data = validated_data.pop("details")
        instance.invoice_number = validated_data.get(
            "invoice_number", instance.invoice_number
        )
        instance.customer_name = validated_data.get(
            "customer_name", instance.customer_name
        )
        instance.date = validated_data.get("date", instance.date)
        instance.save()

        instance.details.all().delete()
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=instance, **detail_data)
        return instance
