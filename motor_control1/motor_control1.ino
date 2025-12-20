
const int enable1Pin = 2;
const int motor1Pin1 = 4;   
const int motor1Pin2 = 3;  

const int enable2Pin = 7;
const int motor2Pin1 = 5;   
const int motor2Pin2 = 6;   

const String KritikSag = "rh";
const String KritikSol = "lh";
const String KritikSagSol = "bh";

const String UyariSag  = "rw";
const String UyariSol  = "lw";
const String UyariSagSol = "bw";

const String UzakSag  = "rm";
const String UzakSol  = "lm";   
const String UzakSagSol = "bm";

const String Stop = "ss";

void TitresimAyarla(String command)
{
  
  if (command == KritikSag) {
    Serial.println("Sag kritik calisti");
    Sag_motor(200);
    Sol_motor(0);

    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                      
    
    digitalWrite(LED_BUILTIN, LOW);   
    delay(1000);  
  }
  else if (command == KritikSol) 
  {
    Serial.println("Sol kritik calisti"); 
    Sag_motor(0);
    Sol_motor(200);  

    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                       
    
    digitalWrite(LED_BUILTIN, LOW);   
    delay(1000);  
  }
  
  else if (command == KritikSagSol)
  {
    Serial.println("SagSol kritik calisti");
    Sag_motor(200);
    Sol_motor(200);

    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                      
    
    digitalWrite(LED_BUILTIN, LOW);   
    delay(1000);  
  }

  else if (command == UyariSag) 
  {
    Serial.println("Sag Uyari calisti"); 
    Sag_motor(150);
    Sol_motor(0);
    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                       
    
    digitalWrite(LED_BUILTIN, LOW);    
    delay(1000);  
  }
  else if (command == UyariSol) 
  {
    Serial.println("Sol Uyari calisti"); 
    Sol_motor(150);
    Sag_motor(0);
    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                     
    
    digitalWrite(LED_BUILTIN, LOW);    
    delay(1000);  
  }
  else if (command == UyariSagSol)
  {
    Serial.println("SagSol Uyari calisti");
    Sag_motor(150);
    Sol_motor(150);

    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                      
    
    digitalWrite(LED_BUILTIN, LOW);    
    delay(1000);  
  }

  else if (command == UzakSag) 
  {Serial.println("Sag Uzak calisti"); 
  Sag_motor(100);
  Sol_motor(0);

  digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                      
    
    digitalWrite(LED_BUILTIN, LOW);   
    delay(1000);  
  }
  else if (command == UzakSol) 
  {
    Serial.println("Sol Uzak calisti");
    Sol_motor(100);
    Sag_motor(0);

    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                      
    
    digitalWrite(LED_BUILTIN, LOW);    
    delay(1000);  
  }
  else if (command == UzakSagSol)
  {
    Serial.println("SagSol Uzak calisti");
    Sag_motor(100);
    Sol_motor(100);

    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                      
    
    digitalWrite(LED_BUILTIN, LOW);    
    delay(1000);  
  }

  else if (command == Stop)
  {
    Serial.println("Motorlar durdu.");
    Sag_motor(0);
    Sol_motor(0);

    digitalWrite(LED_BUILTIN, HIGH); 
    delay(1000);                     
    
    digitalWrite(LED_BUILTIN, LOW);   
    delay(1000);  
  }
}


void Sag_motor(int rate)
{
  // Motorları ileri hareket ettir
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);  
  analogWrite(enable2Pin, rate);  
}

void Sol_motor(int rate)
{
  // Motorları ileri hareket ettir
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  analogWrite(enable1Pin, rate);  
}

void setup() {
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);  
  pinMode(motor2Pin1, OUTPUT);  
  pinMode(motor2Pin2, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(enable1Pin, OUTPUT);
  pinMode(enable2Pin, OUTPUT);


  Serial.begin(9600);

  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);

}

void loop() {
  if (Serial.available() > 0) {
     String read_command = Serial.readString();
     Serial.println(read_command);
     read_command.trim(); 
     TitresimAyarla(read_command);
    /*Sag_motor(200);
    Sol_motor(200);
    */
}
}
