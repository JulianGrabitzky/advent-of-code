def get_file(file_name):
    with open(file_name) as f:
        passports = f.read().split("\n\n")
    return passports


def get_valid_passports(key_dict, passports):
    faulty_passports_task1, faulty_passports_task2 = 0, 0
    for passport in passports:
        passport = passport.replace("\n", " ")
        passport = passport.replace(" ", "\n")
        dict_from_line = {}
        for (key, value) in [x.split(":") for x in passport.split("\n")]:
            dict_from_line[key] = value

        if not set(key_dict.keys()).issubset(dict_from_line.keys()):
            faulty_passports_task1 += 1
            faulty_passports_task2 += 1
            continue

        for key, fun in key_dict.items():
            if not fun(dict_from_line[key]):
                faulty_passports_task2 += 1
                break

    return (
        len(passports) - faulty_passports_task1,
        len(passports) - faulty_passports_task2,
    )


def main():
    key_dict = {
        "byr": lambda inp: int(inp) in range(1920, 2003),
        "iyr": lambda inp: int(inp) in range(2010, 2021),
        "eyr": lambda inp: int(inp) in range(2020, 2031),
        "hgt": lambda inp: False
        if not any(x in inp for x in ["cm", "in"])
        else int(inp[:-2]) in range(150, 194)
        if inp[-2:] == "cm"
        else int(inp[:-2]) in range(59, 77),
        "hcl": lambda inp: len(inp) == 7
        and inp[0] == "#"
        and all(
            [
                char
                in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                ]
                for char in inp[1:]
            ]
        ),
        "ecl": lambda inp: inp in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda inp: len(inp) == 9,
    }
    task1, task2 = get_valid_passports(key_dict, get_file("4.txt"))
    print("Task 1: {}".format(task1))
    print("Task 2: {}".format(task2))


if __name__ == "__main__":
    main()