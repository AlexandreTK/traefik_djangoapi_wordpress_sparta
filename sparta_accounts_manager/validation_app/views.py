from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from .models import UserLicense

def validation(request, account_number):

    users = UserLicense.objects.filter(account_number=account_number, user_status='A')
    if users:
        user = users[0]
        return JsonResponse({'user_status':'valid', 'expiration_date': user.expiration_date.strftime('%d/%m/%Y')})
    else:
        return JsonResponse({'user_status':'invalid'})

    # return HttpResponse("Hello, world. Your account number is: "+account_number)

def homepage(request):
    return HttpResponse("Sparta!")