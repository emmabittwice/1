let distancia = 0
input.onButtonPressed(Button.B, function () {
    basic.showNumber(1)
    basic.pause(100)
    basic.showNumber(2)
    basic.pause(100)
    basic.showNumber(3)
    basic.pause(100)
    basic.showNumber(4)
    basic.pause(100)
    basic.showNumber(5)
    basic.clearScreen()
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    distancia = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P0,
    PingUnit.Centimeters
    )
    if (distancia < 5) {
        maqueen.servoRun(maqueen.Servos.S2, 90)
    } else {
        maqueen.servoRun(maqueen.Servos.S2, 0)
    }
    maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
    maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
})
basic.forever(function () {
	
})
