int light1=2, light2=3, light3=4, light4=5, light5=6, motor=7, gate=8, fan1=9, fan2=10, fan3=11;
int light1s=0,light2s=0,light3s=0,light4s=0,light5s=0, motors=0,gates=0, fan1s=0, fan2s=0,  fan3s=0;
int ldrpin=A0, ldr_active=0;
int irpin=12, buzzer=13, buzzers=0;
void setup() {
 Serial.begin(9600);
for(int i=2; i<12;i++){
  pinMode(i, OUTPUT);
 }
pinMode(irpin, INPUT);
pinMode(buzzer, HIGH);
}

void loop() {
  
 int a=Serial.read();
if(a>0){
 switch(a){
  case 48 : light1c();break;
  case 49 : light2c(); break;
  case 50 : light3c(); break;
  case 51 : light4c(); break;
  case 52 : light5c(); break;
  case 53 : fan1c(); break;
  case 54 : fan2c(); break;
  case 55 : fan3c(); break;
  case 56 : gatec(); break;
  case 57 : motorc();break;
  case 97 : fan1control(1);break;
  case 98 : fan1control(2);break;
  case 99 : fan1control(3);break;
  case 100 : fan1control(4);break;
  case 101 : fan1control(5);break;
  case 102 : fan2control(1);break;
  case 103 : fan2control(2);break;
  case 104 : fan2control(3);break;
  case 105 : fan2control(4);break;
  case 106 : fan2control(5);break;
  case 107 : fan3control(1);break;
  case 108 : fan3control(2);break;
  case 109 : fan3control(3);break;
  case 110 : fan3control(4);break;
  case 111 : fan1control(5);break;
  case 112 : buzzers=1;break;
  case 113 : shut_down();break;
  default: bydefault();
 }
 
}
int ldr=analogRead(ldrpin);
 if((ldr<200)&&(ldr_active==0))
 {
 digitalWrite(light5, HIGH);
 Serial.println("LIGHT ON");
 ldr_active=1;
 light5s=1;
}
else if(ldr>700){
  ldr_active=0;
    digitalWrite(light5, LOW);
   light5s=0;
}

int irread=digitalRead(irpin);
if (irread){
  Serial.println("Someone AT the DOOR");
  if(buzzers==0){
    
  digitalWrite(buzzer, HIGH);
  }
}else if (buzzers==1)
  digitalWrite(buzzer, LOW);
  buzzers=0;
}

void light1c(){
  if(light1s==0){
    digitalWrite(light1, HIGH);
    light1s=1;
    return;
  }
  else if(light1s==1){
    digitalWrite(light1, LOW);
    light1s=0;
    return;
  }
}

void light2c(){
  if(light2s==0){
    digitalWrite(light2, HIGH);
    light2s=1;
    return;
  }
  else if(light2s==1){
    digitalWrite(light2, LOW);
    light2s=0;
    return;
  }
}
void light3c(){
  if(light3s==0){
    digitalWrite(light3, HIGH);
    light3s=1;
    return;
  }
  else if(light3s==1){
    digitalWrite(light3, LOW);
    light3s=0;
    return;
  }
}

void light4c(){
  if(light4s==0){
    digitalWrite(light4, HIGH);
    light4s=1;
    return;
  }
  else if(light4s==1){
    digitalWrite(light4, LOW);
    light4s=0;
    return;
  }
}

void light5c(){
  if(light5s==0){
    digitalWrite(light5, HIGH);
    light5s=1;
    return;
  }
  else if(light5s==1){
    digitalWrite(light5, LOW);
    light5s=0;
    return;
  }
}
void fan1c(){
  if(fan1s==0){
    //digitalWrite(fan1, HIGH);
    fan1s=1;
    return;
  }
  else if(fan1s==1){
 digitalWrite(fan1, LOW);
    fan1s=0;
    return;
  }
}

void fan2c(){
  if(fan2s==0){
  //  digitalWrite(fan2, HIGH);
    fan2s=1;
    return;
  }
  else if(fan2s==1){
   digitalWrite(fan2, LOW);
    fan2s=0;
    return;
  }
}

void fan3c(){
  if(fan3s==0){
   // digitalWrite(fan3, HIGH);
    fan3s=1;
    return;
  }
  else if(fan3s==1){
    digitalWrite(fan3, LOW);
    fan3s=0;
    return;
  }
}
void gatec(){
  if(gates==0){
    digitalWrite(gate, HIGH);
    gates=1;
    return;
  }
  else if(gates==1){
    digitalWrite(gate, LOW);
    gates=0;
    return;
  }
}

void motorc(){
  if(motors==0){
    digitalWrite(motor, HIGH);
    motors=1;
    return;
  }
  else if(motors==1){
    digitalWrite(motor, LOW);
    motors=0;
    return;
  }
}

void fan1control(int i){
  if(fan1s==1){
int    b=i*51;
    analogWrite(fan1,b);
    return;
  }
  else
  analogWrite(fan1,0);
  return;
}
void fan2control(int i){
  if(fan2s==1){
int    b=i*51;
    analogWrite(fan2,b);
    return;
  }
  else
  analogWrite(fan2,0);
  return;
}
void fan3control(int i){
  if(fan3s==1){
int    b=i*51;
    analogWrite(fan3,b);
    return;
  }
  else
  analogWrite(fan3,0);
  return;
}
void shut_down(){
  for (int i=0; i<12; i++){
    digitalWrite(i, LOW);
    
  }
  digitalWrite(13, LOW);
  light1s=0;
  light2s=0;
  light3s=0;
  light4s=0;
  light5s=0;
  motors=0;
  gates=0;
  fan1s=0;
  fan2s=0;
  fan3s=0;
  
return;}

void bydefault(){
  Serial.println(" Command NOT found");
}

