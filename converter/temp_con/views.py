from django.shortcuts import render


def home(request):
    return render(request, 'temp_con/home.html')


def convert_temperature(request):
    if request.method == 'POST':
        temperature = float(request.POST['temperature'])
        conversion_type = request.POST['conversion_type']

        if conversion_type == 'f_to_c':
            converted_temperature = (temperature - 32) * 5 / 9
            result = f"{temperature}°F is {converted_temperature}°C"
        elif conversion_type == 'c_to_f':
            converted_temperature = (temperature * 9 / 5) + 32
            result = f"{temperature}°C is {converted_temperature}°F"
        else:
            result = "Invalid conversion type"

        return render(request, 'temp_con/result.html', {'result': result})

    return render(request, 'temp_con/home.html')
