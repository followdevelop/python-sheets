import gspread # pip install gspread

'''SETUP
- google developer console: https://console.developers.google.com
- new project -> activate drive and sheets api
- credentials -> service account -> name + role=editor
  ->create key and download json
- share client_email fom json in your sheets
'''

gc = gspread.service_account(filename='acces-key.json') # tu .json api google drive sheets
sh = gc.open_by_key("xxxxxxxxx") # or by sheet name: gc.open("TestList")
worksheet = sh.sheet1

res = worksheet.get_all_records()
# res = worksheet.get_all_values() 

# print(res)
print(len(res))