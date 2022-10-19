from django.shortcuts import render

from datetime import date
from rest_framework import viewsets
from .models import hotel, room, range, show
from .serilazers import hotelSerializer

def start(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['качество', 'комфорт', 'эмоции']
    }})


class hotelViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = hotel.objects.all().order_by('stars')
    serializer_class = hotelSerializer  # Сериализатор для модели
def GetTours(request):
    return render(request, 'orders.html', {'data':{
        'current_date': date.today(),
        'test': range.objects.all()}})
def GetTour(request, id):
    return render(request, 'hotels.html', {'data': {'range':
                                              range.objects.filter(id=id)
                                          }})

def GetHotels(request):
	return render(request, 'hotels.html', {'data':{
		'hotels':hotel.objects.all()
	}})

def GetRooms(request, id):
	return render(request,'hotel.html', {'data':{
		'hotel':hotel.objects.filter(id=id),
		'rooms': room.objects.filter(hotel_id=id),
        'idfor' : id
	}})

def GetContact(request):
    return render(request, 'contact.html', {'data':{
        'show': show.objects.all()}
    })



    # return render(request, 'orders.html', {'data' : {
    # 'current_date': date.today(),
    # 'tour': [
    # {'title': 'Страны', 'id': 1},
    # {'title': 'Отели', 'id': 2},
    # {'title': 'Контакты', 'id': 3},
    #

    # return render(request, 'contact.html', {'data' : {
    #     'current_date': date.today(),
    #     'contact': [
    #         {'title': 'Отделение в ТЦ Братеевский', 'id': 1,
    #          'address': 'Ключевая ул., 6, Москва, 115612'},
    #         {'title': 'Отделение в ТЦ Пассаж', 'id': 2,
    #          'address': ' т/ц Марьинский Пассаж, 2 этаж, Люблинская ул., 102а, Москва, 109369'},
    #     ]
    # }})



#def GetCountries(request):
    #return render(request, 'countries.html', {'data': {
        #'countries': [
           # {'title': 'Армения', 'id': 1, 'img': "/../../../../../static/images/armenia.jpeg"},
           # {'title': 'Грузия', 'id': 2, 'img': "/../../../../../static/images/georgia.jpeg"},
           # {'title': 'Турция', 'id': 3, 'img': "/../../../../../static/images/turkey.jpeg"},
           # {'title': 'Куба', 'id': 4, 'img': "/../../../../../static/images/cuba.jpeg"},
           # {'title': 'Сейшелы', 'id': 5, 'img': "/../../../../../static/images/seychelles.jpeg"},
           # {'title': 'Сербия', 'id': 6, 'img': "/../../../../../static/images/Belgrad.jpeg"},
           # {'title': 'Мальдивы', 'id': 7, 'img': "/../../../../../static/images/maldives.jpeg"}
       # ]
    #}})



#hotels=[
            #{'title': 'Elegant Hotel & Resort', 'id': 1,
            # 'address':'11 Tandzaghbyur St, Tsaghkadzor 2310, Армения',
            # 'stars': '4 звезды',
            # 'price':'от 5233р'},

           # {'title': 'Armenian Royal Palace', 'id': 2,
            # 'address': '17, 1 4-th St, Yerevan 0029, Армения',
             # 'stars': '4 звезды',
            # 'price': 'от 4033р'},

            #{'title': 'Kobuleti Georgia Palace Hotel & Spa', 'id': 3,
            # 'address': '6200, Agmashenebeli Avenue 275, Kobuleti, Грузия',
            # 'stars': '5 звезды',
            # 'price': 'от 7833р'},

            #{'title': 'Rooms Hotel Kazbegi', 'id': 4,
            # 'address': '1 V.gorgasali St, Stepantsminda 4700, Грузия',
            # 'stars': '4 звезды',
            # 'price': 'от 10833р'},

           # {'title': 'Kamelya Collection Fulya Hotel', 'id': 5,
           #  'address': 'Kamelya Cad. No:8-1, 07620 Çolaklı - Manavgat/Antalya, Турция',
           #  'stars': '5 звезды',
           #  'price': 'от 22833р'},

           # {'title': 'Selectum Luxury Resort', 'id': 6,
           #  'address': '07506 Serik/Antalya, Турция',
           #  'stars': '5 звезды',
           #  'price': 'от 17833р'},

            #{'title': 'Paradisus Princesa del Mar', 'id': 7,
            # 'address': 'Auropista Sur, Carr. Las Morlas, Km. 19 5, Varadero 42200, Куба',
            # 'stars': '5 звезды',
            # 'price': 'от 17033р'},

           # {'title': 'Four Seasons Resort на Сейшелах', 'id': 8,
           #  'address': 'Petite Anse Mahe Island, Сейшельские Острова',
            # 'stars': '5 звезды',
            # 'price': 'от 107833р'},

            #{'title': 'Hyatt Regency Belgrade', 'id': 9,
            # 'address': 'Милентија Поповића 5, Београд 11070, Сербия',
            # 'stars': '4 звезды',
            # 'price': 'от 9000р'},

           # {'title': 'Anantara Kihavah Maldives Villas', 'id': 10,
            # 'address': 'Kihavah Huravalhi Island Baa Atoll, 20215, Мальдивы',
            # 'stars': '4 звезды',
            # 'price': 'от 99000р'}
        #]


