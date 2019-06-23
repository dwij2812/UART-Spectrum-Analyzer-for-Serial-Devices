/*****************************************************
Getting Started Guide for Zedboard
This demo displays the status of the switches on the
LEDs and prints a message to the serial communication
when a button is pressed.

Terminal Settings:
   -Baud: 115200
   -Data bits: 8
   -Parity: no
   -Stop bits: 1

7/25/16: Created by JonP
****************************************************/
#include <stdio.h>
#include "platform.h"
#include <xgpio.h>
#include "xparameters.h"
#include "sleep.h"
#include "math.h"
#define PI 3.14159265
#define RAND_MAX 0x7fffffff

int main()
{
	double x, ret, val;
   XGpio input, output;
   int button_data = 0;
   int switch_data = 0;

   XGpio_Initialize(&input, XPAR_AXI_GPIO_0_DEVICE_ID);	//initialize input XGpio variable
   XGpio_Initialize(&output, XPAR_AXI_GPIO_1_DEVICE_ID);	//initialize output XGpio variable

   XGpio_SetDataDirection(&input, 1, 0xF);			//set first channel tristate buffer to input
   XGpio_SetDataDirection(&input, 2, 0xF);			//set second channel tristate buffer to input

   XGpio_SetDataDirection(&output, 1, 0x0);		//set first channel tristate buffer to output

   init_platform();
   x=0;
   val = PI / 180;
   float noise;
   float b=0;
   float a=1;
   float t=10;
   float f=0;
   float n=0;
   scanf("%f %f %f %f",&a, &f, &n, &b);
   t=360/n;
   printf("%f %f %f %f\r\n",a,f,t,b);
   while(1){
	  noise = (float)rand()/(float)(RAND_MAX/0.5);
	  ret = a*sin(x*val)+b*noise;
      printf("%f\r\n",ret);
      usleep(1000000/(f*n));			//delay
      if(x<360){
    	  x+=t;
      }
      else{
    	  x=0;
      }
   }
   cleanup_platform();
   return 0;
}
