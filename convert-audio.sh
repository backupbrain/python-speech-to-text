#!/bin/bash

# Convert 24k mp3 to 16x wav/raw
for i in `ls src/*.ts`;
    do ffmpeg -i $i -acodec pcm_s16le -ac 1 -ar 16000 "${i%.*}.wav";
done
