#define trigPin1 6
#define echoPin1 7
#define trigPin2 10
#define echoPin2 11

int LED4 = 9;
int LED3 = 8;

int LED2 = 5;
int LED1 = 4;

char reference1[] = "0001001";
char reference2[] = "0001010";

void setup() {
   Serial.begin (9600);
   
   pinMode(LED1, OUTPUT);
   pinMode(LED2, OUTPUT);
  
   pinMode(trigPin1, OUTPUT);
   pinMode(echoPin1, INPUT);  
   
   pinMode(trigPin2, OUTPUT);
   pinMode(echoPin2, INPUT); 

   pinMode(LED3, OUTPUT);
   pinMode(LED4, OUTPUT);
}


void loop() {
  /*Distance sensor 1*/
  long duration1, distance1, duration2, distance2;
  digitalWrite(trigPin1, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  distance1 = (duration1/2) / 29.1;

  /*Distance sensor 2*/
  digitalWrite(trigPin2, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  distance2 = (duration2/2) / 29.1;
  
  /*sensor1*/
  Serial.print(reference1);
  
  
  /*Test sensor1*/  
   if (distance1 >10) {
    digitalWrite(LED1,HIGH);
    digitalWrite(LED2,LOW);
    Serial.print("0");
   }
   
   else {
    digitalWrite(LED1,LOW);
    digitalWrite(LED2,HIGH);
    Serial.print("1");
    }

   Serial.print(" ");
   Serial.print(reference2);

  /*Test sensor2*/  
   if (distance2 >10) {
    digitalWrite(LED3,HIGH);
    digitalWrite(LED4,LOW);
    Serial.println("0");
   }
   
   else {
    digitalWrite(LED3,LOW);
    digitalWrite(LED4,HIGH);
    Serial.println("1");
    }
    
    delay(1000);
 

}
