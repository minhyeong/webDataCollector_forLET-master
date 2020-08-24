from django.shortcuts import render, redirect, HttpResponse

from cms.models import QuestionList , Log

from datetime import datetime
import math
import json



# Create your views here.
def home(request):
    return render(request, 'data_collector/local_home.html')


def db_state(request):
    users = QuestionList.objects.all()
    user_num = len(users)

    hist_users = [ 0, 0, 0, 0, 0 , 0 ,0 ,0, 0, 0 ,0 ]
    for user in users:
        toshi = (int(datetime.now().strftime('%s')) - int(user.birth.strftime('%s'))) / (60*60*24*365.24)
        # print(str(math.floor(toshi)) + " :" + str(user.birth.year) )
        i = math.floor(toshi/10)
        if i > 11:
            i = 10
        hist_users[i] += 1

    return render(request, 'data_collector/db_state.html' , dict(users=users , user_num=user_num, hist_users=hist_users ))


def log_view(request):
    logs = Log.objects.order_by('id')

    convert_logs = []
    for log in logs:
        buf_log = {}
        buf_log['user_id'] = log.user_id
        buf_log['timestamp'] = datetime.fromtimestamp(log.timestamp/1000.0).strftime('%Y-%m-%d %H:%M:%S.') + str(log.timestamp%1000)
        # buf_log['timestamp'] = strftime('%Y-%m-%d %H:%M:%S')
        if log.state_data == "":
            buf_log['state_data'] = []
        else:
            buf_log['state_data'] = json.loads(log.state_data)


        convert_logs.append(buf_log)


    return render(request , "data_collector/log_view.html" ,{'logs': convert_logs})


def log_view_player(request , user_id):
    logs = Log.objects.filter(user_id__exact=user_id)

    convert_logs = []
    for log in logs:
        buf_log = {}
        buf_log['user_id'] = log.user_id
        buf_log['timestamp'] = datetime.fromtimestamp(log.timestamp/1000.0).strftime('%Y-%m-%d %H:%M:%S.') + str(log.timestamp%1000)
        # buf_log['timestamp'] = strftime('%Y-%m-%d %H:%M:%S')
        if log.state_data == "":
            buf_log['state_data'] = []
        else:
            buf_log['state_data'] = json.loads(log.state_data)


        convert_logs.append(buf_log)


    return render(request , "data_collector/log_view.html" ,{'logs': convert_logs})
