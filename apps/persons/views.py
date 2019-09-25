import requests

# Django
from django.conf import settings
from django.http import Http404

# RestFramework
from rest_framework import views, status
from rest_framework.response import Response

# Serializers
from apps.persons.serializers import PersonSerializer, PersonUpdateSerializer


# Agregar una persona
class AddPerson(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():

            url_pipdrive = '%s/persons?api_token=%s' % (settings.URL_PIPDRIVE, settings.PIPDRIVE_TOKEN)
            data_payload = request.data

            response = requests.post(url_pipdrive, data=data_payload)
            data_json = response.json()
            if response.status_code == 201:
                return Response(data=data_json['data'], status=status.HTTP_200_OK)

            return Response(data=data_json['error'], status=response.status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Person(views.APIView):

    def get_object(self, pk):
        url_pipdrive = '%s/persons/%s?api_token=%s' % (settings.URL_PIPDRIVE, pk, settings.PIPDRIVE_TOKEN)

        response = requests.get(url_pipdrive)

        if response.status_code == 200:
            return response.json()
        raise Http404

    def get(self, request, pk):

        person = self.get_object(pk)

        return Response(data=person['data'])

    def put(self, request, pk):
        person = self.get_object(pk)

        serializer = PersonUpdateSerializer(data=request.data)

        if serializer.is_valid():
            url_pipdrive = '%s/persons/%s?api_token=%s' % (settings.URL_PIPDRIVE, pk, settings.PIPDRIVE_TOKEN)

            response = requests.put(url_pipdrive, data=request.data)
            data_json = response.json()
            if response.status_code == 200:

                return Response(data=data_json['data'], status=status.HTTP_200_OK)

            return Response(data=data_json['error'], status=response.status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person = self.get_object(pk)

        url_pipdrive = '%s/persons/%s?api_token=%s' % (settings.URL_PIPDRIVE, pk, settings.PIPDRIVE_TOKEN)

        response = requests.delete(url_pipdrive)
        data_json = response.json()

        if response.status_code == 200:
            return Response(status=status.HTTP_200_OK)

        return Response(data=data_json['error'], status=status.HTTP_400_BAD_REQUEST)


add_person = AddPerson.as_view()
detail_person = Person.as_view()
