import datetime
import logging
import sys
import time
import requests as requests


def main():
    # Logging and shit
    stream_handler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s.%(msecs)03d][%(levelname).1s][%(module)-15s:%(lineno)-3s] %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S',
                        handlers=[stream_handler])

    # EDIT START DATE HERE
    start_date = datetime.date(2022, 11, 3)  # YYYY MM DD
    # EDIT END DATE HERE
    end_date = datetime.date(2022, 12, 2)  # YYYY MM DD
    # BE CAREFUL TO NOT INCLUDE ALREADY APPROVED DAYS AS IT WILL OVERWRITE THEM!

    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        logging.info('Update for day ' + start_date.strftime("%Y-%m-%d"))
        date = start_date
        start_date += delta
        if date.weekday() < 5:  # THIS AVOIDS FILLING SATURDAYS AND SUNDAYS
            date_timestamp = int(time.mktime(date.timetuple()))
            # SET TIMESTAMP OF THE START OF THE FIRST INTERVAL (added in seconds)
            morning_start = date_timestamp + 60 * (10 * 60)
            # SET TIMESTAMP OF THE END OF THE FIRST INTERVAL (added in seconds)
            morning_end = date_timestamp + 60 * (14 * 60)
            # SET TIMESTAMP OF THE START OF THE SECOND INTERVAL (added in seconds)
            afternoon_start = date_timestamp + 60 * (15 * 60)
            # SET TIMESTAMP OF THE END OF THE SECOND INTERVAL (added in seconds)
            afternoon_end = date_timestamp + 60 * (19 * 60)

            # FOR HALF HOURS YOU WOULD DO (for e.g. 10:30 in the morning):
            # morning_start = date_timestamp + 60 * (10*60 + 30)

            logging.info('Sending request to Holded.')
            payload = {
                "day": date_timestamp,
                "trackerList[0][start]": morning_start,
                "trackerList[0][end]": morning_end,
                "trackerList[1][start]": afternoon_start,  # YOU CAN DELETE THIS SECOND INTERVAL
                "trackerList[1][end]": afternoon_end,  # IF YOU DON'T DO SPLIT SHIFT
                # YOU COULD ADD AS MANY INTERVALS AS YOU WANT, BUT YOU HAVE TO LIKEWISE SET THEIR TIMESTAMPS
                "timezone": "Europe / Madrid",
                "location[accuracy]": 683.2039592110011,
                "location[latitude]": 41.4089216,
                "location[longitude]": 2.1331968,
            }

            headers = {

                'authority': 'app.holded.com',
                'path': '/teamzone/trackers/updateday',
                'scheme': 'https',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'es-ES,es;q=0.9,ca;q=0.8,en;q=0.7',
                'content-length': "360",
                'origin': 'https://app.holded.com',
                'referer': 'https://app.holded.com/employees/timetracking',

                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Windows",
                'sec-fetch-dest': 'empty',
                # HERE IS WHERE YOU PASTE YOUR COOKIE, BE CAREFUL TO NOT BREAK THE STRING
                'cookie': '',
                'sec-fetch-mode': 'cors'
            }

            request = requests.Request('POST', 'https://app.holded.com/teamzone/trackers/updateday',
                                       headers=headers, data=payload)
            prepared = request.prepare()
            logging.info('POST URL {0}'.format(prepared.url))
            logging.info('BODY {0}'.format(prepared.body))
            logging.info('HEADERS {0}'.format(prepared.headers))
            sess = requests.Session()
            post = sess.send(prepared)


if __name__ == '__main__':
    main()