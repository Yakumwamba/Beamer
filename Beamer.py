#!/usr/bin/env python3

import argparse

def print_ascii_art():
    # ASCII art generator logic goes here
    # For simplicity, we will just print the text
    print(r"""                                                                                                                     
      
           J8OOOYGGbOOkGJ' .m&OOOOOOOOOOU7     tAOO&AO&w.   i&OOAYo. /6AOO&h` 78OOOOOOOOOO8p   F&OOOOOOAOkbh!.          
           TObbkTvv[ZbbYb\ .pkbbY#[11111s=    vZYbbnXYbk1   ikbbbYOCl4ObbbkS` oObbYp[11111})   2kbbkJ>>!bbbkO>          
           #AYYYYbbkkYYb7. .6kYYYYYYYYYOI    =4kbkJ`[kYYb%  ikYYYGkkYkYGYYkg` oAYYYYYYYYYO#    5kYYkXSqVYYYY6;          
           J8A&$yssIGU&&&] .m&&882zjjjjji-  -5AkO8GXP$8A&E= i&A&8ty&Ab]58&Ud` 7UA&UhzjjjjL*'   F8&88GqY@888f`           
           fBBWMA44EDMNW8r .VBBWM@&&AAAO82 .u$&$@E4ggEKBKKm_vHDWM!.)v" SNWMZ` uWBWMD&&&AAA&P_  SBBW0C <OMNWHj-          
           1SghVd4ddhqyt"   LgghVddVVhhhhz =355mz`    !hq6mi/mShdx     jdVdw. IgghVdddVhhhh3`  jSghd!  \mVhhVr                                                                                                     
                      """)

def main():
    print_ascii_art()
    parser = argparse.ArgumentParser(description='Beamer CLI Program')
    parser.add_argument('username', type=str, help='Username for  Roblox')
    parser.add_argument('-b', '--banner', action='store_true', help='Print a banner with ASCII graphics')
    args = parser.parse_args()

    if args.banner:
        print_ascii_art("Beamer with a torch")

    print(f"Username: {args.username}")

if __name__ == '__main__':
    main()
