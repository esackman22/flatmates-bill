from fpdf import FPDF
import os
import webbrowser


class Bill:
    """
    Object that contains data about a bill, such as total amount owed
    and the pay period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays
    a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmates):
        weight = self.days_in_house / sum(flatmate.days_in_house for flatmate in flatmates)
        return round(weight * bill.amount, 2)


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


bill = Bill(120, 'April 2023')
john = Flatmate('John', 20)
mary = Flatmate('Mary', 25)

print("John pays: ", round(john.pays(bill, [john, mary]), 2))
print("Mary pays: ", round(mary.pays(bill, [john, mary]), 2))

pdf_report = PdfReport('Report1.pdf')
pdf_report.generate([john, mary], bill)
