#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <math.h>
#include <stddef.h>
#include <termios.h>
#include <fcntl.h>
#include <sys/types.h>
#include <string.h>
#include "I2Cdev.h"
#include "MPU6050.h"
#include <stdlib.h>
// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for InvenSense evaluation board)
// AD0 high = 0x69

MPU6050 accelgyro;
int16_t ax, ay, az;
int16_t gx, gy, gz;
int fd;
float compl_gyrox=0;
float compl_gyroy=0;
float compl_gyroz=0;
void setup() {
    // initialize device
    printf("Initializing I2C devices...\n");
   accelgyro.initialize();

    // verify connection
    printf("Testing device connections...\n");
    printf(accelgyro.testConnection() ? "MPU6050 connection successful\n" : "MPU6050 connection failed\n");
}

void loop() {
    // read raw accel/gyro measurements from device
accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
float ax1=(float)ax/4096;
float ay1=(float)ay/4096;
float az1=(float)az/4096;    // these methods (and a few others) are also available
float gyrox = (float)gx/131;
float gyroy = (float)gy/131;
float gyroz = (float)gz/131;			
float angax = 57.295* atan(ax1 / sqrt(pow(ay1,2)+pow(az1,2)));
float angay = 57.295* atan(ay1 / sqrt(pow(ax1,2)+pow(az1,2)));
float angaz = 57.295* atan(sqrt(pow(ax1,2)+pow(ay1,2)) / az1);
compl_gyrox=((0.98)*(compl_gyrox + gyrox*0.001)+(0.02)*(angax));
compl_gyroy=((0.98)*(compl_gyroy + gyroy*0.001)+(0.02)*(angay));
compl_gyroz=((0.98)*(compl_gyroz + gyroz*0.001)+(0.02)*(angaz));

//float to string
char stringax1[10];
char stringay1[10];
char stringaz1[10];
char string_gyrox[10];
char string_gyroy[10];
char string_gyroz[10];
char string_compl_gyrox[10];
char string_compl_gyroy[10];
char string_compl_gyroz[10];

sprintf(stringax1,"%f",ax1);
sprintf(stringay1,"%f",ay1);
sprintf(stringaz1,"%f",az1);
sprintf(string_gyrox,"%f",gyrox);
sprintf(string_gyroy,"%f",gyroy);
sprintf(string_gyroz,"%f",gyroz);
sprintf(string_compl_gyrox,"%f",compl_gyrox);
sprintf(string_compl_gyroy,"%f",compl_gyroy);
sprintf(string_compl_gyroz,"%f",compl_gyroz);

  
//printf("a/g: %6.4f   %6.4f   %6.4f   %6.4f   %6.4f   %6.4f   %6.4f   %6.4f   %6.4f \n",ax1,ay1,az1,gyrox,gyroy,gyroz,compl_gyrox,compl_gyroy,compl_gyroz);
printf("%6.4f    %6.4f    %6.4f \n",ax1,ay1,az1);
write(fd,stringax1,8);
write(fd,stringay1,8);
write(fd,stringaz1,8);
//write(fd,string_gyrox,8);
//write(fd,string_gyroy,8);
//write(fd,string_gyroz,8);
//write(fd,string_compl_gyrox,8);
//write(fd,string_compl_gyroy,8);
//write(fd,string_compl_gyroz,8);
}

int main()
{
struct termios uart1,old;
char buf[30] = "/dev/ttyO4";
fd = open(buf, O_RDWR | O_NOCTTY);
	if(fd < 0) printf("port failed to open\n");
        tcgetattr(fd,&old);
	bzero(&uart1,sizeof(uart1));

	uart1.c_cflag = B9600 | CS8 | CLOCAL | CREAD;
	uart1.c_iflag = IGNPAR | ICRNL;
	uart1.c_oflag = 0;
	uart1.c_lflag = 0;

	uart1.c_cc[VTIME] = 0;
	uart1.c_cc[VMIN]  = 1;
        tcflush(fd,TCIFLUSH);
	tcsetattr(fd,TCSANOW,&uart1);

    setup();
    for (;;)
{

loop();
usleep(100000);
}
}

