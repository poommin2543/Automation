int x = 0;
void setup() {
 pinMode(led,OUTPUT);
 Serial.begin(115200);
 Serial.setTimeout(1);
}

void loop(){
 while(!Serial.available());
 x = Serial.readString().toInt();
 if(x == 1){
  digitalWrite(led, HIGH);   
 }else if(X == 0){
  digitalWrite(led, LOW);    
 }
 Serial.print(x);
}