import os
import time

os.system(f'python create_virtual_human.py --config default.yaml')

time.sleep(5) # For GPU to release load

# Replace the sentence below.
subtitles = 'Zhang is a computer science Ph.D. student focuses in Autonomous Driving: Three-D detection at VIVA research, University of Ottawa. Before admission to University of Ottawa, he served as data scientist intern at Flipboard Greater China Area Office at Beijing, China. In addition, he was a senior visiting scholar at the United Nations Italy at 2021. He is concerned and committed to helping equal education in underdeveloped areas of Jiaodong.'

os.system(f"python general_demo.py --human file/input/test.mp4 --output output.mp4 --text '{subtitles}'")
