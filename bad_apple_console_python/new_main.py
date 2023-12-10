from moviepy.video.io.VideoFileClip import VideoFileClip
import sys

# ew, trash hack
import pygame

from pygame import mixer


import os

# 4:3 aspect ratio
# this is gonna be 96x36

pygame.init()

mixer.init()
mixer.music.load("out.mp3")
mixer.music.set_volume(1)

song_len_s = mixer.Sound("out.mp3").get_length()
song_len_ms = int(song_len_s*1000)

def main():
    bad_ape()


def bad_ape():
    clear = lambda: os.system('cls')
    clear()

    print("Loading video...")
    ### Setup
    badAppleClip: VideoFileClip = VideoFileClip("bad_apple.mp4")
    print("Video loaded.")
    print("Generating frame data...")
    badAppleFrameGen = badAppleClip.iter_frames()
    print("Generated.")
    
    print("Converting to array...")
    list_app = list(badAppleFrameGen)
    vid_len_frames = len(list_app)
    print("In array form.")

    clock = pygame.time.Clock()
    print("Done!\n")
    
    input("Press enter to start...\n")

    clear()

    mixer.music.play()

    while not mixer.music.get_busy():
        pygame.time.delay(1)
        

    while True:
        if mixer.music.get_pos()+20 >= song_len_ms:
            clear()
            print("Fin")
            break

        song_percentage = mixer.music.get_pos()/song_len_ms

        
        fnum = int(song_percentage*vid_len_frames)
        curframe = list_app[fnum]



        out_string = ""
        for y in range(36):
            for x in range(96):
                pix = curframe[y*10][x*5]
                if pix[0] <= 128:
                    out_string += " " # .
                else:
                    out_string += "#" # #
            out_string += "\n"
            
        clock.tick(60)


        #print(out_string)
        sys.stdout.write(out_string)
        #print("FPS: "+str(clock.get_fps()))
        
        print(str(int(song_percentage*100))+"%")
        # print("FPS: "+str(int(clock.get_fps()*100)/100) + " (No lag if above 30 because the video is 30 fps)     ")
        # print(mixer.music.get_pos())
        # clear()
        sys.stdout.write(f'\033[{1};{1}H')


if __name__ == "__main__":
    main()
