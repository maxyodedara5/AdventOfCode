//if (false) {
//	if (myfile.is_open())
//	{
//		string passport;
//		while (getline(myfile, line))
//		{
//			passport += line + " ";
//			if (line == "") {
//
//				bool byr, iyr, eyr, hgt, hcl, ecl, pid;
//				byr = iyr = eyr = hgt = hcl = ecl = pid = false;
//				if (passport.find("byr:") != std::string::npos) {
//
//					int byrpos = passport.find("byr:");
//					string birthyear = passport.substr(byrpos + 4, 5);
//					int byrnum = stoi(birthyear);
//					if (byrnum >= 1920 && byrnum <= 2002)
//						byr = true;
//				}
//
//				if (passport.find("iyr:") != std::string::npos) {
//
//					int iyrpos = passport.find("iyr:");
//					string issueyear = passport.substr(iyrpos + 4, 5);
//					int issnum = stoi(issueyear);
//					if (issnum >= 2010 && issnum <= 2020)
//						iyr = true;
//				}
//
//				if (passport.find("eyr:") != std::string::npos) {
//
//					int eyrpos = passport.find("eyr:");
//					string issueyear = passport.substr(eyrpos + 4, 5);
//					int exsnum = stoi(issueyear);
//					if (exsnum >= 2020 && exsnum <= 2030)
//						eyr = true;
//				}
//
//				if (passport.find("hgt:") != std::string::npos) {
//
//					int whole = passport.find(" ", passport.find("hgt:"));
//					string height = passport.substr(passport.find("hgt:"), passport.find("hgt:") - whole);
//					hgt = true;
//				}
//
//				if (passport.find("hcl:") != std::string::npos) {
//					hcl = true;
//				}
//
//				if (passport.find("ecl:") != std::string::npos) {
//					ecl = true;
//				}
//
//				if (passport.find("pid:") != std::string::npos) {
//					pid = true;
//				}
//
//				if (byr == true && iyr == true && eyr == true && hgt == true && hcl == true && ecl == true && pid == true) {
//
//					valid2++;
//
//				}
//
//
//				passport = "";
//			}
//		}
//	}
//	cout << valid2;
//}