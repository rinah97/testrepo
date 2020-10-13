from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "news"
ws1.append(["제목", "링크", "신문사"])

wb.save(filename='news.xlsx')