import schedule
import time
from volume_analyze.Standard_deviation_and_Z_score.stream_analize import main

def job():
    print("I'm working...")
    print(main())


schedule.every().minutes.at(":00").do(job)



while True:
    schedule.run_pending()
    time.sleep(1)