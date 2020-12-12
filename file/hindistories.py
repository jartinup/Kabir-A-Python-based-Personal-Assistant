import time
import random
import webbrowser
import sys

videos = [
'https://www.youtube.com/watch?v=o_MUyflsE_4',
'https://www.youtube.com/watch?v=6z-rInMyw3E',
'https://www.youtube.com/watch?v=3aehnepCdwo',
'https://www.youtube.com/watch?v=f6BFbFmHIFA',
'https://www.youtube.com/watch?v=VgEFpaLDarU',
'https://www.youtube.com/watch?v=hl37dhen8_0',
'https://www.youtube.com/watch?v=RG-HUkwd0yc',
'https://www.youtube.com/watch?v=JUg1crctSSI',
'https://www.youtube.com/watch?v=6TDTzNyF2As',
'https://www.youtube.com/watch?v=042VBIf9vj8',
'https://www.youtube.com/watch?v=tkVTSA7smYU',
'https://www.youtube.com/watch?v=-8jA35Vlef8',
'https://www.youtube.com/watch?v=F__W7wiwtsk',
'https://www.youtube.com/watch?v=olhPFESySpY',
'https://www.youtube.com/watch?v=V3hlTLKpDoA',
'https://www.youtube.com/watch?v=HJWqffRvC9s',
'https://www.youtube.com/watch?v=Jh5x5aBPvXM',
'https://www.youtube.com/watch?v=csbhoVPes80',
'https://www.youtube.com/watch?v=dUg0I-B2FUE',
'https://www.youtube.com/watch?v=Z96-q4ovIOw',
'https://www.youtube.com/watch?v=1LPHkSZis3s',
'https://www.youtube.com/watch?v=W4Ycp_RjdHE',
'https://www.youtube.com/watch?v=4K5fX86gpTg',
'https://www.youtube.com/watch?v=SQ6N2Psd1hY',
'https://www.youtube.com/watch?v=1-SiF33kXYw'
]
random_video = random.randint(0,25)
n=1
for i in range(n):
    webbrowser.open(videos[random_video])

sys.exit()




    