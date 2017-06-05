/*
  The motors are connected to PIN 6,7,8,9
*/

void set_speed(int x,int y)
{
      
   analogWrite(6,x*255);
   analogWrite(7,y*255);
   analogWrite(8,x*255);
   analogWrite(9,y*255);
}


void setup()
{

  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  
  Serial.begin(57600);
}


void loop()
{ 
  if(Serial.available())
    {
      String xyz=Serial.readStringUntil('\r');
      if(xyz=="stop")
        set_speed(0,0);
      else if(xyz=="forward")
        set_speed(1,0);
      else if(xyz=="back")
        set_speed(0,1);
      else
        set_speed(0,0);
                
       Serial.flush();
    }
}
