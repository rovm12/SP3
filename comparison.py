import os


class CompareAndExport:
    @staticmethod
    def compare():
        mm = input("0. Type this one first to configure it.\
                   \n1. Export videos into h265 \
                   \n2. Export videos into vp9\nType your selection here: ")

        if mm == "0":
            # Merge two videos into one next to each pther. Save the output into merge.mp4
            terminal_command = "ffmpeg -i vp8.webm -i vp9.webm -filter_complex hstack merged.mp4"
            os.system(terminal_command)

        elif mm == "1":
            # convert the results from last step to .h265
            terminal_command2 = "ffmpeg -i merged.mp4 -c:v libx265 -vtag hvc1 merged_h265.mp4"
            os.system(terminal_command2)

        elif mm == "2":
            # convert the merged.mp4 file into codec vp9
            terminal_command2 = "ffmpeg -i merged.mp4 -c:v libvpx-vp9 -b:v 2M -pass 1 -an -f null /dev/null && \
                                    ffmpeg -i merged.mp4 -c:v libvpx-vp9 -b:v 2M -pass 2 -c:a libopus merged_vp9.webm"
            os.system(terminal_command2)

        else:
            print("That was not never an option. :) ")

        print("Done it! :)")