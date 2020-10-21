//Project GreenPants ~ John Butler

#include "rollbot.h"
#include <iostream>
#include <cmath>
#include <time.h>
#include <string>
#include <sstream>
using namespace std;

int combatRoll(int skill, bool wasAttack)
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
	//bool wasAttack = false; // set in a fixed position for testing

	std::string response = printAttack(wasAttack, wasFumble, wasCrit, wasImpaled, sl, roll, location);
	cout << response << endl;

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
		return "Off Arm";
	}

	else if (location < 45)
	{
		return "Main Arm";
	}

	else if (location < 80)
	{
		return "Body";
	}

	else if (location < 90)
	{
		return "L-Leg";
	}

	else if (location <= 100)
	{
		return "R-Leg";
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
		return "FL-Leg";
	}

	else if (location < 79)
	{
		return "FR-Leg";
	}

	else if (location < 90)
	{
		return "BL-Leg";
	}

	else if (location <= 100)
	{
		return "BR-Leg";
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

std::string printAttack(bool wasAttack, bool wasFumble, bool wasCrit, bool wasImpaled, int SL, int roll, int location)
{
	std::string target;
	std::string beast;
	std::stringstream str;

	if (wasAttack)
	{
		str << "[ATT @John] ";
	}
	else
	{
		str << "[DEF @John] ";
	}

	if (SL > 0)
	{
		str << "[SL:+" << SL << "] " ;
	}
	else
	{
		str << "[SL:" << SL << "] ";
	}

	if (wasCrit)
	{
		str << "{CRIT!} ";
	}

	if (wasImpaled)
	{
		str << "{IMPALE!} ";
	}

	if (wasFumble)
	{
		str << "{FUMBLE!} ";
	}
	else if (!wasFumble)
	{
		target = targetLocation(location);
		beast = beastLocation(location);
		str << "[Bi:" << target << "|Quad:"  << beast<< "]";
	}
	str << " [Roll:" << roll << "] ";
	return str.str();
}

