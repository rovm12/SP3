import os

class Stream:
    @staticmethod
    def stream_live():
        # broadcasting lively to my IP that is 192.168.1.42 through the port 2222 with a packet size of 1316
        terminal_command = "ffmpeg -re -i bbb.mp4 -an -c:v copy -f mpegts udp://192.168.1.42:2222?pkt_size=1316"
        os.system(terminal_command)