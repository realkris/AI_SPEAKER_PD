# Project AI Speaker 

### Our Contributors 💫
<a href="https://github.com/realkris/AI_SPEAKER_PD/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=realkris/AI_SPEAKER_PD" />
</a>

*Made with [contrib.rocks](https://contrib.rocks)*

## Project Overview:

In this project we introduce our approach for an advanced Artificial Intelligence (AI) Speaker that seamlessly integrates Text-to-Speech (TTS) and Wave-to-Lip (Wav2Lip) Shape Prediction models. The outcome is a framework that harmonizes the capabilities of natural language processing with Computer vision techniques. The AI Speaker's primary objective is to transform news scripts by offering enhanced realism through a fusion of lifelike speech synthesis and synchronized lip movements. By bridging the gap between auditory and visual modalities, this innovative solution aims to elevate user engagement and enhance the overall Quality of Experience (QoE) in multimedia communication. Key highlights of the AI Speaker include its ability to generate speech with emotional tones, synchronize lip movements accurately across diverse languages, and facilitate user-friendly script input for smooth integration into various applications. By prioritizing adaptability and user convenience, the integrated AI Speaker promises an intuitive experience, which causes deeper interactions between technology and human communication within multimedia environments.

## Hardware and Software Requirements:
If you have a GPU, recommended

- **Hardware:**
  - At least Core i7 10700, GPU optional

- **Software:**
  - is described in the installation of the project
Get a Anaconda installed with a environment of python==3.8, then: 

## Instructions for Setup and Execution:

### Quick Start
#### 1. Building Environment
Get a Anaconda installed with a environment of python==3.8, then: 

If you have a GPU, recommended

```
python -m pip install paddlepaddle-gpu==2.4.1.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```
after that,
```
pip install -r requirements.txt
```
I've tested it on CUDA 11.2 with CUDNN 8.x. 


For CPU only:
```
pip install -r requirements-cpu.txt
```

#### 2. Installations

1. Make sure you have 'Visaul Studio Build Tools' and 'ffmpeg' installed.

#### 3. Demo

Execute:

```
python app.py
```
open the website url and write the words that need to be generated as variable subtitles or simply use the deafault text and submit.

That's all folks.


---

By following these instructions, anyone should be able to successfully set up and run the project. If you encounter any issues or have questions, feel free to contact [provide contact information].

Thank you for using our project!




#### 4. To train the model

**Training is only needed when necessary.**

There are three models used in this project:

1. first_order_predictor: in create_virtual_human.py
2. TTS model: in PaddleTools/TTS.py
3. wav to lip model: also in PaddleTools/TTS.py

The TTS model and wav to lip model is trainable. 
The details for training process will be unleased after the grade publication of this course in the interest of plagiarism protection.




### Description for default.yaml, no need to change by default
```
GANDRIVING:
   FOM_INPUT_IMAGE: './file/input/test.png' #Static image with human face. If you want to change the image, please replace this file
   FOM_DRIVING_VIDEO: './file/input/zimeng.mp4' # Used as a reference video for emoticon migration. If the generation effect is not good, please replace this file, but it is generally not used.
   FOM_OUTPUT_VIDEO: './file/input/test.mp4' #Video output path after expression migration

TTS:
   SPEED: 1.0 #SPEED
   PITCH: 1.0 #pitch
   ENERGY: 1.0 #Pronunciation energy level

SAVEPATH:
   VIDEO_SAVE_PATH: './file/output/video/' #Path to save audio
   AUDIO_SAVE_PATH: './file/output/audio/' #Save the path to generate the virtual anchor video
```

## Acknowledgements

This project utilizes code from the following sources:

- The implementation of loading weights for TTS and WAV2LiP modules is from [paddlepaddle example](https://github.com/PaddlePaddle/PaddleSpeech/tree/develop?tab=readme-ov-file)
- The implementation of creating virtual human is from [CSDN](http://t.csdnimg.cn/HWkxj)
- The implementation of the submit button in front end was adapted from [Claudio Scotto](https://codepen.io/claudiosc8/pen/OOgeMj).
- The background image utilized in this project was adapted from [wallpapercave](https://wallpapercave.com/wallpaper-gif)
