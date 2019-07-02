from django.http import HttpResponse
import subprocess

def led_on(request):
    output = subprocess.check_output(['mygpio','-g','18','-e','1'])
    return HttpResponse('led on ' + str(output, 'utf-8'))

def led_off(request):
    output = subprocess.check_output(['mygpio','-g','18','-e','0'])
    return HttpResponse('led off ' + str(output,'utf-8'))
