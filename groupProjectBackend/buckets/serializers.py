from rest_framework import serializers
from .models import Transaction, Bucket, Icon

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class BucketSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')
    
    class Meta:
        model = Bucket
        fields = (
            'id',
            'owner',
            'name',
            'description',
            'is_active',
            'min_amt',
            'percentage',
            'parent_bucket',
            'children'
            )

    def create(self, validated_data):
        return Bucket.objects.create(**validated_data)

class BucketDetailSerializer(BucketSerializer):

    def update(self, instance, validated_data):        
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.min_amt = validated_data.get('min_amt', instance.min_amt)
        instance.percentage = validated_data.get('percentage', instance.percentage)
        instance.parent_bucket = validated_data.get('parent_bucket', instance.parent_bucket)
        instance.save()
        return instance

class TransactionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField (source='owner.id')
    income = serializers.FloatField()
    date_created = serializers.ReadOnlyField()
    receipt = serializers.JSONField()

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

class TransactionDetailSerializer(TransactionSerializer):

    def update(self, instance, validated_data):        
        instance.income = validated_data.get('income', instance.income)
        instance.receipt = validated_data.get('receipt', instance.receipt)
        instance.save()
        return instance


class IconSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    image = serializers.CharField()

    def create(self, validated_data):
        return IconSerializer.objects.create(**validated_data)