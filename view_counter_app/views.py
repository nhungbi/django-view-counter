from django.shortcuts import render
import random 
import datetime

users = {} #global dict to track view for different users
# Create your views here.
def track_view(request):
    print(request.COOKIES)
    print(users)

    #first time visit = check for existing user in cookie
    user_id = request.COOKIES.get('user_id')

    if user_id not in users: 
        user_id = str(random.randint(100000,999999))
        users[user_id] = {
            'count': 1,
            'start_time': datetime.datetime.now(),
        }
    else:
        users[user_id]['count'] += 1

    response = render(request, 'count.html', users[user_id])
    # response.delete_cookie('foo') to delete cookie from other projects
    # response.delete_cookie('sessionid')
    # response.delete_cookie('session_id_number')
    response.set_cookie('user_id', user_id)
    return response



    
    
