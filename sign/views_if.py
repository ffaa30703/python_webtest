from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sign.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist

@csrf_exempt
def test(request):
    print('hello')
    return HttpResponse("ni hao")

@csrf_exempt
def add_event(request):
    print('====================')
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    start_time = request.POST.get('start_time', '')
    print('------'+eid)
    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'event id already exists'})

    if status == '':
        status = 1

    try:
        Event.objects.create(id=eid, name=name, limit=limit, address=address, status=int(status), start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error It must be in YY-MM-DD HH:mm:SS format'
        return JsonResponse({'status': 10024, 'message': error})

    return JsonResponse({'status':200,'message':'add event success'})

# 查询发布会接口
@csrf_exempt
def get_event_list(request):
    eid = request.GET.get("eid", "")#发布会ID
    name = request.GET.get("name", "")#发布会名称
    print('eid:'+eid+' name:'+name)
    if eid == ''and name == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})
    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)

        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status':200, 'message':'success', 'data':event})
    if name!='':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})