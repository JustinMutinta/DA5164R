import PyPDF2
from datetime import datetime, date
from mos_15F_task_list import mos_15F
from mos_15N_task_list import mos_15N


class Form_creator:
    def __init__(self, rank, last_name, first_name, mos, task_number):
        self.rank = rank
        self.last_name = last_name
        self.first_name = first_name
        self.mos = mos
        self.task_number = task_number

    def find_task(self):
        if self.mos == "15F":
            for task in mos_15F:
                if self.task_number in task:
                    return task
                    break
                else:
                    pass
        else:
            for task in mos_15N:
                if self.task_number in task:
                    return task
                    break
                else:
                    pass

    def task_items_to_be_printed(self, current_task):
        counter = 65
        task_items = self.find_task()
        task_to_be_printed = self.find_task()
        soldier_info = f"{self.rank} {self.last_name}, {self.first_name}"
        output_text = {}
        output_text.update({'TASKNUM[0]': self.task_number, 'TASKTITLE[0]': task_to_be_printed[1], 'SOLDIER[0]': soldier_info,})

        while counter < 79:
            task_counter = 2
            for task in current_task:
            # for task in task_items[2:]:
                new_title = f"TITLE_{chr(counter)}[0]"
                output_text[new_title] = task
                task_counter += 1
                counter += 1

        return output_text


    def pdf_creator(self):
        now = datetime.now()
        dateTime_string = now.strftime("%m-%d-%Y_%H-%M-%S")

        reader = PyPDF2.PdfReader("template/DA5164_R.pdf")
        writer = PyPDF2.PdfWriter()

        page = reader.pages[0]
        writer.add_page(page)

        master_task_list = self.find_task()
        master_task_list_length = len(master_task_list)

        while master_task_list_length > 0:
            counter = 0
            mini_list = []
            while(counter < 15):
                for task in master_task_list:
                    mini_list.append(task)
                    counter += 1
                    master_task_list_length -= 1
            writer.update_page_form_field_values(writer.pages[0], self.task_items_to_be_printed(mini_list))

            try:
                pdf_output = f"outputs\{self.rank}_{self.last_name}_{self.first_name}_{self.task_number}_{dateTime_string}_PAGE_{counter}_DA5164_R.pdf"
                with open(pdf_output, "wb") as output_stream:
                    writer.write(output_stream)
            except Exception as e:
                print(e)