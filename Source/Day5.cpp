#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm> 

using namespace std;
void Day5() {

	string line;
	ifstream myfile("Day5.txt");
	//byr iyr eye hgt hcl ecl pid cid
		/*byr(Birth Year)
		iyr(Issue Year)
		eyr(Expiration Year)
		hgt(Height)
		hcl(Hair Color)
		ecl(Eye Color)
		pid(Passport ID)
		cid(Country ID)*/

	int valid = 0;
	int valid2 = 0;
	int current = 0;
	int biggest = 0;
	int planechart[128][8];

	for (size_t i = 0; i < 128; i++)
	{
		for (size_t j = 0; j < 8; j++)
		{
			planechart[i][j] = 0;

		}
	}



	if (myfile.is_open())
	{
		string passport;
		while (getline(myfile, line))
		{
			for (size_t i = 0; i < line.length(); i++)
			{
				if (line[i] == 'F') {
					line[i] = '0';
				}
				else if (line[i] == 'B') {
					line[i] = '1';
				}
				else if (line[i] == 'R') {
					line[i] = '1';
				}
				else if (line[i] == 'L') {
					line[i] = '0';
				}
			}

			//line = "1234567899";
			string firstpart = line.substr(0, 7);
			string secondpart = line.substr(7, 3);


			int num1 = std::stoi(firstpart, nullptr, 2);
			int num2 = std::stoi(secondpart, nullptr, 2);

			current = num1 * 8 + num2;
			if (current > biggest) {
				biggest = current;
			}

			planechart[num1][num2] = 1;

		}
	}

	for (size_t i = 0; i < 128; i++)
	{
		for (size_t j = 0; j < 8; j++)
		{
			cout << planechart[i][j] << "R" << i << " " << "C" << j << " ";
		}
		cout << endl;
	}
	cout << biggest;

	if (false) {
		if (myfile.is_open())
		{
			string passport;
			while (getline(myfile, line))
			{
				passport += line + " ";
				if (line == "") {

					bool byr, iyr, eyr, hgt, hcl, ecl, pid;
					byr = iyr = eyr = hgt = hcl = ecl = pid = false;
					if (passport.find("byr:") != std::string::npos) {

						int byrpos = passport.find("byr:");
						string birthyear = passport.substr(byrpos + 4, 5);
						int byrnum = stoi(birthyear);
						if (byrnum >= 1920 && byrnum <= 2002)
							byr = true;
					}

					if (passport.find("iyr:") != std::string::npos) {

						int iyrpos = passport.find("iyr:");
						string issueyear = passport.substr(iyrpos + 4, 5);
						int issnum = stoi(issueyear);
						if (issnum >= 2010 && issnum <= 2020)
							iyr = true;
					}

					if (passport.find("eyr:") != std::string::npos) {

						int eyrpos = passport.find("eyr:");
						string issueyear = passport.substr(eyrpos + 4, 5);
						int exsnum = stoi(issueyear);
						if (exsnum >= 2020 && exsnum <= 2030)
							eyr = true;
					}

					if (passport.find("hgt:") != std::string::npos) {

						int whole = passport.find(" ", passport.find("hgt:"));
						string height = passport.substr(passport.find("hgt:"), passport.find("hgt:") - whole);
						hgt = true;
					}

					if (passport.find("hcl:") != std::string::npos) {
						hcl = true;
					}

					if (passport.find("ecl:") != std::string::npos) {
						ecl = true;
					}

					if (passport.find("pid:") != std::string::npos) {
						pid = true;
					}

					if (byr == true && iyr == true && eyr == true && hgt == true && hcl == true && ecl == true && pid == true) {

						valid2++;

					}


					passport = "";
				}
			}
		}
		cout << valid2;
	}

	myfile.close();
}