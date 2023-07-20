from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import YourModel

def your_view(request):
    if request.method == 'POST':
        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        field3 = request.POST.get('field3')
        checkbox_list = request.POST.get('checkbox_list', False)

        # Save the data to the database
        YourModel.objects.create(
            field1=field1,
            field2=field2,
            field3=field3,
            checkbox_list=checkbox_list
        )

    # Fetch all the data from the database
    all_data = YourModel.objects.all()
    return render(request, 'UI.html', {'data': all_data})
