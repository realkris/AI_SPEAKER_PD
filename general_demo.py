# -*- coding: utf-8 -*-  
import os
import argparse

#引入飞桨生态的语音和GAN依赖
from paddlespeech.cli.tts.infer import TTSExecutor
from PaddleTools.GAN import wav2lip

parser = argparse.ArgumentParser()
parser.add_argument('--human', type=str,default='', help='human video', required=True)
parser.add_argument('--output', type=str, default='output.mp4', help='output video')
parser.add_argument('--text', type=str,default='ACROSS THE GREAT WALL WE CAN REACH EVERY CORNER IN THE WORLD.', help='human video', required=False)

if __name__ == '__main__':
    args = parser.parse_args()
    tts = TTSExecutor()
    wavfile = "output.wav"
    tts(text=args.text, lang='en', output=wavfile, voc="pwgan_vctk", am="fastspeech2_vctk")
    video = wav2lip(args.human,wavfile,args.output) #将音频合成到唇形视频
    os.remove(wavfile) #删除临时的音频文件
    print('The video is generated and the output path is {}'.format(args.output))
