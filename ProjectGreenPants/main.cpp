//Project GreenPants ~ John Butler

#include <iostream>
#include <cmath>
#include "rollbot.h"
#include<time.h>
using namespace std;

int main() {
	int test = 35;
	srand(time(0));

	attackRoll(60);
	cout << endl << endl;

	cout << flipDigits(test);

}