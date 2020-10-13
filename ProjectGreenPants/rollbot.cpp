//Project GreenPants ~ John Butler

#include "rollbot.h"
#include <iostream>
#include <cmath>
#include <time.h>
#include <string>
using namespace std;

int attackRoll(int skill)
{
	
	int roll = 0;
	int sl = 0;
	int location = 0;
	

	roll = rand() % 100 + 1;
	sl = successLevel(skill, roll);
	location = flipDigits(roll);

	isCrit(roll, sl);
	isImpaled(roll, sl);
	isFumble(roll, sl);

	bool wasCrit = isCrit(roll, sl);
	bool wasImpaled = isImpaled(roll, sl);
	bool wasFumble = isFumble(roll, sl);

	printAttack(wasFumble, wasCrit, wasImpaled, sl, roll, location);


	
	/*
	cout <<"original roll is: " <<  roll << endl; // test line
	cout << "flipped roll: " << flipDigits(roll) << endl ;
	cout << "Target location is: " << targetLocation(location) << endl;
	cout << "Beast location is: " << beastLocation(location) << endl;

	cout << "Success Level is: ";

		
	
	if (isCrit(roll, sl))
	{
		cout << "(CRIT) SL is: +" << sl;
	}

	else if ((sl < 0) && isCrit(roll, sl))
	{
		cout << "(FUMBLE!) SL is: " << sl;
	}
	
	else if ((sl > 0) && !isCrit(roll, sl))
	{
		cout << "SL is: +" << sl;
	}
	
	else if ((sl < 0) && !isCrit(roll, sl))
	{
		cout << "SL is: " << sl;
	}

	else if ((sl > 0) && isImpaled(roll, sl))
	{
		cout << "SL is: +" << sl;
	}

	else if ((sl < 0) && isImpaled(roll, sl))
	{
		cout << "SL is: " << sl;
	}

	else
	{
		cout << "ERROR";
	}
	
	*/


	return roll;
}

int flipDigits(int flippee)
{
	int ones = 0;
	int tens = 0;
	int flippedDigit = 0;


	ones = flippee % 10;
	tens = flippee / 10;
	flippedDigit = (ones * 10) + tens;

	return flippedDigit;
}

bool isCrit(int roll, int SL)
{
	if (roll % 11 == 0 && SL >= 0)
	{
		return true;
	}
	else
		return false;
}

bool isImpaled(int roll, int SL)
{
	if (roll % 10 == 0 && SL >= 0)
	{
		return true;
	}

	else
		return false;

}

bool isFumble(int roll, int SL)
{
	if (roll % 11 == 0 && SL < 0)
	{
		return true;
	}
	else
		return false;
}

std::string targetLocation(int location)
{
	
	if (location < 10)
	{
		return "Head";
	}

	else if (location < 25)
	{
		return "Left/Secondary Arm";
	}

	else if (location < 45)
	{
		return "Right/Primary Arm";
	}

	else if (location < 80)
	{
		return "Body";
	}

	else if (location < 90)
	{
		return "Left Leg";
	}

	else if (location <= 100)
	{
		return "Right Leg";
	}

	else
	{
		return "ERROR";
	}
}

std::string beastLocation(int location)
{

	if (location < 17)
	{
		return "Head";
	}

	else if (location < 57)
	{
		return "Body";
	}

	else if (location < 68)
	{
		return "Front Left Leg";
	}

	else if (location < 79)
	{
		return "Front Right Leg";
	}

	else if (location < 90)
	{
		return "Back Left Leg";
	}

	else if (location <= 100)
	{
		return "Back Right Leg";
	}

	else
	{
		return "ERROR";
	}
}

int successLevel(int skill, int roll) 
{
	int success = 0;
	roll = roll / 10;
	skill = skill / 10;

	success = skill - roll;

	return success;
}

void printAttack(bool wasFumble, bool wasCrit, bool wasImpaled, int SL, int roll, int location)
{
	std::string target;
	std::string beast;

	if (SL > 0)
	{
		cout << "SL: +" << SL << " ";
	}
	else
	{
		cout << "SL: " << SL << " ";
	}

	cout << "Roll: " << roll << " ";

	if (wasCrit)
	{
		cout << "(CRIT!) ";
	}

	if (wasImpaled)
	{
		cout << "(IMPALE!) ";
	}

	if (wasFumble)
	{
		cout << "(FUMBLE!) ";
	}

	 target = targetLocation(location);
	 beast = beastLocation(location);
	 cout << "Hit: " << target << "/" << beast;
}

