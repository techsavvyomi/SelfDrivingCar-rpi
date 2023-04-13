



#include <MotorDriver.h>

#include<SoftwareSerial.h>
SoftwareSerial bt05(10,9); 
MotorDriver m;


// duration for output
int time = 90;
// initial command
char command = 0;

void setup() {
  pinMode(13,OUTPUT);
  pinMode(2,OUTPUT);
  Serial.begin(9600);
  bt05.begin(9600);
}

void loop() {
  //receive command
  if (bt05.available() > 0){
    command = bt05.read();
  }
  else{
    reset();
  }
   send_command(command,time);
}

void stop(){
  m.motor(1,BRAKE,0);
  m.motor(2,BRAKE,0);
  m.motor(3,BRAKE,0);
  m.motor(4,BRAKE,0); 
}

void right(int time){
  digitalWrite(13,HIGH);
  m.motor(1,FORWARD,120);
  m.motor(2,BACKWARD,120);
  m.motor(3,BACKWARD,120);
  m.motor(4,FORWARD,120); 
  delay(time);
  digitalWrite(13,LOW);
  stop();
}

void left(int time){
  digitalWrite(13,HIGH);
  m.motor(1,BACKWARD,120);
  m.motor(2,FORWARD,120);
  m.motor(3,FORWARD,120);
  m.motor(4,BACKWARD,120);  
  delay(time);
  digitalWrite(13,LOW);
  stop();
}

void forward(int time){
  m.motor(1,FORWARD,120);
  m.motor(2,FORWARD,120);
  m.motor(3,FORWARD,120);
  m.motor(4,FORWARD,120);  
  delay(time);
  stop();
}

void reverse(int time){
  m.motor(1,BACKWARD,120);
  m.motor(2,BACKWARD,120);
  m.motor(3,BACKWARD,120);
  m.motor(4,BACKWARD,120); 
  delay(time);
  stop();
}

void forward_right(int time){
   m.motor(1,FORWARD,90);
  m.motor(2,BACKWARD,120);
  m.motor(3,BACKWARD,120);
  m.motor(4,FORWARD,90);
  delay(time);
  stop();
}

void reverse_right(int time){
  m.motor(1,BACKWARD,120);
  m.motor(2,FORWARD,90);
  m.motor(3,FORWARD,120);
  m.motor(4,BACKWARD,120); 
  delay(time);
  stop();
}

void forward_left(int time){
   m.motor(1,FORWARD,120);
  m.motor(2,BACKWARD,90);
  m.motor(3,BACKWARD,90);
  m.motor(4,FORWARD,120);
  delay(time);
  stop();
}

void reverse_left(int time){

  m.motor(1,FORWARD,120);
  m.motor(2,BACKWARD,90);
  m.motor(3,BACKWARD,120);
  m.motor(4,FORWARD,120); 
  delay(time);
  stop();
}

void reset(){
  m.motor(1,BRAKE,0);
  m.motor(2,BRAKE,0);
  m.motor(3,BRAKE,0);
  m.motor(4,BRAKE,0); 
}
void send_command(int command, int time){
    switch(command)
  {
case 0: reset(); break;

     // single command
     case '1': forward(time); break;
     case '2': reverse(time); break;
     case '3': right(time); break;
     case '4': left(time); break;

     //combination command
     case '6': forward_right(time); break;
     case '7': forward_left(time); break;
     case '8': reverse_right(time); break;
     case '9': reverse_left(time); break;

     default: Serial.print("Inalid Command\n");

    
  }
}
