import os


class ChooseIp:
    @staticmethod
    def stream_live_v2():
        # giving the option to insert your own id
        IP = str(input("Introduce the IP where you want to stream the video: "))
        terminal_command = "ffmpeg -re -i bbb.mp4 -an -c:v copy -f mpegts udp://"
        term_command = ":2222?pkt_size=1316"
        def_term_cmd = terminal_command + IP + term_command

        print(def_term_cmd)
        os.system(def_term_cmd)

