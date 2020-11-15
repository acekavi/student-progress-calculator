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


def progress_check(credits):
    if credits[0] == 120:
        return "Progress"

    elif credits[0] == 100 and (credits[1] or credits[2]) == 20:
        return "Progress (module trailer)"

    elif credits[2] >= 80:
        return "Excluded"

    else:
        return "Do not progress – module retriever"


def student_progress_cal():
    while True:
        credits_list = []
        for i in ["pass", "defer", "fail"]:
            x = CharInput(f"Please enter your credits at {i}", (0, 20, 40, 60, 80, 100, 120)).int_input()
            credits_list.append(x)

        if sum(credits_list) == 120:
            return progress_check(credits_list)

        else:
            print("Total incorrect")


class Histograms:
    def __init__(self,hist_list):
        self.hist_list = hist_list

    def horizontal_histogram(self):
        no_of_progress = self.hist_list.count('progress')
        no_of_progress_mt = self.hist_list.count('progress (module trailer)')
        no_of_not_progress = self.hist_list.count('do not progress – module retriever')
        no_of_excluded = self.hist_list.count('excluded')
        print(f"""----------------------------------------------------------------
Progress    {no_of_progress}    : {no_of_progress * "*"}
Trailing    {no_of_progress_mt}    : {no_of_progress_mt * "*"}
Retriever   {no_of_not_progress}    : {no_of_not_progress * "*"}
Excluded    {no_of_excluded}    : {no_of_excluded * "*"}

{len(self.hist_list)} outcomes in total.
----------------------------------------------------------------""")


    def vertical_histogram(self):
        histogram_dict = {
            "Progress" : self.hist_list.count('progress'),
            "Trailing" : self.hist_list.count('progress (module trailer)'),
            "Retriever" : self.hist_list.count('do not progress – module retriever'),
            "Excluded" : self.hist_list.count('excluded')
        } # Progress status and its count in a dictionary

        # Printing the header of the histogram by iterating the keys of dictionary
        print("\n----------------------------------------------------------------")
        for key in histogram_dict:
            print(key,end="\t")
        print()

        # Printing the stars
        for i in range(1, max(histogram_dict.values()) + 1): # Finding the max value in the dictionary for rows
            for progress_value in histogram_dict.keys(): # A loop iterating keys
                if histogram_dict[progress_value] >= i: # If the value of the key is equal or greater than the current -
                    print('\t*\t\t', end=' ')           # -iteration of the main loop, printing a star
                else:
                    print('\t \t\t', end=' ')
            print()



class ForStaff:

    def manual():
        histogram_list = [] # Progress status in a list
        while True:
            histogram_list.append(student_progress_cal().lower()) # Run student progress function and get values for the histogram list
            print("\nWould you like to enter another set of data?")
            choice = CharInput("Enter 'y' for yes or 'q' to quit and view results", ("y", "q")).str_input()
            if choice == "y":
                print()
                continue

            else:
                Histograms(histogram_list).vertical_histogram()
                Histograms(histogram_list).horizontal_histogram()


    def automatic():
        filename = "dataset.txt"
        try:
            lines = [] # Context line by line in a list
            with open(filename) as file: # Reading the file
                for line in file:
                    line = line.strip()  # Striping the file line by line
                    lines.append(line)  # storing line by line in a list

    # Printing file name and its context
            print(f"\nFile name = {filename}")
            for line in lines:
                print(line)
    # ----------------------------------

            histogram_list = [] # Same histogram list as the manual 1. Progress status in a list
            for line in lines: # Accessing line by line in the lins[] array
                elem = line.split() # Spliting sentences into words

                int_indexes = [2, 5, 8] # Indexes of numbers in the dataset after spliting

                int_strings_with_comma = [elem[i] for i in int_indexes] # Selecting the elements with only numbers

                int_strings = [s.replace(',', '') for s in int_strings_with_comma] # Removing the commas(,) at the end of numbers if any

                int_list = [int(i) for i in int_strings] # Converting the number strings to Integers

                histogram_list.append(progress_check(int_list).lower()) # Checking progresses and adding them to histogram list

            Histograms(histogram_list).vertical_histogram()
            Histograms(histogram_list).horizontal_histogram()

        except FileNotFoundError:
            print(f"{filename} could not be found!")