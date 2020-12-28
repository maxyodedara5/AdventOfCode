#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 
#include <map>	
#include <unordered_map>
using namespace std;

int GetNOPValue(string& line, int& accumulator, vector <string> ::iterator& it, map <int, int>& game, int& linenum);
int GetACCValue(string& line, int& accumulator, vector <string> ::iterator& it, map <int, int>& game, int& linenum);
int GetJMPValue(string& line, int& accumulator, vector <string> ::iterator& it, map <int, int>& game, int& linenum);

void Day8() {

	string line;
	ifstream myfile("Day8.txt");




	map <int, int> gameassembly;
	vector <string> listOfIns;
	vector <string> ::iterator currentpos;
	currentpos = listOfIns.begin();
	int linenum = 0;
	map <int, int> ::iterator it;
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{

			listOfIns.push_back(line);
			gameassembly.insert({ linenum , 0 });
			linenum++;
		}
	}
	myfile.close();

	currentpos = listOfIns.begin();
	linenum = 0;
	bool flag = true;
	int accumulator = 0;
	while (flag) {
		it = gameassembly.find(linenum);
		if (it->second == 0) {
			string cur = *currentpos;

			if (cur.find("nop") != std::string::npos) {
				accumulator = GetNOPValue(cur, accumulator, currentpos, gameassembly, linenum);
			}

			if (cur.find("acc") != std::string::npos) {
				accumulator = GetACCValue(cur, accumulator, currentpos, gameassembly, linenum);
			}

			if (cur.find("jmp") != std::string::npos) {
				accumulator = GetJMPValue(cur, accumulator, currentpos, gameassembly, linenum);
			}

		}
		else {
			flag = false;
			cout << accumulator << " is the current value before infi loop" << endl;
		}

	}
}

int GetNOPValue(string& line, int& accumulator, vector <string> ::iterator& it, map <int, int>& game, int& linenum) {
	int num;
	map <int, int> ::iterator newit;
	newit = game.find(linenum);
	newit->second = 1;
	/*if (line.find("+") != std::string::npos) {
		num = stoi(line.substr(line.find("+"), line.length()));
		if (num == 0) {
			it++;
			linenum++;
		}
		else {
			it += num;
			linenum += num;
		}
		accumulator += num;

	}
	else
	{
		num = stoi(line.substr(line.find("-"), line.length()));
		accumulator -= num;
		if (num == 0) {
			it++;
			linenum++;
		}
		else {
			it -= num;
			linenum -= num;
		}
	}*/

	it++;
	linenum++;
	return accumulator;
}

int GetACCValue(string& line, int& accumulator, vector <string> ::iterator& it, map <int, int>& game, int& linenum) {
	int num;
	map <int, int> ::iterator newit;
	newit = game.find(linenum);
	newit->second = 1;
	if (line.find("+") != std::string::npos) {
		num = stoi(line.substr(line.find("+"), line.length()));
		it++;
		linenum++;
		accumulator += num;

	}
	else
	{
		num = stoi(line.substr(line.find("-"), line.length()));
		accumulator += num;
		it++;
		linenum++;

	}

	return accumulator;
}

int GetJMPValue(string& line, int& accumulator, vector <string> ::iterator& it, map <int, int>& game, int& linenum) {
	int num;
	map <int, int> ::iterator newit;
	newit = game.find(linenum);
	newit->second = 1;
	if (line.find("+") != std::string::npos) {
		num = stoi(line.substr(line.find("+"), line.length()));
		it += num;
		linenum += num;
		//accumulator += num;

	}
	else
	{
		num = stoi(line.substr(line.find("-"), line.length()));
		//accumulator -= num;
		it += num;
		linenum += num;


	}

	return accumulator;
}