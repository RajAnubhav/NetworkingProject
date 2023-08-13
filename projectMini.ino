#define ledPin 12
#define buzzPin 13
const int motorAPin1 = 4;
const int motorAPin2 = 5;
// char data[3] = {'0', 'a', '\n'};
String data = "0a";
void setup() {
  pinMode(motorAPin1, OUTPUT);
  pinMode(motorAPin2, OUTPUT);
  // pinMode(motorAEnablePin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  pinMode(buzzPin, OUTPUT);
  digitalWrite(buzzPin, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    data = Serial.readString();
    if (data[0] == '1' && data[1] == 'f') {
      digitalWrite(ledPin, LOW);
      Serial.println("LED: OFF");
    } else if (data[0] == '1' && data[1] == 'o') {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED: ON");
    } else if (data[0] == '2' && data[1] == 'f') {
      digitalWrite(buzzPin, LOW);
      Serial.println("Buzzer: OFF");
    } else if (data[0] == '2' && data[1] == 'o') {
      digitalWrite(buzzPin, HIGH);
      Serial.println("Buzzer: ON");
    } else if (data[0] == '3' && data[1] == 'o') {
      digitalWrite(motorAPin1, HIGH);
      Serial.println("Motor: ON --> Forward");
      delay(2000);
    } else if (data[0] == '3' && data[1] == 'f') {
      digitalWrite(motorAPin1, LOW);
      Serial.println("Motor: OFF --> Forward");
      delay(2000);
    } else if (data[0] == '4' && data[1] == 'o') {
      digitalWrite(motorAPin2, HIGH);
      Serial.println("Motor: ON --> Backward");
      delay(2000);
    } else if (data[0] == '4' && data[1] == 'f') {
      digitalWrite(motorAPin2, LOW);
      Serial.println("Motor: OFF --> Backward");
      delay(2000);
    }
  }
}

void buzzBuzzer(unsigned int duration) {
  digitalWrite(buzzPin, HIGH);  // Turn on the buzzer
  delay(duration);              // Buzz for the specified duration
  digitalWrite(buzzPin, LOW);   // Turn off the buzzer
}