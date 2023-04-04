from Data_storage import QuessionAnswer


class Quiz_bl(object):

    def __init__(self, User_ID,):
        self.user_id = User_ID

        self.Obj1 = QuessionAnswer(User_ID)

    def InsertMaks(self, GivenAnswer, Paper_Id):
        correct_ = 0
        incorrect_ = 0
        for i, item in enumerate(self.ViewCorrectAnswer(Paper_Id)):
            print(item)
            print(GivenAnswer)
            if item[8] == GivenAnswer[i]:
                correct_ += 1
            else:
                incorrect_ += 1

        print(correct_)
        print(incorrect_)

        return self.Obj1.InsertMaks(correct_, incorrect_, Paper_Id)

    def ViewQuiz(self, Paper_Id):
        return self.Obj1.quiz(Paper_Id)
    
    def ViewStudentsMarks(self,Paper_Id):
        print('in side BL :',self.user_id)
        return self.Obj1.ViewStudentsMarks(self.user_id,Paper_Id)
    
    def ViewCorrectAnswer(self,Paper_Id):
        return self.Obj1.ViewCorrectAnswer(Paper_Id)

    def ActivePaper(self):
        return self.Obj1.ActivePaper()

    def IsComplted(self, Paper_Id):
        return self.Obj1.IsComplted(Paper_Id)
