from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

from .models import QuestionList , Log
from .forms import BasicQuestion, LifeProlongingQuestion, LifeQualityQuestion, TIPI_JQuestion, DASQuestion

from datetime import datetime, date , time

import json
import math
import requests

def agreement(request):
    return render(request, 'cms/agreement.html')


def home(request):

    if request.method == 'POST':
        if request.POST['agree']:
            request.session.flush()
            return redirect('cms:question_basic')

    info_text = "延命治療についてのアンケート"

    return render(request, 'cms/home.html', dict(info_text=info_text ))


def get_user_id_from_session(request):
    user_id = None
    if 'user_id' in request.session:
        user_id = request.session['user_id']
    return user_id

def confirm_user_id(user_id):
    return user_id is None

# 基本質問
def question_basic(request):
    user_id = get_user_id_from_session(request)
    if user_id is None:
        user = QuestionList()
    else:
        user = QuestionList.objects.get(pk=user_id)

    birth_elems = {'year':0, 'month': 0,'day': 0}
    sleep_time_elems = {'top': -1 ,'bottom': -1 }
    if request.method == 'POST':

        rev = request.POST

        # year,mouth,dayが入力されていることを確認する
        birth_flag = True
        for elem in birth_elems.keys():
            if rev[elem].isdigit()==True:
                if int(rev[elem]) == 0:
                    birth_flag = False
                else:
                    birth_elems[elem] = int(rev[elem])

        if(birth_flag):
            user.birth = date(birth_elems['year'], birth_elems['month'], birth_elems['day'])

        user.gendar = rev['gendar']
        user.blood = rev['blood']
        user.sleep_time_top = time(int(rev['sleep_time_top']),00,00)
        user.sleep_time_bottom = time(int(rev['sleep_time_bottom']),00,00)
        user.sport = rev['sport']
        user.music = rev['music']
        user.taste = rev['taste']
        user.save()
        request.session['user_id'] = user.id

        if(birth_flag):
            return redirect('cms:question_lifequality_rank_fix')


    form = BasicQuestion(instance=user)
    if user.birth is not None:
        birth_elems['year'] = user.birth.year
        birth_elems['month'] = user.birth.month
        birth_elems['day'] = user.birth.day
    if user.sleep_time_bottom is not None:
        sleep_time_elems['bottom'] = user.sleep_time_bottom.hour
    if user.sleep_time_top is not None:
        sleep_time_elems['top'] = user.sleep_time_top.hour

    return render(request, 'cms/question_basic.html', dict(form=form ,
                                                           birth_form=birth_elems,
                                                           sleep_time_form=sleep_time_elems
                                                           ))


# 生命の質
def question_lifequality_rank_fix(request):
    user_id = get_user_id_from_session(request)
    if(confirm_user_id(user_id)):
        return redirect('cms:home')
    user = QuestionList.objects.get(pk=user_id)

    if request.method == 'POST':
        rev = request.POST

        user.rank1 = rev['rank1']
        user.rank2 = rev['rank2']
        user.rank3 = rev['rank3']
        user.rank4 = rev['rank4']
        user.rank5 = rev['rank5']
        user.rank6 = rev['rank6']

        user.save()
        return redirect('cms:TIPI_J')

    else:
        form = LifeQualityQuestion(instance=user)

    return render(request, 'cms/question_lifequality_rank_fix.html', dict(form=form))

# TIPI_J : 性格判定
def TIPI_J(request):
    user_id = get_user_id_from_session(request)
    if(confirm_user_id(user_id)):
        return redirect('cms:home')
    user = QuestionList.objects.get(pk=user_id)

    if request.method == 'POST':
        form = TIPI_JQuestion(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('cms:DAS')
    else:
        form = TIPI_JQuestion(instance=user)

    return render(request, 'cms/question_tipij.html', dict(form=form))


# 死生観
def DAS(request):
    user_id = get_user_id_from_session(request)
    if(confirm_user_id(user_id)):
        return redirect('cms:home')

    user = QuestionList.objects.get(pk=user_id)

    if request.method == 'POST':
        form = DASQuestion(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('cms:question_lifeprolonging')
    else:
        form = DASQuestion(instance=user)

    return render(request, 'cms/question_das.html', dict(form=form))


def post_weblet_api(querys=None):
    if querys is None:
        querys = {}
    _url = "https://lang1.is.tokushima-u.ac.jp:9201/wdclet-api/"

    r = requests.post(_url, querys)
    return json.loads(r.text)

# 延命治療選択
def question_lifeprolonging(request):
    user_id = get_user_id_from_session(request)
    if(confirm_user_id(user_id)):
        return redirect('cms:home')

    user = QuestionList.objects.get(pk=user_id)

    if request.method == 'POST':
        form = LifeProlongingQuestion(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('cms:finish')
    else:
        form = LifeProlongingQuestion(instance=user)

    will_help_data = post_weblet_api(querys=user.set_querys())

    return render(request, 'cms/question_lifeprolonging.html',
                  dict(form=form, user_id=user_id,
                       will_help_data=will_help_data))


# 終了画面
def finish(request):
    info_text = "お疲れ様でした"
    request.session.flush()
    return render(request, 'cms/finish.html', dict(info_text=info_text))


def logging(request):

    if request.method == 'PUT':
        rev = request.body
        str_rev = rev.decode()
        dict_rev = json.loads(str_rev)

        log = Log()
        log.user_id = dict_rev['Item']['user_id']
        # log.timestamp = datetime.fromtimestamp(dict_rev['Item']['timestamp']/1000.0)
        log.timestamp = dict_rev['Item']['timestamp']
        log.state_data = dict_rev['Item']['state']
        log.save()

        # print(dict_rev)
        # print(json.dumps(rev))

        return HttpResponse("ok!")

    return redirect('cms:home')
