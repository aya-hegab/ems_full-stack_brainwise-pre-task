from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from user_account.permissions import IsAdminUser
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes


@api_view(['POST'])
@permission_classes([IsAdminUser])
@authentication_classes([TokenAuthentication])
def employee_register(request):
    serializer = EmployeeRegisterSerializer(data=request.data)
    if serializer.is_valid():
        # employee, token = serializer.save()
        employee = serializer.save()
        return Response(
            {
                "user": {
                    "id": employee.user.id,
                    "email": employee.user.email,
                    "role": employee.user.role,
                    # "token": token.key
                },
                "employee": {
                    "id": employee.id,
                    "name": employee.name,
                    "mobile_number": employee.mobile_number,
                    "company": employee.company.name,
                    "department": employee.department.name,
                    "designation": employee.designation,
                    "status": employee.status,
                    "hired_on": employee.hired_on,
                    "days_employed": employee.days_employed,
                }
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def custom_auth_token(request):
    print(request.data)
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'role': user.role})
    else:
        raise AuthenticationFailed(detail='Method Not Allowed', code=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout_view(request, format=None):
    request.user.auth_token.delete()
    return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def user_employee_details(request):
    user = request.user
    try:
        employee = user.employee_profile  
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response({'detail': 'Employee details not found'}, status=status.HTTP_404_NOT_FOUND)

