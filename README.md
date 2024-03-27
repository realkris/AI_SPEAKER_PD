# Project AI Speaker for CSI7163
## Quick Start
### 1. Building Environment
Get a Anaconda installed with a environment of python==3.8, then: 

If you have a GPU, recommended

```
python -m pip install paddlepaddle-gpu==2.1.3.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
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



### 2. Demo

1. Make sure the target image is stored in './file/input/test.png'
2. Enter runner.py and write the words that need to be generated as variable subtitles.
3. Execute using Webpage(release soon)
4. Execute in terminal:

```
python runner.py
```

That's all folks.

*Note, NVIDIA GPU with 10GB or more VRAM is required for inferencing with GPU.

The generation process includes generating vitual human avatar, after that we do TTS then fit the speech audio to lips.
It is clealy that vitual human avatar can be used repeatly once generated. In this case, after first time running, you can also do quick inferences on your vitual human avatar pre-generated. 
You run:
```
python general_demo.py --human file/input/test.mp4 --output output.mp4 --text 'Your text for speech here, for example, ACROSS THE GREAT WALL WE CAN REACH EVERY CORNER IN THE WORLD.'
```
For quick inferencing it only takes 30s on a 3080Ti GPU.



### To train the model

**Training is only needed when necessary.**

There are three models used in this project:

1. first_order_predictor: in create_virtual_human.py
2. TTS model: in PaddleTools/TTS.py
3. wav to lip model: also in PaddleTools/TTS.py

The TTS model and wav to lip model is trainable. 
The details for training process will be unleased after the grade publication of CSI7163 in the interest of plagiarism protection.




## Description for default.yaml, no need to change by default
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
