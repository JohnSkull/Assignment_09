#------------------------------------------#
# Title: Test Harness
# Desc: A Module to test the Modules
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks


import DataClasses as DC
import ProcessingClasses as PC
import IOClasses as IO

lstOfCDObjects = []
file_name = ['TestCD.txt', 'TestTrack.txt']

print('\n\nTesting Track class')
print(DC.Track.__doc__)
trk1 = DC.Track(1, 'test.track1', '01:59')
trk2 = DC.Track(2, 'test.track2', '02:59')
print(trk1)
print('record for file:', trk1.get_record())

print('\n\nTesting CD class')
print(DC.CD.__doc__)
cd1 = DC.CD(1, 'test_title', 'cd_artist')
print(cd1)
print('record for file:', cd1.get_record())
print('adding tracks...')
cd1.add_track(trk1)
cd1.add_track(trk2)
print('get tracks:\n', cd1.get_tracks())
print('get long record:\n', cd1.get_long_record())
print('removing track 2...')
cd1.rmv_track(2)
print('get long record:\n', cd1.get_long_record())
lstOfCDObjects.append(cd1)

print('\n\nTesting of class FileIO')
IO.FileIO.save_inventory(file_name, lstOfCDObjects)
print(IO.FileIO.load_inventory(file_name))

print('\n\nTesting ScreenIO class')
print('Main menu:')
IO.ScreenIO.print_menu()
print('selection in menu: {}'.format(IO.ScreenIO.menu_choice()))
print('Inventory:')
IO.ScreenIO.show_inventory(lstOfCDObjects)
cd2 = DC.CD(2, 'test_title_2', 'cd_artist_2')
lstOfCDObjects.append(cd2)
print('Inventory:')
for item in lstOfCDObjects:
    print(item)
cd_idx = 1
cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
print('\nSub Menu')
IO.ScreenIO.print_CD_menu()
print('selection in sub menu: {}'.format(IO.ScreenIO.menu_CD_choice()))
print('Tracks:')
IO.ScreenIO.show_tracks(cd)

print('\n\nTesting Processing Classes')
PC.DataProcessor.add_CD((3, 'Foreigner', 'Foreigner'), lstOfCDObjects)
print('Inventory:')
for item in lstOfCDObjects:
    print(item)


