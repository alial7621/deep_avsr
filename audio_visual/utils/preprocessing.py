"""
Author: Smeet Shah
Copyright (c) 2020 Smeet Shah
File part of 'deep_avsr' GitHub repository available at -
https://github.com/lordmartian/deep_avsr
"""

import torch
import os



def preprocess_sample(file, params):

    """
    Function to preprocess each data sample.
    """

    videoFile = file + ".mp4"
    audioFile = file + ".wav"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


    #Extract the audio from the video file using the FFmpeg utility and save it to a wav file.
    v2aCommand = "ffmpeg -y -v quiet -i " + videoFile + " -ac 1 -ar 16000 -vn " + audioFile
    os.system(v2aCommand)

    return
