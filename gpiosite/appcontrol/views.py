from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

def blinker(request):
	if 'on' in request.POST:
		GPIO.output(18,GPIO.HIGH)
	elif 'off' in request.POST:
		GPIO.output(18,GPIO.LOW)
	return render(request, 'control_page.html')

