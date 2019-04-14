import pandas as pd 
import numpy as np
import os

sheets = []

def make_pandas(file):
	sheet_name = pd.read_csv(file)
	return sheet_name

def make_list_of_sheets():
	direct = r"C:\Users\Russel\Desktop\IPL DATASET\csv"
	for i,file in enumerate(os.listdir(direct)):
			if file.endswith(".csv"):
				sheets.append(make_pandas(direct+"\\"+file))

def Run_avg_columns_top_players():
	batsman_sheet = []
	for sheet in sheets:
		#print(sheet[0:2])
		try:
			sheet["Run Avg"] = sheet["Runs"]/sheet["Matches Played"]
			#print("done")
		except KeyError:
			try:
				#print("KeyError 1")
				sheet["Run Avg"] = sheet["Run"]/sheet["Matches Played"]
			except KeyError:
				try:
					#print("KeyError 2")
					sheet["Run Avg"] = sheet["Run"]/sheet["Matches Played "]
				except KeyError:
					#print("KeyError 3")
					sheet["Run Avg"] = sheet["Runs"]/sheet["Matches Played "]


	for sheet in sheets:
		new_sheet = sheet.sort_values(by=["Run Avg"], ascending=False)[0:2]
		batsman_sheet.append(new_sheet)		

	make_lots_of_files(batsman_sheet,r"C:\Users\Russel\Desktop\IPL DATASET\csv\batsmen","batsmen")	

def best_bowler():
	best_bowler_sheet = []
	for sheet in sheets:
		try:
			sheet["bowled/eco"] = sheet['Balls Bowled'].astype(int)/sheet["Economy"].astype(float)
		except KeyError:
			try:
				sheet["bowled/eco"] = sheet['BallsBowled'].astype(int)/sheet["Economy"].astype(float)
			except ValueError:
				sheet["bowled/eco"] = None	
		except ValueError:
			sheet["bowled/eco"] = None

	for sheet in sheets:
		new_sheet = sheet.sort_values(by=["bowled/eco"], ascending=False)[0:1]
		best_bowler_sheet.append(new_sheet)

	make_lots_of_files(best_bowler_sheet,r"C:\Users\Russel\Desktop\IPL DATASET\csv\bowler","bowlers")


def best_all_rounder():
	all_round_sheet = []
	for sheet in sheets:
		try:
			sheet["all_round_variate"] = sheet['Run Avg']/sheet["bowled/eco"]	
		except ValueError:
			sheet["all_round_variate"] = None

	for sheet in sheets:
		new_sheet = sheet.sort_values(by=["all_round_variate"], ascending=False)[0:1]
		all_round_sheet.append(new_sheet)

	make_lots_of_files(all_round_sheet,r"C:\Users\Russel\Desktop\IPL DATASET\csv\rounder","rounders")	
	

def best_wicket_keeper():
	wicket_keeper_sheet = []
	for sheet in sheets:
		try:
			new_sheet = sheet.sort_values(by=["Ct_St"], ascending=False)[0:1]
		except KeyError:
			new_sheet = sheet.sort_values(by=["ct_st"], ascending=False)[0:1]
		wicket_keeper_sheet.append(new_sheet)
	
	make_lots_of_files(wicket_keeper_sheet,r"C:\Users\Russel\Desktop\IPL DATASET\csv\wicket","wickets")	
	

def put_pandas_in_csv(sheet,file,name):
	file = file + "\\" + name + ".csv"
	sheet.to_csv(file)

def make_lots_of_files(sheet_array,file,name):
	for i, sheet in enumerate(sheet_array):
		put_pandas_in_csv(sheet,file,name + str(i))

def make_best_team():
	#5 batsmen

	#2 all rounders

	#1 wicket keeper

	#3 bowlers




make_list_of_sheets()
Run_avg_columns_top_players()
best_bowler()
best_all_rounder()
best_wicket_keeper()
make_best_team()