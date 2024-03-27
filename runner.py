# Import the subprocess module to run shell commands and time module for delays
import subprocess
import time

# Define a function to generate content based on subtitles and a configuration file
def generate(subtitles, config='default.yaml'): 
    # Execute a Python script to create a virtual human using a configuration file
    subprocess.run(['python', 'create_virtual_human.py', '--config', config])
    
    # Wait for 5 seconds to allow the GPU to release any load from the previous task
    time.sleep(5)

    # Execute another Python script to process input video with the provided subtitles
    # and save the output in the 'static/output.mp4' file
    subprocess.run(['python', 'general_demo.py', '--human', 'file/input/test.mp4', '--output', 'static/output.mp4', '--text', subtitles])
