import random
from datetime import datetime, timedelta

# Function creates fake logs
def make_logs():

    # File where logs will be saved
    file = open("runs/app.log", "w")

    start_time = datetime.now()

    # Loop through 120 minutes
    for i in range(120):

        time = start_time + timedelta(minutes=i)

        errors = random.randint(0,2)
        timeouts = random.randint(0,1)
        info = random.randint(5,10)

        # Create an incident between minute 50 and 70
        if i > 50 and i < 70:
            errors = errors + random.randint(8,12)
            timeouts = timeouts + random.randint(3,5)

        # Error logs
        for j in range(errors):
            file.write(str(time) + " ERROR\n")

        # Timeout logs
        for j in range(timeouts):
            file.write(str(time) + " WARNING timeout\n")

        # Normal logs
        for j in range(info):
            file.write(str(time) + " INFO system operating normally\n")

    file.close()

    print("logs created")

# Function is run
make_logs()