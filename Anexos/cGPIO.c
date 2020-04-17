#include <wiringPi.h>

int main(){
	
	if(wiringPiSetup()==-1){
		return 1;
	}
	
	pinMode(0,OUTPUT);
	while(1){
		digitalWrite(0,HIGH);
		digitalWrite(0,LOW);
	}
	return 0;
}
