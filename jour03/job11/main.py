def time_text(temps):
    heures = temps // 60
    minutes = temps % 60
    print(f"{heures} heure(s) et {minutes} minute(s)")

time_text(60)
time_text(160)
time_text(3090)