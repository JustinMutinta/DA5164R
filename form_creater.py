import PyPDF2
from datetime import datetime, date

# reader = PyPDF2.PdfReader("template/DA5164_R.pdf")
# fields = reader.get_form_text_fields()
# print(fields)

class Form_creator:

    def __init__(self, name, task_number):
        self.name = name
        self.task_number = task_number


    def pdf_creator(self):
        now = datetime.now()
        dateTime_string = now.strftime("%m-%d-%Y_%H-%M-%S")
        # current_time = now.time()
        # date_string = now.date()

        reader = PyPDF2.PdfReader("template/DA5164_R.pdf")
        writer = PyPDF2.PdfWriter()

        page = reader.pages[0]
        writer.add_page(page)

        try:
            pdf_output = f"outputs\Soldier-One_{dateTime_string}_DA5164_R.pdf"
            with open(pdf_output, "wb") as output_stream:
                writer.write(output_stream)
        except Exception as e:
            print(e)