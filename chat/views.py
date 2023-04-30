from django.shortcuts import render, redirect

from chat.models import Room, Messages #thêm class Room, Message trong file model ở app chat
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def home(request):
	return render(request, 'home.html')

def room(request, room):
	#lấy username ở đường dẫn
	username = request.GET.get('username')
	room_details = Room.objects.get(name = room)

	return render(request, 'room.html', {
		'username' : username,
		'room' : room,
		'room_details' : room_details,
		})

def checkview(request):
	room = request.POST['room_name'] #lấy dữ liệu từ 'room_name ở file home.html'
	username = request.POST['username']
    
	#lọc dữ liệu
	#nếu phòng chat tồn tại
	if Room.objects.filter(name = room).exists():
		return redirect('/' + room + '/?username=' + username)
	#nếu phòng chat chưa có
	else:
		#tạo phòng chát mới
		new_room = Room.objects.create(name = room)
		new_room.save() #lưu phòng chát mới
		return redirect('/' + room + '/?username=' + username)

def send(request):
	#lấy dữ liệu từ room.html
	message = request.POST['message']
	username = request.POST['username']
	room_id = request.POST['room_id']

	#tạo message để up lên database
	new_message = Messages.objects.create(value = message, user = username, room=room_id)
	new_message.save()
	return HttpResponse('Message sent successful !')

def getMessages(request, room):
	#get room
	room_details = Room.objects.get(name = room)

	messages = Messages.objects.filter(room__icontains = room_details.id)
	return JsonResponse({'messages':list(messages.values())})