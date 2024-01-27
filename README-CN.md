# PaddleBoBo 
## Quick Start
### 1.安装依赖包*
```
pip install -r requirement.txt
```
### 2.配置文件说明(default.yaml)，默认无需更改
```
GANDRIVING:
  FOM_INPUT_IMAGE: './file/input/test.png' #带人脸的静态图，如要更换形象，请替换这个文件
  FOM_DRIVING_VIDEO: './file/input/zimeng.mp4' #用作表情迁移的参考视频，如果生成效果不好，请更换这个文件，但一般不用
  FOM_OUTPUT_VIDEO: './file/input/test.mp4' #表情迁移后的视频输出路径

TTS:
  SPEED: 1.0 #语速
  PITCH: 1.0 #音高
  ENERGY: 1.0 #发音能级

SAVEPATH:
  VIDEO_SAVE_PATH: './file/output/video/' #保存音频的路径
  AUDIO_SAVE_PATH: './file/output/audio/' #保存生成虚拟主播视频的路径
```

### 运行

1. 确保目标形象存放在了'./file/input/test.png'
2. 进入runner.py，将需要生成的话写到subtitles后面。
3. 运行

```
python runner.py
```

这就是一切了。

*注意，需要16GB以上显存NVIDIA GPU。
