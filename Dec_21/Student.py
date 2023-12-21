class Student:
    def __init__(self):
        self.num:         int            = ""
        self.name:        str            = ""
        self.total_score: int            = 0
        self.__scores:    dict[str, int] = {}

    def init_data(self, n: int):
        """
        Generates stub data for this student

        @param n: Seed used for randomization
        """
        from main import SUBJECTS
        import random
        import string

        random.seed(n) # Temporarily define a seed

        self.num  = n
        self.name = ''.join(random.choices(string.ascii_letters, k=6))

        for subject in SUBJECTS:
            self.update_score(subject, random.randint(40, 100))    

        random.seed() # Revert to default seed after method to ensure code outside this method still behaves normally
        pass

    def get_score(self, subject: str):
        """
        Gets the score of a subject

        Parameters:
        subject: The subject to query
        """
        if not subject in self.__scores:
            return 0
        
        return self.__scores[subject]

    def update_score(self, subject: str, value: int):
        """
        Updates a subject with a new value

        Parameters:
        subject: The subject to update
        value:   The new score for this subject 
        """
        added_value = 0
        if subject in self.__scores:
            added_value -= self.__scores[subject]

        self.__scores[subject] = value
        self.total_score += added_value

    def print_stats(self):
        """
        Displays a student's statistics
        """
        # We print "||" at the start to compensate for the "||" at the end
        print(f"|| ID: {self.num:>4} || Name: {self.name:<7}", end="-" * 8)
        for subject, score in self.__scores.items():
            print(f" {subject}: {score:>6} ||", end="")
        print()
