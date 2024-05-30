from rest_framework import status
from rest_framework.response import Response
from user_account.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from .models import Department
from .serializer import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes

@api_view(['GET'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def list_departments(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def add_department(request):
    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def update_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def delete_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        department.delete()
        return Response({"message": "Department deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


