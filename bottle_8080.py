from bottle import route, run, template, get, static_file, request
from time import sleep
import control

@route('/<x>')
def movement(x):
    control.move(x)

@route('/pwm/<ena>/<enb>')
def movement_by_pwm(ena,enb):
    ena, enb = float(ena), float(enb)
    if ena > 0:
        control.GPIO.output(control.in1,1)
        control.GPIO.output(control.in2,0)
    else :
        control.GPIO.output(control.in1,0)
        control.GPIO.output(control.in2,1)
    
    if enb > 0:
        control.GPIO.output(control.in3,1)
        control.GPIO.output(control.in4,0)
    else :
        control.GPIO.output(control.in3,0)
        control.GPIO.output(control.in4,1)
    
    control.ena.ChangeDutyCycle(abs(ena))
    control.enb.ChangeDutyCycle(abs(enb))

@route('/wonder')
def wonderwoman():
    return template('dictate')

@route('/wonder/<sentence>')
def wonder(sentence):
    print(sentence)
    for word in sentence:
        if word=='跑':
            control.move('w',1)
        elif word=='前':
            control.move('w',0.3)
        elif word=='進':
            control.move('w',0.3)
        elif word=='左':
            control.move('a',0.3)
        elif word=='右':
            control.move('d',0.3)
        elif word=='後':
            control.move('s',0.3)
        elif word=='圈':
            control.move('j',1)
            sleep(0.1)
            control.move('k',1)

@get('/<filename>')
def js(filename):
    return static_file(filename, root='static')

@route('/ant')
def antman():
    return template('touch')

@route('/ajax', method='POST')
def ajax():
    arrow = request.forms.get("arrow")

    stop_key = (87, 83, 65, 68)

    if int(arrow) == 119:
        control.move('w',0.3)
    if int(arrow) == 115:
        control.move('s',0.3)
    if int(arrow) == 100:
        control.move('d',0.3)
    if int(arrow) == 97:
        control.move('a',0.3)
    if int(arrow) in stop_key:
        print('STOP')

try:
    run(host='0.0.0.0', port=8080)

finally:
    control.ena.stop()
    control.enb.stop()
    control.GPIO.cleanup()