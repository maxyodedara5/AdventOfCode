#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 
#include <unordered_set>
#include <array>
using namespace std;
void Day6() {

	string line;
	ifstream myfile("Day6.txt");

	if (myfile.is_open())
	{
		string currentgroup;
		string prestring;
		unordered_set<char> groupans;
		int total = 0;
		vector <char> previousline;
		vector <char> nextline;
		vector <char> disline;

		int numpeople = 0;
		string totalline;
		int finalcount[26] = { 0 };
		int secondans = 0;
		while (getline(myfile, line))
		{


			if (line == "") {

				for (size_t i = 0; i < totalline.length(); i++)
				{
					finalcount[int(totalline[i]) - 97]++;
				}

				for (size_t i = 0; i < 26; i++)
				{
					if (numpeople == finalcount[i]) {
						secondans++;
					}
				}

				numpeople = 0;
				totalline = "";
				for (size_t i = 0; i < 26; i++)
				{
					finalcount[i] = 0;
				}

			}
			else {
				totalline += line;

				numpeople++;
			}


			//for (size_t i = 0; i < prestring.length(); i++)
			//{
			//	previousline.push_back(prestring[i]);
			//}
			//
			//nextline.clear();
			//for (size_t i = 0; i < line.length(); i++)
			//{
			//	nextline.push_back(line[i]);
			//}
			////p 6 n 8 
			//if (prestring != "" && line != "")
			//if (previousline.size() > nextline.size()) {
			//	for (size_t i = 0; i < nextline.size(); i++)
			//	{
			//		if (prestring.find(nextline[i]) != string::npos){
			//			disline.push_back(nextline[i]);
			//		}
			//	}
			//}
			//else
			//{
			//	for (size_t i = 0; i < previousline.size(); i++)
			//	{
			//		if (line.find(previousline[i]) != string::npos) {
			//			disline.push_back(previousline[i]);
			//		}
			//	}

			//}

			//total += disline.size();
			//

			//prestring = line;


		}
		cout << secondans;
	}


	/*if (myfile.is_open())
	{
		string currentgroup;
		unordered_set<char> groupans;
		int total = 0;
		while (getline(myfile, line))
		{
			currentgroup += line;
			if (line == "") {

				for (size_t i = 0; i < currentgroup.length(); i++)
				{
					groupans.insert(currentgroup[i]);
				}

				total += groupans.size();
				cout << total << endl;
				groupans.clear();
				currentgroup = "";
			}

		}
		cout << total;
	}*/




	myfile.close();
}