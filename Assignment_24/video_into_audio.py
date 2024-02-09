
import time
from threading import Thread
import requests 
from moviepy import editor

def downloader(url , file_name) : 
    result = requests.get(url)
    f = open(file_name , "wb")
    f.write(result.content) 
    f.close()

video_list = []
outputs = []
videos = [ "https://aspb15.cdn.asset.aparat.com/aparat-video/00704eb4d3f5ec4600ef1f47767ddd7f14028226-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjMzODViZTRmODE4NDAyYTRmZjc3NWU4NjhjYjZmNjM5IiwiZXhwIjoxNjc4NzIyMDU3LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.CscwAqFd9pSMCABfmIaqlmDHghKsdT-C_VNYIEUH94Q" ,
           "https://aspb3.cdn.asset.aparat.com/aparat-video/59502de31f677be549ad5dc2c9a639f014143770-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjA0OWE5NTA0M2I1ZmMzMDMyOTE2OThkN2JjMmVmYTZlIiwiZXhwIjoxNjc4NzIxODcwLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.YWhWqxyhLNzwTBQfXxth1evrJksebxWjYWEPae1LI64" ,
           "https://aspb3.cdn.asset.aparat.com/aparat-video/71a25cb7bf41a749a92c127b19b7f63910411185-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjRlNTQyNTQyODc3YmQ4MmUzMGE5ZmNhYjYxNzU0ODMxIiwiZXhwIjoxNjc4NzIyMTY1LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.ixCOAcyP08QN9Hmg6p30wzeShQX8moc11Tf2YRh30_I" ,
           "https://aspb11.cdn.asset.aparat.com/aparat-video/5521fe3e0d12c444101acc05468c5e7514605620-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjNhMWEwOTZmMzQyOTdjZWExZGQ3ZDc2ZjAwODM4ZWY5IiwiZXhwIjoxNjc4NzIyMjQwLCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.HJLpuLobk2S9XrF2zb-6XUGlJ7baoSPZqcBmLAB48ng" ,
           "https://as10.cdn.asset.aparat.com/aparat-video/a3672b5779abfaf20d257214a61fd4088244946-240p.mp4?wmsAuthSign=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6IjcxMjBmZmQ3NTZmYjhlZDM1MTUyY2UyYjUwOTE0ZjAzIiwiZXhwIjoxNjc4NzIyODU2LCJpc3MiOiJTYWJhIElkZWEgR1NJRyJ9.bA2SeyJjaY6Ic-HgbFpW50y3QTT8KOYN1_8ul0yRD84" ]

for i in range(0,5) :    
    video_list=downloader(videos[i] , f"output/video{i+1}.mp4")
    outputs.append(f"output/video{i+1}.mp4")

def convert_video_into_audio(i , video):
        media = editor.VideoFileClip(video)
        media.audio.write_audiofile(f"audio/audio{i+1}.mp3")
        

def normal_execution():
    start_time = time.time()
    for i in range(1,6) :
        vid = editor.VideoFileClip(f"output/video{i}.mp4")
        vid.audio.write_audiofile(f"output/audio{i}.mp3")
    end_time = time.time()
    print(f"\nDuration of normal converting is: {end_time - start_time} seconds.\n")

def multi_threading():
    start = time.time()
    threads = []
    for index , file in enumerate(outputs) :      
        threads.append(Thread(target= convert_video_into_audio ,args= [index, file]))
        
    for t in threads :
        t.start()
    for t in threads :
        t.join()

    end = time.time()
    print(f"\nDuration of converting with multi threading is: {end - start} seconds.\n")

normal_execution()
multi_threading()