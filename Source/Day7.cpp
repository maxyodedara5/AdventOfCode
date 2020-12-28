#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 
#include <map>	
#include <unordered_map>
using namespace std;
void Day7() {

	string line;
	ifstream myfile("Day7.txt");


	unordered_multimap <string, string> rules;
	unordered_map <string, int> rulestrack;
	unordered_map <string, int> shinytrack;

	unordered_map <string, string> ::iterator it;
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{

			//light red bags contain 1 bright white bag, 2 muted yellow bags.
			string bagname = line.substr(0, line.find("bags") - 1);
			rules.insert({ bagname, line.substr(line.find("contain") + 8 , line.length()) });
			it = rules.find(bagname);
			cout << "BAGNAME " << it->first << " \t\tCONTENT " << it->second << endl;

			if (line.find("shiny gold bag") != std::string::npos && line.find("shiny gold bags contain") == std::string::npos) {


				shinytrack.insert({ bagname,1 });
				//rulestrack.insert({ bagname,1 });
			}
			else
			{
				//shinytrack.insert({ bagname,0 });
				rulestrack.insert({ bagname,0 });
			}

		}

		cout << "Lists created ";
		vector <string> tochecknext;
		for (auto& y : shinytrack)
		{
			for (auto& x : rulestrack)
			{
				it = rules.find(x.first);
				if (it->second.find(y.first) != std::string::npos) {
					tochecknext.push_back(x.first);
				}
			}
		}
		/*
		bool allruleschecked = false;
		while (allruleschecked != true) {

			if () {

			}
		}
		*/

	}



	/*while (getline(myfile, line))
	{
		rules.push_back(line);
	}
	reverse(rules.begin(), rules.end());
	int shinybag = 0;
	map<string, int> listbags;
	for (size_t i = 0; i < rules.size(); i++)
	{
		if (rules[i].find("no other bags") != std::string::npos) {
			shinybag += 0;
			string bagname = rules[i].substr(0, rules[i].find("bags") - 1);
			listbags[bagname] = 0;
		}
		else
		{
			string bagname = rules[i].substr(0, rules[i].find("bags") - 1);
			map<string, int> ::iterator it = listbags.find(bagname);
			if (it == listbags.end())
			{

			}
		}


	}*/



	myfile.close();
}

