import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.basketball-reference.com/leagues/NBA_2026_advanced.html"
table = pd.read_html(url)
#Selects table with all the data we want
players = table[0]

players = players[players["Rk"]!= "Rk"]

all_stars = ["Scottie Barnes","Devin Booker","Cade Cunningham", "Jalen Duren","Anthony Edwards", "Chet Holmgren","Jalen Johnson","Tyrese Maxey","Jaylen Brown","Jalen Brunson","Kevin Durant","De'Aaron Fox","Brandon Ingram", "Lebron James","Kawhi Leonard", "Donovan Mitchell","Stephen Curry","Deni Avdija","Luka Dončić", "Shai Gilgeous-Alexander","Nikola Jokić", "Jamal Murray","Norman Powell","Alperen Sengun","Pascsal Siakam","Karl-Anthony Towns","Victor Wembanyama","Giannis Antetokounmpo"]
    
#Filters Dataframe to just players that are currently all stars this season.
all_star_players = players[players["Player"].isin(all_stars)]

all_star_players["PER"] = pd.to_numeric(all_star_players["PER"], errors="coerce")

plt.figure(figsize=(12,6))
plt.bar(all_star_players["Player"], all_star_players["PER"], color = "skyblue")
plt.xticks(rotation=45, ha="right")
plt.ylabel("PER")
plt.title("2025-2026 NBA All-Stars - PER Comparison")
plt.tight_layout()
plt.savefig("all_stars_per.png")
