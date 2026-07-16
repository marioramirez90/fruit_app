from django.http import JsonResponse
# Create your views here.
def send_fruits(request):
   fruits =[
      {
        "name": "Apfel",
        "gewicht": 0.30,
        "farbe": "rot",
        },
        {
        "name": "Banana",
        "gewicht": 0.20,
        "farbe": "gelb",
        },
        {
        "name": "Orange",
        "gewicht": 0.25,
        "farbe": "orange",
        },
         {
        "name": "birne",
        "gewicht": 0.25,
        "farbe": "grün",
        },
         {
        "name": "kiwi",
        "gewicht": 0.25,
        "farbe": "braun",
        }
      
   ]

   return JsonResponse(fruits)