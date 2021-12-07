import os


class CodecConverter:
    @staticmethod
    def conversor_tool():
        # menu to show the options 
        menu = input("Choose 1 option\n 1. VP8: \n 2. VP9: \n 3. h265: \n 4. AV1: \n")

        if menu == "1":
            # convert from .mp4 to .vp8
            terminal_command2 = "ffmpeg -i vid2.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8.webm"
            os.system(terminal_command2)

        elif menu == "2":
            # convert from .mp4 to .vp9
            terminal_command = "ffmpeg -i vid2.mp4 -c:v libvpx-vp9 -b:v 2M -pass 1 -an -f null /dev/null && \
                                ffmpeg -i vid2.mp4 -c:v libvpx-vp9 -b:v 2M -pass 2 -c:a libopus vp9.webm"
            os.system(terminal_command)

        elif menu == "3":
            # convert from .mp4 to .h265
            terminal_command = "ffmpeg -i vid2.mp4 -c:v libx265 -vtag hvc1 h265.mp4"
            os.system(terminal_command)

        elif menu == "4":
            # convert from .mp4 to .av1
            terminal_command = "ffmpeg -i vid2.mp4 -c:v libaom-av1 -crf 30 -b:v 0 av1.mkv"
            os.system(terminal_command)


if __name__ == '__main__':
    print("holi")