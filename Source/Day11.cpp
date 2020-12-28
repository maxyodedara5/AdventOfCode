#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 
#include <map>	
#include <unordered_map>

using namespace std;
char checkSeat(char seat, int row, int col, vector<vector<char>> location);
void PrintLocation(vector<vector<char>> loca, int a, int b);
int Day11() {

	string line;
	ifstream myfile("Day11.txt");

	vector <string> listOfIns;
	vector < vector < char> > loc1, loc2;

	//reading the file input
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{
			listOfIns.push_back(line);
		}
	}
	myfile.close();

	//putting all data in 2d vector 
	for (size_t i = 0; i < listOfIns.size(); i++)
	{
		vector <char> current;
		for (size_t j = 0; j < listOfIns[i].length(); j++)
		{
			current.push_back(listOfIns[i][j]);
		}
		loc1.push_back(current);
	}

	//2 states to check for changes 
	loc2 = loc1;

	for (size_t i = 0; i < listOfIns.size(); i++)
	{

		for (size_t j = 0; j < listOfIns[i].length(); j++)
		{
			//cout << loc1[i][j] << "  ";
			if (loc1[i][j] != '.')
				loc1[i][j] = checkSeat(loc1[i][j], i, j, loc1);
			PrintLocation(loc1, listOfIns.size(), listOfIns[0].length());
		}
		cout << endl;
	}


	cout << "Asdf";
	return 0;
}

/*Cell-->Current Cell (row, col)
		N -->  North        (row-1, col)
		S -->  South        (row+1, col)
		E -->  East         (row, col+1)
		W -->  West            (row, col-1)
		N.E--> North-East   (row-1, col+1)
		N.W--> North-West   (row-1, col-1)
		S.E--> South-East   (row+1, col+1)
		S.W--> South-West   (row+1, col-1) */

		//check positions
char checkSeat(char seat, int row, int col, vector<vector<char>> location) {

	int occupied = 0;
	char toReturn;
	vector <char> a;
	try
	{
		if (row - 1 >= 0)
			a.push_back(location[row - 1][col]);
		a.push_back(location[row + 1][col]);
		a.push_back(location[row][col + 1]);
		if (col - 1 >= 0)
			a.push_back(location[row][col - 1]);
		if (row - 1 >= 0)
			a.push_back(location[row - 1][col + 1]);
		if (row - 1 >= 0 && col - 1 >= 0)
			a.push_back(location[row - 1][col - 1]);
		a.push_back(location[row + 1][col + 1]);
		if (col - 1 >= 0)
			a.push_back(location[row + 1][col - 1]);
	}
	catch (const std::exception&)
	{

	}

	for (size_t i = 0; i < a.size(); i++)
	{
		if (a[i] == '.') {
			continue;
		}
		if (a[i] == '#') {
			occupied++;
		}
	}

	if (occupied >= 4)
	{
		toReturn = 'L';
		return toReturn;
	}
	else
	{
		toReturn = '#';
		return toReturn;
	}


}

void PrintLocation(vector<vector<char>> loca, int a, int b) {

	cout << "-----------------------" << endl;

	for (int i = 0; i < a; i++)
	{

		for (int j = 0; j < b; j++)
		{
			cout << loca[i][j] << "  ";


		}
		cout << endl;
	}

	cout << "-----------------------" << endl;
}