from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework.views import APIView
# Create your views here.




from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403,'message':'invalid serializer'})
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        # token_obj , _ =  Token.objects.get_or_create(user = user) #TokenAuthentication
        refresh = RefreshToken.for_user(user)

        return Response({'status':200,'message':'data saved',
                          'refresh': str(refresh) , 
                          'access': str(refresh.access_token), 
                          'payload':serializer.data,
                          'message':'Data Saved'})



# @api_view(['GET'])
# def home(request): 
#     query = Student.objects.all()
#     squery =  StudentSerializer(query,many=True)
#     return Response({'status':200, 'message':squery.data})

# @api_view(['POST'])
# def post_student(request):
#     x = request.data
#     serializer = StudentSerializer(data = x)
#     if serializer.is_valid():
#         return Response({'status':200, 'message':'you send', 'payload':x})
#     print(serializer.errors)
#     return Response({'status':403, 'errors': 'serializer.error' ,'error':'invalid data format'})

# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student, data=request.data)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':400,'errors':serializer.errors})
#         serializer.save()
#         return Response({'status':200, 'message':'data updated', 'updated data':serializer.data})
#     except Exception as e:
#         return Response({'status':403, 'error':'invalid id'})
    
# @api_view(['DELETE'])
# def delete_student(request):
#     try:
#         id = request.GET.get('id')
#         print(id)
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response({'status':200, 'message':'student deleted'})
#     except Exception as e:
#         return Response({'status':403, 'message':'invalid id', 'error':e} )
    
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({'status':200,'Books Data':serializer.data})


#Adding Token-Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj, many=True)
        print(request.user)
        return Response({'payload':serializer.data})
    
    def post(self, request):
        x = request.data
        serializer = StudentSerializer(data = x)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'message':'you send', 'payload':x})
        print(serializer.errors)
        return Response({'status':403, 'errors': 'serializer.error' ,'error':'invalid data format'})
    
    def put(self, request):
        pass
    
    def patch(self, request):
        try:
            student = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student, data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':400,'errors':serializer.errors})
            serializer.save()
            return Response({'status':200, 'message':'data updated', 'updated data':serializer.data})
        except Exception as e:
            return Response({'status':403, 'error':'invalid id'})
    
    def delete(self, request):
        try:
            id = request.GET.get('id')
            print(id)
            student = Student.objects.get(id=id)
            student.delete()
            return Response({'status':200, 'message':'student deleted'})
        except Exception as e:
            return Response({'status':403, 'message':'invalid id', 'error':e} )

