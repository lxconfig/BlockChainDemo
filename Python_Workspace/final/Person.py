class Person:
    def __init__(self, name, dob, sex, zipcode, illness):
        self.name = name
        self.dob = dob
        self.sex = sex
        self.zipcode = zipcode
        self.illness = illness

    def __repr__(self):
        return "{0}, {1}, {2}, {3}, {4}\n".format(self.name, self.print_dob(), self.print_sex(), self.print_zipcode(), self.illness)

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(self.name, self.print_dob(), self.print_sex(), self.print_zipcode(), self.illness)

    def print_dob(self):
        filled_dob = self.dob
        to_fill = 8 - len(self.dob)
        for i in range(to_fill):
            filled_dob = filled_dob + '*'
        return filled_dob

    def print_sex(self):
        if self.sex == '':
            return '*'
        else:
            return self.sex

    def print_zipcode(self):
        filled_zipcode = self.zipcode
        to_fill = 5 - len(self.zipcode)
        for i in range(to_fill):
            filled_zipcode = filled_zipcode + '*'
        return filled_zipcode
