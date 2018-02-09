from datetime import datetime, timedelta
from time import strftime

import data

secondWeekEnding = datetime.strptime(data.endDate, "%m/%d/%Y")
days1 = data.week1
days2 = data.week2

fields = [
	"First Week Ending", 
	"DateRow1", 
	"StartRow1", 
	"EndRow1", 
	"StartRow1_2", 
	"EndRow1_2", 
	"RegRow1", 
	"HolRow1", 
	"VacRow1", 
	"SckRow1", 
	"OTimeRow1", 
	"StrTimeRow1", 
	"OTimeRow1_2", 
	"DateRow2", 
	"StartRow2", 
	"EndRow2", 
	"StartRow2_2", 
	"EndRow2_2", 
	"RegRow2", 
	"HolRow2", 
	"VacRow2", 
	"SckRow2", 
	"OTimeRow2", 
	"StrTimeRow2", 
	"OTimeRow2_2", 
	"DateRow3", 
	"StartRow3", 
	"EndRow3", 
	"StartRow3_2", 
	"EndRow3_2", 
	"RegRow3", 
	"HolRow3", 
	"VacRow3", 
	"SckRow3", 
	"OTimeRow3", 
	"StrTimeRow3", 
	"OTimeRow3_2", 
	"DateRow4", 
	"StartRow4", 
	"EndRow4", 
	"StartRow4_2", 
	"EndRow4_2", 
	"RegRow4", 
	"HolRow4", 
	"VacRow4", 
	"SckRow4", 
	"OTimeRow4", 
	"StrTimeRow4", 
	"OTimeRow4_2", 
	"DateRow5", 
	"StartRow5", 
	"EndRow5", 
	"StartRow5_2", 
	"EndRow5_2", 
	"RegRow5", 
	"HolRow5", 
	"VacRow5", 
	"SckRow5", 
	"OTimeRow5", 
	"StrTimeRow5", 
	"OTimeRow5_2", 
	"DateRow6", 
	"StartRow6", 
	"EndRow6", 
	"StartRow6_2", 
	"EndRow6_2", 
	"RegRow6", 
	"HolRow6", 
	"VacRow6", 
	"SckRow6", 
	"OTimeRow6", 
	"StrTimeRow6", 
	"OTimeRow6_2", 
	"DateRow7", 
	"StartRow7", 
	"EndRow7", 
	"StartRow7_2", 
	"EndRow7_2", 
	"RegRow7", 
	"HolRow7", 
	"VacRow7", 
	"SckRow7", 
	"OTimeRow7", 
	"StrTimeRow7", 
	"OTimeRow7_2", 
	"RegWEEKLY TOTALS", 
	"HolWEEKLY TOTALS", 
	"VacWEEKLY TOTALS", 
	"SckWEEKLY TOTALS", 
	"OTimeWEEKLY TOTALS", 
	"StrTimeWEEKLY TOTALS", 
	"OTimeWEEKLY TOTALS_2", 
	
	
	"Second Week Ending", 
	"DateRow1_2", 
	"StartRow1_3", 
	"EndRow1_3", 
	"StartRow1_4", 
	"EndRow1_4", 
	"RegRow1_2", 
	"HolRow1_2", 
	"VacRow1_2", 
	"SckRow1_2", 
	"OTimeRow1_3", 
	"StrTimeRow1_2", 
	"OTimeRow1_4", 
	"DateRow2_2", 
	"StartRow2_3", 
	"EndRow2_3", 
	"StartRow2_4", 
	"EndRow2_4", 
	"RegRow2_2", 
	"HolRow2_2", 
	"VacRow2_2", 
	"SckRow2_2", 
	"OTimeRow2_3", 
	"StrTimeRow2_2", 
	"OTimeRow2_4", 
	"DateRow3_2", 
	"StartRow3_3", 
	"EndRow3_3", 
	"StartRow3_4", 
	"EndRow3_4", 
	"RegRow3_2", 
	"HolRow3_2", 
	"VacRow3_2", 
	"SckRow3_2", 
	"OTimeRow3_3", 
	"StrTimeRow3_2", 
	"OTimeRow3_4", 
	"DateRow4_2", 
	"StartRow4_3", 
	"EndRow4_3", 
	"StartRow4_4", 
	"EndRow4_4", 
	"RegRow4_2", 
	"HolRow4_2", 
	"VacRow4_2", 
	"SckRow4_2", 
	"OTimeRow4_3", 
	"StrTimeRow4_2", 
	"OTimeRow4_4", 
	"DateRow5_2", 
	"StartRow5_3", 
	"EndRow5_3", 
	"StartRow5_4", 
	"EndRow5_4", 
	"RegRow5_2", 
	"HolRow5_2", 
	"VacRow5_2", 
	"SckRow5_2", 
	"OTimeRow5_3", 
	"StrTimeRow5_2", 
	"OTimeRow5_4", 
	"DateRow6_2", 
	"StartRow6_3", 
	"EndRow6_3", 
	"StartRow6_4", 
	"EndRow6_4", 
	"RegRow6_2", 
	"HolRow6_2", 
	"VacRow6_2", 
	"SckRow6_2", 
	"OTimeRow6_3", 
	"StrTimeRow6_2", 
	"OTimeRow6_4", 
	"DateRow7_2", 
	"StartRow7_3", 
	"EndRow7_3", 
	"StartRow7_4", 
	"EndRow7_4", 
	"RegRow7_2", 
	"HolRow7_2", 
	"VacRow7_2", 
	"SckRow7_2", 
	"OTimeRow7_3", 
	"StrTimeRow7_2", 
	"OTimeRow7_4", 
	"RegWEEKLY TOTALS_2", 
	"HolWEEKLY TOTALS_2", 
	"VacWEEKLY TOTALS_2", 
	"SckWEEKLY TOTALS_2", 
	"OTimeWEEKLY TOTALS_3", 
	"StrTimeWEEKLY TOTALS_2", 
	"OTimeWEEKLY TOTALS_4", 
	"Full-Time", 
	"Part Time", 
	"Name", 
	"ID Number", 
	"Title", 
	"Supervisor",
]

import sys
sys.path.append("./fdfgen/")
from fdfgen import forge_fdf

fields = [
	('Name', data.name),
	('Part Time', True),
	('Supervisor', data.supervisor),
	('Title', data.title),
	('ID Number', data.emplid),
	('Second Week Ending', secondWeekEnding.strftime("%m/%d/%Y")),
	('First Week Ending', (secondWeekEnding - timedelta(days=7)).strftime("%m/%d/%Y"))
]

dowOffsetLUT = {
	'Sat': 6,
	'Sun': 5,
	'Mon': 4,
	'Tue': 3,
	'Wed': 2,
	'Thu': 1,
	'Fri': 0,
}

fieldIndex = 1
accumulatedTime = 0
for entry in days1:
	i = dowOffsetLUT[entry[0]]
	relevantDateStr = (secondWeekEnding - timedelta(days=i+7)).strftime("%m/%d/%Y")
	
	# Add Date
	fields.append(("DateRow" + str(fieldIndex), relevantDateStr))
	
	# First Time Block
	fields.append(('StartRow' + str(fieldIndex), entry[1]))
	fields.append(('EndRow' + str(fieldIndex), entry[2]))
	
	start = datetime.strptime(relevantDateStr + ' ' + entry[1], "%m/%d/%Y %I:%M %p")
	end = datetime.strptime(relevantDateStr + ' ' + entry[2], "%m/%d/%Y %I:%M %p")
	blockTime1 = end-start
	totalTime = blockTime1
	
	# Second Time Block
	if(len(entry) > 3):
		fields.append(('StartRow' + str(fieldIndex) + '_2', entry[3]))
		fields.append(('EndRow' + str(fieldIndex) + '_2', entry[4]))
	
		start = datetime.strptime(relevantDateStr + ' ' + entry[3], "%m/%d/%Y %I:%M %p")
		end = datetime.strptime(relevantDateStr + ' ' + entry[4], "%m/%d/%Y %I:%M %p")
		blockTime2 = end-start
		totalTime = totalTime + blockTime2
	
	# Total Time
	decimalTime = totalTime.seconds//3600 + ((totalTime.seconds//60)%60)/60.0
	accumulatedTime += decimalTime
	fields.append(("RegRow" + str(fieldIndex), decimalTime))
	fields.append(("StrTimeRow" + str(fieldIndex), decimalTime))
	
	fieldIndex += 1

# Weekly Totals
fields.append(("RegWEEKLY TOTALS", accumulatedTime))
fields.append(("StrTimeWEEKLY TOTALS", accumulatedTime))


fieldIndex = 1
accumulatedTime = 0
for entry in days2:
	i = dowOffsetLUT[entry[0]]
	relevantDateStr = (secondWeekEnding - timedelta(days=i)).strftime("%m/%d/%Y")
	
	# Add Date
	fields.append(("DateRow" + str(fieldIndex) + "_2", relevantDateStr))
	
	# First Time Block
	fields.append(('StartRow' + str(fieldIndex)+ '_3', entry[1]))
	fields.append(('EndRow' + str(fieldIndex) + '_3', entry[2]))
	
	start = datetime.strptime(relevantDateStr + ' ' + entry[1], "%m/%d/%Y %I:%M %p")
	end = datetime.strptime(relevantDateStr + ' ' + entry[2], "%m/%d/%Y %I:%M %p")
	blockTime1 = end-start
	totalTime = blockTime1
	
	# Second Time Block
	if(len(entry) > 3):
		fields.append(('StartRow' + str(fieldIndex) + '_4', entry[3]))
		fields.append(('EndRow' + str(fieldIndex) + '_4', entry[4]))
	
		start = datetime.strptime(relevantDateStr + ' ' + entry[3], "%m/%d/%Y %I:%M %p")
		end = datetime.strptime(relevantDateStr + ' ' + entry[4], "%m/%d/%Y %I:%M %p")
		blockTime2 = end-start
		totalTime = totalTime + blockTime2
	
	# Total Time
	decimalTime = totalTime.seconds//3600 + ((totalTime.seconds//60)%60)/60.0
	accumulatedTime += decimalTime
	fields.append(("RegRow" + str(fieldIndex) + "_2", decimalTime))
	fields.append(("StrTimeRow" + str(fieldIndex) + "_2", decimalTime))
	fieldIndex += 1

# Weekly Totals
fields.append(("RegWEEKLY TOTALS_2", accumulatedTime))
fields.append(("StrTimeWEEKLY TOTALS_2", accumulatedTime))





fdf = forge_fdf("",fields,[],[],[])

fdf_file = open("data.fdf","wb")

fdf_file.write(fdf)
fdf_file.close()
