from django.shortcuts import render

# Create your views here.
def home_page(request):

	if request.method == "POST":
		time = request.POST.get("time")

		return render(request, 'appointment/home_page.html', {'time': time})


	return render(request, 'appointment/home_page.html')