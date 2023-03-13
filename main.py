from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input('Please provide the amount owed: '))
period = input('Please provide the period of the bill: ')

bill = Bill(amount, period)

number_of_flatmates = int(input('How many flatmates are there? '))
flatmates = []
for i in range(number_of_flatmates):
    name = input('Please provide the name of flatmate #{}. '.format(i+1))
    days = int(input('Please provide the number of days that {} spent in the flat: '.format(name)))
    flatmates.append(Flatmate(name, days))

pdf_report = PdfReport(bill.period + ' Bill.pdf')
pdf_report.generate(flatmates, bill)
