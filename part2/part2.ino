int stopTime=500;
void setup() {
  // put your setup code here, to run once:
pinMode(13,OUTPUT);
Serial.begin(9600);
}

int i=0;
void loop() {
  // put your main code here, to run repeatedly:
i++;
Serial.print("Iteration: ");
Serial.println(i);
delay(stopTime);
digitalWrite(13,HIGH);
delay(stopTime);
digitalWrite(13,LOW);
}
