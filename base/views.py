from django.shortcuts import render

# Create your views here.
def index(request):
    #print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
    return render(request, 'index.html')