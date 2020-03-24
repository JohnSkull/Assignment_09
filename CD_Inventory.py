#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: 
# Johnh, 2020-Mar-19, Copied Starter Files into local folder
# Johnh, 2020-Mar-19, Extended functionality to add tracks
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

def main():
	lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
	lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
	IO.ScreenIO.print_menu()
	strChoice = IO.ScreenIO.menu_choice()
	while strChoice != 'x':
		if strChoice == 'l':
			load(lstFileNames,lstOfCDObjects)
		elif strChoice == 'a':
			addCD(lstFileNames,lstOfCDObjects)
		elif strChoice == 'd':
			IO.ScreenIO.show_inventory(lstOfCDObjects)
		elif strChoice == 'c':
			if len(lstOfCDObjects) > 0:
				chooseAlbum(lstFileNames,lstOfCDObjects)
			else:
				print("No CDS available")
		elif strChoice == 's':
			save(lstFileNames,lstOfCDObjects)
		else:
			print('General Error')
		IO.ScreenIO.print_menu()
		strChoice = IO.ScreenIO.menu_choice()
			
def load(lstFileNames,lstOfCDObjects):
	print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
	strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
	if strYesNo.lower() == 'yes':
		print('reloading...')
		lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
		IO.ScreenIO.show_inventory(lstOfCDObjects)
	else:
		input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
		IO.ScreenIO.show_inventory(lstOfCDObjects)

def addCD(lstFileNames,lstOfCDObjects):
	tplCdInfo = IO.ScreenIO.get_CD_info()
	cd_id, cd_title, cd_artists = tplCdInfo
	while not cd_id.isdigit():
		print("Error! Invalid CD ID, its not numeric")
		return 
	PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
	IO.ScreenIO.show_inventory(lstOfCDObjects)


#he wants to save the album info
def chooseAlbum(lstFileNames,lstOfCDObjects):
	IO.ScreenIO.show_inventory(lstOfCDObjects)
	cd_idx = input('Select the CD / Album index: ')
	
	try:
		cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
	except Exception as e:
		return
		
	while True:
		IO.ScreenIO.print_CD_menu()
		strChoice = IO.ScreenIO.menu_CD_choice()
		if strChoice == 'x':
			break
		if strChoice == 'a':    #modify track
			tplTrkInfo = IO.ScreenIO.get_track_info()
			trkID, trkTitle, trkLength = tplTrkInfo
			if trkID.isdigit() and 0 <= int(trkID) - 1:
				PC.DataProcessor.add_track(tplTrkInfo, cd)
			else:
				print("Invalid track ID")
		elif strChoice == 'd':
			try:
				cd.get_tracks()	
				IO.ScreenIO.show_tracks(cd)
			except Exception as e:
				print(e)
		elif strChoice == 'r':
			try:
				cd.get_tracks()
				IO.ScreenIO.show_tracks(cd)
				trk_idx = int(input('Select the Track index: '))
				cd.rmv_track(trk_idx)
			except Exception as e:
				print(e)
		else:
			print('General Error')

def save(lstFileNames,lstOfCDObjects):
	IO.ScreenIO.show_inventory(lstOfCDObjects)
	strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
	if strYesNo == 'y':
		IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
	else:
		input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
	
	
main()