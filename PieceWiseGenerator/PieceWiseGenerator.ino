#include "DualVNH5019MotorShield.h"
#include "PinChangeInt.h"
//#include <avr/interrupt.h>

DualVNH5019MotorShield md;
int inPinL = 11; // 3-> right   11-> left
int inPinR = 3;
volatile unsigned long time0_R,time1_R,time0_L,time1_L=0;
volatile double constant = 106714.09515, L=0, R=0;
int input=0, startValue = 70, increment = 30;
int FL[30], FR[30], BL[30], BR[30];
int index = 0;

void stopIfFault()
{
  if (md.getM1Fault())
  {
    Serial.println("M1 fault");
    while(1);
  }
  if (md.getM2Fault())
  {
    Serial.println("M2 fault");
    while(1);
  }
}

void Interrupt_L(void)
{
    time1_L = time0_L;
    time0_L = micros();
}
void Interrupt_R(void)
{
    time1_R = time0_R;
    time0_R = micros();
}

void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(50);
  md.init();
  PCintPort::attachInterrupt(inPinL,Interrupt_L,RISING);
  PCintPort::attachInterrupt(inPinR,Interrupt_R,RISING);
  md.setSpeeds(input,input);
  input = startValue;
}

      
void loop()
{
    if (input <= 400){
        md.setSpeeds(input,input);
        delay(2000);    //start motor
        noInterrupts();
        L = constant/(time0_L-time1_L);
        R = constant/(time0_R-time1_R); 
        interrupts();
        for (int i = 0;i<10;i++)
          sample();
        md.setSpeeds(0,0);
        L/=10;
        R/=10;
        Serial.print(input);Serial.print("\t");Serial.print(L);Serial.print("\t");Serial.println(R);
        
        
        if (input > 0){
          FL[index] = L;
          FR[index] = R;
          input *= (-1);
          }
        else{
          BL[index] = L;
          BR[index] = R;
          input -= increment;
          input *= (-1);
          index++;
        }
        delay(1000);
    }
    else{
      Serial.println("Done");
      while(1);
    }
}
void sample(){
    noInterrupts();    
    L += constant/(time0_L-time1_L);
    R += constant/(time0_R-time1_R); 
    interrupts();
    delay(20);    //sample
}
