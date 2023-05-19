#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
//ประกาศตัวแปร
const int trig1 = 13;
const int echo1 = 12;
const int trig2 = 8;
const int echo2 = 9;
const int servoPin = 10;
const int buzzerPin = 11;
const int SW_modePin = 7;
const int SW_manualPin = 6;

const int DISTANCE_THRESHOLD_OUTSIDE = 35; //กำหนดระยะห่างด้านนอก
const int DISTANCE_THRESHOLD_INSIDE = 30; //ระยะภายใน

unsigned short distance1;
unsigned short distance2;

Servo myservo;
LiquidCrystal_I2C lcd(0x20, 16, 2);
//------------------------------
void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.backlight();
  myservo.attach(servoPin);
  pinMode(echo1, INPUT);
  pinMode(trig1, OUTPUT);
  pinMode(echo2, INPUT);
  pinMode(trig2, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(SW_modePin, INPUT);
  pinMode(SW_manualPin, INPUT);
}

void loop()
{
  myservo.write(0);
  
  if (digitalRead(SW_modePin)) // Automode
  {
    readUltrasonicDistance(trig2, echo2, distance2);//เรียกตัวด้านใน
    
    if (distance2 > DISTANCE_THRESHOLD_INSIDE)
    {
      lcd.clear();
      lcd.print("Not Full");
      readUltrasonicDistance(trig1, echo1, distance1);//เช็คค่าข้างนอก
      if (distance1 < DISTANCE_THRESHOLD_OUTSIDE)
      {
        tone(buzzerPin, 250, 500);
        delay(1000);
        openclosetrash();
        delay(5000);
      }
    }
    else
    {
      lcd.clear();
      lcd.print("Full");
      delay(5000);
    }
  }
  else // Manual mode
  {
    readUltrasonicDistance(trig2, echo2, distance2);
    Serial.print("Distance Inside: ");
    Serial.print(distance2);
    Serial.println(" cm");
    
    if (distance2 > DISTANCE_THRESHOLD_INSIDE)
    {
      lcd.clear();
      lcd.print("Not Full");
      delay(2000);
    }
    else
    {
      lcd.clear();
      lcd.print("Full");
      delay(5000);
    }
    
    while (!digitalRead(SW_manualPin))
    {
      myservo.write(120);
    }
  }
}

unsigned short readUltrasonicDistance(int triggerPin, int echoPin)//ฟังค์ชั่นใช้งาน ultrasonic โดยtrigger pin เป็นตัวกำหนดว่าจะเอาตัวไหน
{
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(5);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(triggerPin, LOW);

  unsigned long duration = pulseIn(echoPin, HIGH);
  unsigned short distance = (duration / 2) / 29.1;
  
  return distance; // ส่งค่า ระยะออกเป็นผลของฟังชั่น
}

void openclosetrash()//ฟังชั่นเปิดปิดฝาถัง
{
  for (int pos = 0; pos <= 120; pos += 10)
  {
    myservo.write(pos);
    delay(20);
  }
  
  delay(5000);
  
  for (int pos = 120; pos >= 0; pos -= 10)
  {
    myservo.write(pos);
    delay(15);
  }
}
