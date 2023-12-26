import csv
import requests
import os

while True:
    name=input("what is the artist's name? ").title()
    results=requests.get("https://itunes.apple.com/search?entity=song&limit=3&term="+name)
    tracks=results.json()
    if len(tracks["results"])==0 :
        continue
    else:
        with open("songs.csv", "a", newline="") as file :
            if os.stat("songs.csv").st_size == 0 :
                writer=csv.writer(file)
                writer.writerow(["Artist", "1st", "2nd", "3rd"])
            else:
                writer=csv.DictWriter(file, fieldnames=(["Artist", "1st", "2nd", "3rd"]))
                forWrow=[name]
                for track in tracks["results"]:
                    forWrow.append(track["trackName"])
                writer.writerow({"Artist" : forWrow[0], "1st" : forWrow[1], "2nd" : forWrow[2], "3rd" : forWrow[3]})
        CorE="a"
        while CorE!="C" and CorE!="E" :
            CorE=input("if you want to continue press C and if you want to exit press E: ").upper()
            print("")
            if CorE!="C" and CorE!="E":
                print("Wrong input! try again.")
        if CorE == "E" :
            print("the list of the artist and their three most popular songs is saved in songs.csv. See you later!")
            break
    
    
    