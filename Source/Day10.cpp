#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 
#include <map>	
#include <unordered_map>
using namespace std;

void Day10() {

	string line;
	ifstream myfile("Day10.txt");

	vector <int> listOfIns, currentlist;


	int linenum = 0;
	bool work = true;
	map <int, int> ::iterator it;
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{



			listOfIns.push_back(stoi(line));


		}
	}
	myfile.close();


	vector <int> ::iterator currentpos;
	sort(listOfIns.begin(), listOfIns.end());
	listOfIns.insert(listOfIns.begin(), 0);
	listOfIns.push_back(listOfIns.back() + 3);
	currentpos = listOfIns.begin();
	int diffOne = 0;
	int diffThree = 0;
	int diffTwo = 0;
	while (currentpos != listOfIns.end() - 1) {

		if (*currentpos + 1 == *(currentpos + 1))
		{
			diffOne++;
			currentpos++;
		}
		else if (*currentpos + 2 == *(currentpos + 1))
		{
			diffTwo++;
			currentpos++;
		}
		else if (*currentpos + 3 == *(currentpos + 1))
		{
			diffThree++;
			currentpos++;
		}

	}
	cout << diffOne << endl;
	cout << diffThree << endl;
	cout << diffOne * diffThree;
}

