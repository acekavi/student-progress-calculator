class CharInput:
    def __init__(self, question, param):
        self.question = question
        self.param = param

    def int_input(self):
        while True:
            try:
                x = int(input(f"{self.question} : "))

                if x in self.param:
                    return x
                else:
                    print(f"Please enter a value in range of {self.param}")

            except ValueError:
                print("Sorry only integers are allowed, try again!")

    def str_input(self):
        while True:
            try:
                x = input(f"{self.question} : ").lower()

                if x in self.param:
                    return x
                else:
                    print(f"Please enter a value of {self.param}")

            except ValueError:
                print("Sorry incorrect value, try again!")


def student_progress_cal():
    while True:
        credits_list = []
        for i in ["pass", "defer", "fail"]:
            x = CharInput(f"Please enter your credits at {i}", (0, 20, 40, 60, 80, 100, 120)).int_input()
            credits_list.append(x)

        if sum(credits_list) == 120:
            if credits_list[0] == 120:
                return "Progress"

            elif credits_list[0] == 100 and (credits_list[1] or credits_list[2]) == 20:
                return "Progress (module trailer)"

            elif credits_list[2] >= 80:
                return "Excluded"

            else:
                return "Do not progress – module retriever"

        else:
            print("Total incorrect.")


class Histograms:
    def __init__(self,hist_list):
        self.hist_list = hist_list

    def vert_histogram(self):
        no_of_progress = self.hist_list.count('progress')
        no_of_progress_mt = self.hist_list.count('progress (module trailer)')
        no_of_not_progress = self.hist_list.count('do not progress – module retriever')
        no_of_excluded = self.hist_list.count('excluded')
        return f"""
        ------------------------------------------------------------------------------------------------------------------------------
        Horizontal Histogram
        Progress    {no_of_progress}    : {no_of_progress * "*"}
        Trailer     {no_of_progress_mt}     : {no_of_progress_mt * "*"}
        Retriever   {no_of_not_progress}    : {no_of_not_progress * "*"}
        Excluded    {no_of_excluded}    : {no_of_excluded * "*"}

        {len(self.hist_list)} outcomes in total.
        ------------------------------------------------------------------------------------------------------------------------------
                    """
class ForStaff:
    def manual():
        histogram_list = []
        while True:
            histogram_list.append(student_progress_cal().lower())
            print("\nWould you like to enter another set of data?")
            choice = CharInput("Enter 'y' for yes or 'q' to quit and view results", ("y", "q")).str_input()
            if choice == "y":
                continue

            else:
                print(Histograms(histogram_list).vert_histogram())

    def automatic():
        lines = []
        with open("dataset.txt") as file:
            for line in file:
                line = line.strip()  # Striping the file line by line
                lines.append(line)  # storing everything in a list

        # Getting the striped lines and spliting them again and adding line by line to a new list
        records = []
        records_new = []
        for i in lines:
            records.append(i.split(","))
            for e in i:
                records_new.append(i.split("="))


        new_list = []
        for i in records_new:
            try:
                new_list.append(int(i))
            except ValueError:
                pass
            except TypeError:
                pass


        print(lines)
        print(records_new)
        print(new_list)

------------------------------------------------------------------

all_char = []
        for elem in lines:
            x = elem.split(" ")
            for word in x:
                y = word.split(",")
                all_char.append(y)

        new_list = []
        for i in all_char:
            for char in i:
                try:
                    new_list.append(int(i))
                except ValueError:
                    pass
                except TypeError:
                    pass


#------------------------------------------------------------------------------------------