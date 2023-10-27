
const int posicionInicial[] = {40,30,30};
int posicionActual[] = {40,30,30};
const int motor1_I = 6;
const int motor1_D = 7;
const int motor2_I = 8;
const int motor2_D = 9;

void setup()  
{
    pinMode(motor1_I,OUTPUT);
    pinMode(motor1_D,OUTPUT);
    pinMode(motor2_I,OUTPUT);
    pinMode(motor2_D,OUTPUT);
    Serial.begin(9600);
}

void loop() 
{
    #rutina
    moverMotor(1,50);
    moverMotor(2,20);

    #regresar a home
    moverMotor(1,40);
    moverMotor(2,30)
}

void moverMotor(int motor, int grados){

    int movimiento = posicionActual[motor-1] - grados;
    
    switch (motor)
    {
    case 1:
        if(movimiento < 0){
            movimiento = abs(movimiento)
            int tiempo = grados(movimiento);
            posicionActual[0] = movimiento;
            digitalWrite(motor1_I, HIGH);
            delay(movimiento*5);
            digitalWrite(motor1_I, LOW);        
        }
        else{
            int tiempo = grados(movimiento);
            posicionActual[0] = movimiento;
            digitalWrite(motor1_D, HIGH);
            delay(movimiento*5);
            digitalWrite(motor1_D, LOW);        
        }
        break;
    case 2:
        if(movimiento < 0){
            int tiempo = grados(abs(movimiento));
            posicionActual[1] = movimiento;
            digitalWrite(motor2_I, HIGH);
            delay(movimiento*5);
            digitalWrite(motor2_I, LOW);        
        }
        else{
            int tiempo = grados(movimiento);
            posicionActual[1] = movimiento;
            digitalWrite(motor2_D, HIGH);
            delay(movimiento*5);
            digitalWrite(motor2_D, LOW);        
        }
        break;
    default:
        break;
    }
        
}

int grados(int grados){
    return grados/5;
}