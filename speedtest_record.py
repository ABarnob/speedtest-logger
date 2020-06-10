from datetime import datetime
import time
import speedtest


class SpeedtestRecord:
    def __init__(self, servers=[], threads=None, interval=30):
        '''
        Constructs all the necessary attributes for the SpeedtestRecord object.

        Parameters
        ----------
            servers : list, optional
                server id's
            threads : int, optional
                number of operation threads
            interval : int, optional
                program interval in minutes
        '''

        self.servers = servers
        self.threads = threads
        self.interval = interval

    def get_speed(self):
        '''
        Tests the current internet speed
        Returns
        -------
        Object
        '''
        try:
            # The speedtest
            s = speedtest.Speedtest()
            s.get_servers(self.servers)
            s.get_best_server()
            s.download(threads=self.threads)
            s.upload(threads=self.threads)
        except:
            s = False

        return s

    def write_to_file(self, file_name, content):
        '''
        Writes the file in the disk
        '''
        with open(file_name, 'a') as f:
            f.write(content)

    def speed_in_megabits(self, speed_in_bits):
        '''
        Converts speed from bits per second to Megabits per second
        Returns
        -------
        float
        '''
        return round(speed_in_bits / 10**6, 2)

    def main(self):
        while True:
            speed = self.get_speed()

            # Get current date and time
            now = datetime.now()
            current_time = now.strftime('%I:%M %p')

            # Set output file name as today's date (dd-mm-YYYY.txt)
            file_name = f'{now.strftime("%d-%m-%Y")}.txt'

            if speed:
                result_dict = speed.results.dict()
                download_speed = self.speed_in_megabits(
                    result_dict['download'])
                upload_speed = self.speed_in_megabits(
                    result_dict['upload'])

                # optput format
                output = (
                    f'[{current_time}]\n'
                    f'Download: {download_speed} Mbps\n'
                    f'Upload: {upload_speed} Mbps\n'
                    f'--------------------------------------\n'
                )
            else:
                # optput format
                output = (
                    f'[{current_time}]\n'
                    f'Something went wrong!\n'
                    f'--------------------------------------\n'
                )

            self.write_to_file(file_name, output)

            # Interval
            time.sleep(self.interval * 60)


if __name__ == '__main__':
    speedtest_record = SpeedtestRecord()
    speedtest_record.main()
