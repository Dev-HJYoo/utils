#!/bin/sh

INPUT_DIR=INPUT_VIDEOs_FOLDER_PATH

BASE_DIR=SAVE_VIDEOS_FOLDEL_PATH
OUTPUT_DIR=$BASE_DIR/Resampling_24
OUTPUT_DIR2=$BASE_DIR/Resampling_16
FILES=$(ls $INPUT_DIR | grep .mp4)

for FILE in $FILES
do
    name='basename $FILE'
    FILENAME="${FILE%.*}"
    ffmpeg -i $INPUT_DIR/$FILE -r 24 -c:v libx264 -b:v 3M -strict -2 $OUTPUT_DIR/$FILENAME.mp4
    ffmpeg -i $INPUT_DIR/$FILE -r 16 -c:v libx264 -b:v 3M -strict -2 $OUTPUT_DIR2/$FILENAME.mp4
done