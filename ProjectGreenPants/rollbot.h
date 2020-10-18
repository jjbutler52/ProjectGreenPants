#pragma once
//Project 1 COP3014 John Butler

//Project GreenPants ~ John Butler

#ifndef ROLLBOT_H
#define ROLLBOT_H
#include<cmath>
#include<string>

	int attackRoll(int skill);
	int defendRoll(int skill);
	int flipDigits(int toBeFlipped);
	int successLevel(int skill, int roll);
	
	bool isCrit(int roll, int SL);
	bool isImpaled(int roll, int SL);
	bool isFumble(int roll, int SL);
	
	std::string targetLocation(int location);
	std::string beastLocation(int location);
	
	void printAttack(bool wasFumble, bool wasCrit, bool wasImpaled, int SL, int Roll, int location);
	
	


#endif