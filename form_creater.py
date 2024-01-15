import PyPDF2
from datetime import datetime, date

# reader = PyPDF2.PdfReader("template/DA5164_R.pdf")
# fields = reader.get_form_text_fields()
# print(fields)

class Form_creator:

    def __init__(self, rank, last_name, first_name, task_number):
        self.rank = rank
        self.last_name = last_name
        self.first_name = first_name
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
        soldier_info = f"{self.rank} {self.last_name} {self.first_name}"

        writer.update_page_form_field_values(
            writer.pages[0], {
                'TASKNUM[0]': self.task_number,
                'SOLDIER[0]': soldier_info
            }
        )

        try:
            pdf_output = f"outputs\{self.rank}_{self.last_name}_{self.first_name}_{self.task_number}_{dateTime_string}_DA5164_R.pdf"
            with open(pdf_output, "wb") as output_stream:
                writer.write(output_stream)
        except Exception as e:
            print(e)