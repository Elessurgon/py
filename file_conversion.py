import pandas as pd
from pyxlsb import open_workbook as open_xlsb
import os

def make_xlsb_to_csv(file):
	df = []
	with open_xlsb(file) as wb:
	    with wb.get_sheet(1) as sheet:
	        for row in sheet.rows():
	        	df.append([item.v for item in row])
	            
	print(df[0])
	print()
	df = pd.DataFrame(df[1:], columns=df[0])
	df.to_csv(r"C:\Users\Russel\Desktop\IPL DATASET\csv"+"\\"+os.path.basename(os.path.splitext(file)[0])+".csv")
	
def make_xlsx_to_csv(file):
	df = pd.read_excel(file)
	df.to_csv(r"C:\Users\Russel\Desktop\IPL DATASET\csv"+"\\"+os.path.basename(os.path.splitext(file)[0])+".csv")

def make_xls_to_csv(file):
	df = pd.read_excel(file)
	df.to_csv(r"C:\Users\Russel\Desktop\IPL DATASET\csv"+"\\"+os.path.basename(os.path.splitext(file)[0])+".csv")

if __name__ == "__main__":

	direct = r"C:\Users\Russel\Desktop\IPL DATASET"
	for file in os.listdir(direct):
		if file.endswith(".xls"):
			make_xls_to_csv(direct+ "\\" +file)
		elif file.endswith(".xlsx"):
			make_xlsx_to_csv(direct+ "\\"+ file)
		elif file.endswith(".xlsb"):
			make_xlsb_to_csv(direct+ "\\"+ file)
		else:
			print("not this")
	print("Done")

