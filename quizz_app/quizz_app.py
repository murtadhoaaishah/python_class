import random
import time
import PyPDF2


class QuizApp:
    def __init__(self):
        self.score = 0
        self.questions = []
        self.start_time = 0
        self.end_time = 0



    def load_questions_from_pdf(self, file_path):
        """
        load questions from pdf given the file path 
        """

        with open(file_path, "rb")
            reader = pyPDF2.pdfReader   (file_path)
            text = ""
            for page_number in range(len(reader.pages)):
                text += reader.pages[page_number].extract_text()
                page = reader.getpage(page_number)
                lines = text.split('\n')
                print(text)

            # for line in lines:


    #text
quiz = QuizApp()
text = quiz.load_questions_from_pdf('./Python-Interview-Questions.pdf')