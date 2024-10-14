from rest_framework import serializers
from django.contrib.gis.geos import Point
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError, GeocoderTimedOut
from ..models import Address, ClientAddress, ProfessionalAddress


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'street',
            'city',
            'postal_code',
            'country',
            'latitude',
            'longitude',
            'location',
            'slug',
        ]
        read_only_fields = ['slug']

    def validate(self, data):
        address_str = f"{data.get('street')}, \
            {data.get('postal_code')} {data.get('city')}, \
                {data.get('country')}"
        geolocator = Nominatim(user_agent="Nois")

        try:
            location = geolocator.geocode(address_str, exactly_one=True)
            if location:
                django_point = Point(location.longitude, location.latitude)
                data['latitude'] = location.latitude
                data['longitude'] = location.longitude
                data['location'] = django_point
            else:
                raise serializers.ValidationError(
                    "L'adresse fournie est invalide ou incomprise."
                    )
        except GeocoderServiceError:
            raise serializers.ValidationError(
                "Le service de validation des adresses \
                    est temporairement indisponible. \
                        Veuillez réessayer plus tard."
                )
        except GeocoderTimedOut:
            raise serializers.ValidationError(
                "Le service de validation des adresses \
                    a rencontré une erreur. Veuillez réessayer."
            )
        except Exception as e:
            raise serializers.ValidationError(
                f"Une erreur est survenue lor de la validation de l'adresse. \
                    {str(e)}"
            )

        return data

    def create(self, validated_data):
        print("Creating instance of:", self.Meta.model)
        address = self.Meta.model(**validated_data)
        print("Address instance created:", address)
        address.save()
        return address

    def update(self, instance, validated_data):
        instance.street = validated_data.get(
            'street', instance.street
            )
        instance.city = validated_data.get(
            'city', instance.city
            )
        instance.postal_code = validated_data.get(
            'postal_code', instance.postal_code
            )
        instance.country = validated_data.get(
            'country', instance.country
            )
        instance.latitude = validated_data.get(
                'latitude', instance.latitude
                )
        instance.longitude = validated_data.get(
                'longitude', instance.longitude
                )
        instance.location = validated_data.get(
                'location', instance.location
                )
        instance.save()

        return instance

class ClientAddressSerializer(AddressSerializer):
    class Meta(AddressSerializer.Meta):
        model = ClientAddress
        fields = AddressSerializer.Meta.fields + ['client']

class ProfessionalAddressSerializer(AddressSerializer):
    class Meta(AddressSerializer.Meta):
        model = ProfessionalAddress
        fields = AddressSerializer.Meta.fields + ['professional']

