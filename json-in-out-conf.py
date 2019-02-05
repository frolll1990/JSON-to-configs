import json, time


file = open('686_Symblos.json', 'rb')
csv_file = open('config.csv', 'a')
ini_file = open('uber_feed_mt5.ini', 'a')
parsed_json = json.loads(file.read())

symbol_count = parsed_json["Server"][0]["ConfigSymbols"]

print("Number of symbols is:\n", len(symbol_count))

time.sleep(3)

what = int(input('''
What Do You Want? 
1.\tSwapChanger Config
2.\tUberFeed Config
:'''))

if what == 1:
    for a in range(0, len(symbol_count)):
        symbol_name = parsed_json["Server"][0]["ConfigSymbols"][a]["Symbol"]
        print(symbol_name)
        stroka = str('demo\demoforex;' + str(symbol_name) + ';0.' + str(a + 1) + ';-0.' + str(a + 1) + '\n')
        print(stroka)
        csv_file.write(stroka)
    csv_file.close()

else:
    for a in range(0, len(symbol_count)):
        symbol_name = parsed_json["Server"][0]["ConfigSymbols"][a]["Symbol"]
        print(symbol_name)
        stroka = str(str(symbol_name) + '=range:0.001,interval:300,mode:sd' + '\n')
        print(stroka)
        ini_file.write(stroka)
    ini_file.close()


file.close()
