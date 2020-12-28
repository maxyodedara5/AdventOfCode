#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 
#include <map>	
#include <unordered_map>
using namespace std;

void Day9() {

	string line;
	ifstream myfile("Day9.txt");

	vector <long long int> listOfIns, currentlist;


	int linenum = 0;
	bool work = true;
	map <int, int> ::iterator it;
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{



			listOfIns.push_back(stoll(line));


		}
	}
	myfile.close();
	int preamble = 25;

	currentlist = { listOfIns.begin() , listOfIns.begin() + 25 };
	vector <long long int> ::iterator currentpos;
	vector <long long int> ::iterator firstiter, seconditer;
	firstiter = currentlist.begin();
	seconditer = currentlist.begin();
	currentpos = listOfIns.begin() + preamble;
	bool badFound = true;

	while (firstiter != currentlist.end() && badFound == true) {

		while (seconditer != currentlist.end())
		{
			if (*firstiter == *seconditer) {
				seconditer++;
				continue;
			}
			else
			{
				if (*firstiter + *seconditer == *currentpos) {
					currentlist.erase(currentlist.begin());
					currentlist.push_back(*currentpos);
					firstiter = currentlist.begin();
					seconditer = currentlist.begin();

					currentpos++;
					//
				}
				seconditer++;
			}
		}
		firstiter++;
		if (firstiter == currentlist.end()) {
			cout << *currentpos;
			badFound = false;
		}
		seconditer = currentlist.begin();
	}
}

