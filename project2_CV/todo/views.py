from django.shortcuts import render
from .forms import CVform
from .models import CV
from django.views import View

class HomeView(View):
    def get(self, request):
        form = CVform()
        candidates = CV.objects.all()
        return render(request ,'home.html' , {'candidates':candidates, 'form':form})
        
    def post(self, request ):
        form =CVform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'form': form})
        
class CandidateView(View):
    def get(self, request, pk):
        candidate = CV.objects.get(pk=pk)
        return render(request, 'cv2.html', {'candidate': candidate})
