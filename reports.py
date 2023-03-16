import os
import webbrowser
from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Creates a pdf file that contains data about
    the flatmates such as their names, their due amount,
    and the pay period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image('files/house.png', w=30, h=30)

        # Insert title block
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')

        # Insert period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=14)

        # Insert cells for flatmates
        for flatmate in flatmates:
            pdf.cell(w=100, h=25, txt=flatmate.name, border=0)
            pdf.cell(w=150, h=25, txt='$' + str(flatmate.pays(bill, flatmates)), border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open('file://' + os.path.realpath(self.filename))


class FileSharer:

    def __init__(self, filepath, api_key='AChEE64IsSzyilTObRDRUz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url