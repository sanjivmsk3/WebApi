from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import *
from .models import *
from datetime import datetime

# Create your views here.

#####--------------------Question 1------------------#######
class Home(APIView):
    def post(self, request):
        all_detail = request.data
        p = 0
        c = 0
        for i in all_detail:
            if i >= 0:
                p += 1
            elif i < 0:
                c += 1
        context = {
            "valid_entries":p,
            "invalid_entries":c,
            "min":min(all_detail),
            "max":max(all_detail),
            "average": sum(all_detail) / p
        }
        return Response(context)

#####--------------------Question 2------------------#######
class BookSlot(APIView):
    def post(self, request):
        slot = 10;
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        s = request.data['field1']
        if current_time <= str("01:00"):
            if s <= 2:
                slot = slot - s
                if slot >= 0:
                    a = {"status": "confirmed"}
                else:
                    return Response({"slot full, unable to save booking"})
            else:
                return Response({"Please enter only 2 slot"})
            return Response(a)
        else:
            return Response({"Booking is available only 12:00AM to 01:00AM"})


#####--------------------Question 3------------------#######
class Plot(APIView):
    def post(self, request):
        x = request.data['x']
        y = request.data['y']

        if x == 1 and y == 1:
            return Response({"status":"accepted"})
        elif x == 1 and y == 5:
            return Response({"status": "accepted"})
        elif x == 5 and y == 1:
            return Response({"status": "accepted"})
        elif x == 5 and y == 2:
            return Response({"status": "accepted"})
        elif x == 5 and y == 5:
            return Response({"status": "Success"})