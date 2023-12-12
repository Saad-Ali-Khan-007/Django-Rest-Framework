from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer

# Create your views here.
@api_view(['GET','POST'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['flask','Django','Tornado','FastApi'],
        'course_provider': 'Scaler'
    }
    if request.method == 'GET':
        print('You hit a get method')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print(data)
        print("You hit a post method")
        return Response(courses)

@api_view(['GET','POST','DELETE','PUT','PATCH'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        person_id = data['id']
        person_obj = Person.objects.get(pk=person_id)
        serializer = PeopleSerializer(person_obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'PATCH':
        data = request.data
        person_id = data['id']
        person_obj = Person.objects.get(pk=person_id)
        serializer = PeopleSerializer(person_obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        person_id = request.data['id']
        person_obj = Person.objects.get(pk=person_id)
        person_obj.delete()
        return Response({"message": "Person deleted successfully"})
        


    