from bottle import route, run
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

try:
    run(host='0.0.0.0', port=8080)

finally:
    control.ena.stop()
    control.enb.stop()
    control.GPIO.cleanup()
