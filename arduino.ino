#include <LiquidCrystal_I2C.h>
#include <DHT.h>
#include <Wire.h> 

// Definimos el pin digital donde se conecta el sensor y el tipo de sensor
#define DHTPIN 9
#define DHTTYPE DHT22
// Inicializamos el sensor DHT11
DHT dht(DHTPIN, DHTTYPE);

// CONSTRUCTOR PARA LA PANTALLA LCD 16X2
//Crear el objeto lcd con dirección en hexadecimal tamaño 16 x 2
//LiquidCrystal_I2C lcd1(0x27,16,2);
LiquidCrystal_I2C lcd2(0x25,16,2);

// MEDIDOR DE pH
#define pHPIN A0
int sensorValue = 0; 
unsigned long int avgValue; 
float b;
int buf[10],temp;


void setup()
{
   // Inicializamos comunicación serie
  Serial.begin(9600);
  // Comenzamos el sensor DHT
  dht.begin();
  // Iinicializar lcd_i2c
  //lcd1.init();
  lcd2.init();
  //Encender la luz de fondo.
  //lcd1.backlight();
  lcd2.backlight();
}
 
void loop()
{
  // LEER TEMPERATURA Y HUMEDAD Y ESPERAR 5 SEGUNDOS
  float temperatura = dht.readTemperature();
  float humedad = dht.readHumidity();
  delay(5000);
  //lcd1.clear();
  lcd2.clear();

  //CORROBORAR ERROR EN SENSOR
//  if (temperatura>0){
  // MOVER EL CURSOR A LA POSICION(0, 0)
  //lcd1.setCursor(0,0);
  lcd2.setCursor(0,0);  
  // IMPRIMIR EN lcd1
  lcd2.print("T:");  lcd2.print(temperatura,1); lcd2.print("C ");// TEMPERATURA con 1 decimal
  lcd2.print(" H:");  lcd2.print(humedad,0); lcd2.print("%");// HUMEDAD sin decimales;  
//}
//else{
   // IMPRIMIR MENSAJE DE ERROR
  //lcd1.print("ERROR EN dht");
//  lcd2.setCursor(0,0); 
//  lcd2.print("ERROR EN DHT");
//}

for(int i=0;i<10;i++) 
 { 
  buf[i]=analogRead(pHPIN);
  delay(10);
 }
 for(int i=0;i<9;i++)
 {
  for(int j=i+1;j<10;j++)
  {
   if(buf[i]>buf[j])
   {
    temp=buf[i];
    buf[i]=buf[j];
    buf[j]=temp;
   }
  }
 }
 avgValue=0;
 //PROMEDIO DE LAS 6 MEDICIONES DEL MEDIO
 for(int i=2;i<8;i++) avgValue+=buf[i];
 float pHVol=(float)avgValue*5.0/1024/6;
 
 //    CALIBRACION
 float ph = -5.70 * pHVol + 21.34;
 lcd2.setCursor(0,1);
 lcd2.print("pH:");lcd2.print(ph);//lcd2.print("  T:00.0C");
 delay(20);

 //MANDAR DATOS AL PUERTO SERIE
  Serial.print(temperatura,1);
  Serial.print(" ;");
  Serial.print(humedad,1);
  Serial.print(" ;");
  Serial.print(ph,1);
  Serial.println(" ;");
  delay(1000);
}

  
