from utils import read_input

# day 4 seems to be about input validation
# so the ƒirst difficulty is reading this file

class Passport:
    def __init__(self, birth_year: str=None, issue_year: str=None, expir_year: str=None,
                 height: str=None, hair_colour: str=None, eye_colour: str=None,
                 pass_id: str=None, country_id: str=None) -> None:
        self.birth_year = birth_year
        self.issue_year = issue_year
        self.expir_year = expir_year
        self.height = height
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        self.pass_id = pass_id
        self.country_id = country_id
        
    def is_valid(self):
        VALID_EYE_CLR = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        valid_bir_year = self.birth_year != None and len(self.birth_year) == 4 and int(self.birth_year) >= 1920 and int(self.birth_year) <= 2002
        valid_iss_year = self.issue_year != None and len(self.issue_year) == 4 and int(self.issue_year) >= 2010 and int(self.issue_year) <= 2020
        valid_exp_year = self.expir_year != None and len(self.expir_year) == 4 and int(self.expir_year) >= 2020 and int(self.expir_year) <= 2030

        valid_h_inches = self.height != None and self.height[-2:] == "in" and int(self.height[:-2]) >=59 and int(self.height[:-2]) <= 76
        valid_h_cm = self.height != None and self.height[-2:] == "cm" and int(self.height[:-2]) >= 150 and int(self.height[:-2]) <= 193
        valid_height = valid_h_cm or valid_h_inches
        
        valid_hair = self.hair_colour != None and len(self.hair_colour) == 7 and self.hair_colour[0] == "#" and self.hair_colour[1:].isalnum()
        valid_eye = self.eye_colour != None and self.eye_colour in VALID_EYE_CLR
        valid_pid = self.pass_id != None and len(self.pass_id) == 9 and self.pass_id.isnumeric()
        
        return valid_bir_year and \
            valid_iss_year and \
                valid_exp_year and \
                    valid_height and \
                        valid_eye and \
                            valid_hair and \
                                valid_pid


if __name__ == "__main__":
    rows = read_input("day4")
    rows = [el.replace("\n", "") for el in rows]
    # print(rows)
    
    # inside rows, entries are separated by a "\n" entry
    # so the first thing to do is extract entries
    
    entries = []
    i, j = 0, 0
    while i != -1:
        try:
            j = rows.index("", i)
        except ValueError:
            break
        entries.append(" ".join(rows[i:j]).strip('\n'))
        i = j+1
    entries.append(" ".join(rows[i:j]).strip("\n"))
    
    valid_passports = 0
    # validate passports
    for entry in entries[:-1]:
        curr_passport = Passport()
        for kw_val in entry.split(" "):
            print(entry.split(" "))
            kw, val = kw_val.split(":")[0], kw_val.split(":")[1]
            if kw == "byr":
                curr_passport.birth_year = val
            elif kw == "iyr":
                curr_passport.issue_year = val
            elif kw == "eyr":
                curr_passport.expir_year = val
            elif kw == "hgt":
                curr_passport.height = val
            elif kw == "hcl":
                curr_passport.hair_colour = val
            elif kw == "ecl":
                curr_passport.eye_colour = val
            elif kw == "pid":
                curr_passport.pass_id = val
            elif kw == "cid":
                curr_passport.country_id = val
        if curr_passport.is_valid():
            valid_passports += 1
            
    print(valid_passports)
                