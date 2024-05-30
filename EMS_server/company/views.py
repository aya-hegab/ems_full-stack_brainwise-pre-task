from rest_framework import status
from .models import Company
from .serializer import CompanySerializer
from user_account.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes


@api_view(['GET'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def list_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def add_company(request):
    if request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def update_company(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def delete_company(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        company.delete()
        return Response({"message": "Company deleted successfully"}, status=status.HTTP_204_NO_CONTENT)