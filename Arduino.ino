//#include <AFMotor.h>
//AF_DCMotor pump(3);
//AF_DCMotor fan(1);
//AF_DCMotor light(2);
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 20, 4); 
int startstring = 0; 
int charcount = 0; 
int iCount = 0;
void setup() {

Serial.begin(9600);
lcd.init();
lcd.backlight();
lcd.setCursor(0,0); 
pinMode(13, OUTPUT);
}


void loop() {
char incomingByte = 0; 
if (Serial.available() > 0) { 
incomingByte = Serial.read();
//Serial.print(incomingByte);
digitalWrite(13, HIGH);
//if (incomingByte  = '*'){      //pump
//  digitalWrite(LED_BUILTIN , LOW);
//  delay(5000);
//  digitalWrite(LED_BUILTIN , HIGH);
//    pump.setSpeed(200);
//    pump.run(FORWARD);
//    delay(5000);
//    pump.run(RELEASE);
//    delay(500000); 
//}
//else 
//if (incomingByte == '|'){        //fan on
//  fan.setSpeed(200);
//  fan.run(FORWARD);
//  }
//  else if (incomingByte == '='){        //fan off
//  fan.run(RELEASE);
//  }
//  else if (incomingByte == '+'){        //light on
//  light.setSpeed(200);
//  light.run(FORWARD);
//  }
//
//  else if (incomingByte == '_'){         //light off
//  light.run(RELEASE);
//  } 
//else

if ((incomingByte == '~') && (startstring == 1)){
startstring = 0;
delay(3000);
lcd.clear();
charcount = 0;
lcd.setCursor(0,0);
}
else {
   digitalWrite(LED_BUILTIN , LOW);
  delay(50000);
  }
if (startstring == 1){
  if (++charcount < 81){
    lcd.print(incomingByte);
  }
}

if (charcount == 20) {
lcd.setCursor(0,1);
}
if (charcount == 40) {
lcd.setCursor(0,2);
}
if (charcount == 60) {
lcd.setCursor(0,3);
}
if (charcount == 80){
delay(6000);
lcd.clear();
lcd.setCursor(0,0);
charcount = 0;
}

if (incomingByte == '~'){
startstring = 1;
}
}
digitalWrite(13, LOW);
delay(100);
}
