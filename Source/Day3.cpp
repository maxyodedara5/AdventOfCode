
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 


using namespace std;
void Day3() {

	string line;
	int treecount = 0;
	ifstream myfile("TreesDay3.txt");
	if (myfile.is_open())
	{
		int currentpos = 0;
		int lineNum = 0;
		while (getline(myfile, line))
		{


			// check slopes

				// check only even rows when slope down is 2
			if (lineNum % 2 == 0) {
				// check if tree in path
				if (line.at(currentpos % line.length()) == '#') {
					treecount++;
				}
				// increment column iterators
				currentpos += 1;
			}

			// increment line count
			lineNum++;



			//First solution
			/*if (line[currentpos % line.length()] == '#') {
				treecount++;
			}
			currentpos += 7;*/

		}
		cout << treecount;
		myfile.close();
	}
}