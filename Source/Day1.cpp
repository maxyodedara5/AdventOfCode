
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 


using namespace std;


void Day1() {


	std::vector <int> numbers;


	//std::vector <int> numbers = { 1721 , 979 , 366 , 299 , 675 , 1456 };
	string line;
	ifstream myfile("InputNumbers.txt");
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{

			numbers.push_back(stoi(line));
		}
		myfile.close();
	}

	sort(numbers.begin(), numbers.end());

	std::vector<int>::reverse_iterator last = numbers.rbegin();


	/*while ( 2020 < (numbers[0] + numbers.back()) ) {
		numbers.pop_back();
	}*/

	while (2020 < (numbers[0] + numbers[1] + numbers.back()))
		numbers.pop_back();
	/*while (numberfound == false) {
		numberToFind = 2020 - *start;


		if (std::find(numbers.begin(), numbers.end(), numberToFind) != numbers.end()) {
			std::cout << "Element found";
			numberfound = true;
			cout << *start << endl;
			cout << numberToFind << endl;
		}
		else
		{
			start++;
		}

	}*/

	std::vector<int>::iterator start = numbers.begin();
	int count = 0;
	for (int i = 0; i < 46; i++)
	{
		for (int j = 0; j < 46; j++) {

			for (int k = 0; k < 46; k++)
			{
				if (numbers[i] + numbers[j] + numbers[k] == 2020) {
					cout << numbers[i] << numbers[j] << numbers[k];
				}
				count++;
			}
		}
	}
	cout << "Counted so many times " << count;

	//while (numberfound = true && number2found == true) {
	//	while (numberfound == false) {
	//		while (number2found == false) {

	//			if (number1 + number2 + number3 == 2020) {
	//				numberfound = true;
	//				number2found = true;
	//			}
	//			else {
	//				num3++;
	//			}
	//		}
	//		num2++;
	//	}
	//	start++;
	//}
}