
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 
using namespace std;
void Day2() {



	std::vector <int> numbers;


	int validpass = 0;
	string line;
	ifstream myfile("PasswordDay2.txt");
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{

			cout << (line);

			int colonat = line.find(":");
			string password = line.substr(colonat + 2, line.length());
			string limits = line.substr(0, colonat - 2);
			int hypenat = line.find("-");
			string lowerlimit = line.substr(0, hypenat);
			int spaceat = line.find(" ");
			string higherlimit = line.substr(hypenat + 1, spaceat - (hypenat + 1));

			int num1 = stoi(lowerlimit);
			int num2 = stoi(higherlimit);
			string key = line.substr(colonat - 1, 1);
			/*int currentcount = 0;
			for (int i = 0; i < password.length(); i++)
			{
				if (key[0] == password[i]) {
					currentcount++;
				}
			}
			if (currentcount < num1 || currentcount > num2) {

			}
			else {
				validpass++;
			}*/

			bool pos1 = false;
			bool pos2 = false;

			if (key[0] == password[num1 - 1])
				pos1 = true;
			if (key[0] == password[num2 - 1])
				pos2 = true;

			if (pos1 == pos2) {

			}
			else {
				validpass++;
			}
		}
		cout << validpass;
		myfile.close();
	}




}