from converter import CodecConverter
from comparison import CompareAndExport
from stream import Stream
from stream_choosing_ip import ChooseIp


if __name__ == '__main__':
    menu = input("Choose what do you want to do.\n1. Conversor\n2. Compare \
                 \n3. Stream live w/ out choosing IP\n4. Stream live choosing IP  ")

    if menu == "1":
        cc = CodecConverter
        cc.conversor_tool()
    elif menu == "2":
        c1 = CompareAndExport
        c1.compare()
    elif menu == "3":
        ss = Stream
        ss.stream_live()
    elif menu == "4":
        s1 = ChooseIp
        s1.stream_live_v2()
    else:
        print("That was never an option. ")





