from moviepy.video.io.VideoFileClip import VideoFileClip
import sys

# ew, trash hack
import pygame

from pygame import mixer


import os

# 4:3 aspect ratio
# this is gonna be 48x36

pygame.init()

mixer.init()
mixer.music.load("out.mp3")
mixer.music.set_volume(1)
def main():
    bad_ape()





def bad_ape():
    clear = lambda: os.system('cls')
    clear()

    print("Loading video...")
    ### Setup
    badAppleClip: VideoFileClip = VideoFileClip("bad_apple.mp4")
    badAppleFrameGen = badAppleClip.iter_frames()


    list_app = list(badAppleFrameGen)

    # so it turns it into [frame_num][height][width]
    #print(len(list_app))
    #print(len(list_app[0]))
    #print(len(list_app[0][0]))

    frame = 0

    clock = pygame.time.Clock()
    print("Done!\n")

    input("Press enter to start...\n")

    clear()

    out_string = ""
    mixer.music.play()
    while True:
        curframe = list_app[frame]

        for y in range(36):
            for x in range(96):
                pix = curframe[y*10][x*5]
                if pix[0] <= 128:
                    out_string += "."
                else:
                    out_string += "#"
            out_string += "\n"
        
        clock.tick(30)
        #print(out_string)
        sys.stdout.write(out_string)
        print("FPS: "+str(clock.get_fps()))
        out_string = ""
        
        # clear()
        sys.stdout.write(f'\033[{1};{1}H')
        frame += 1
        if frame >= 6584:
            clear()
            print("Fin")
            break





if __name__ == "__main__":
    main()