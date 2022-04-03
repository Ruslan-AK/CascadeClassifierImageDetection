source https://youtu.be/XrCAvs9AePM


C:\Users\Ruslan2\Downloads\opencv\build\x64\vc14\bin\opencv_annotation.exe --annotations=pos.txt --images=positive/


# You click once to set the upper left corner, then again to set the lower right corner.
# Press 'c' to confirm.
# Or 'd' to undo the previous confirmation.
# When done, click 'n' to move to the next image.
# Press 'esc' to exit.
# Will exit automatically when you've annotated all of the images



# generate positive samples from the annotations to get a vector file using:
# C:\Users\Ruslan2\Downloads\opencv\build\x64\vc14\bin\opencv_createsamples.exe -info pos.txt -w 12 -h 12 -num 1000 -vec pos.vec

# train the cascade classifier model using:
# C:\Users\Ruslan2\Downloads\opencv\build\x64\vc14\bin\opencv_traincascade.exe -data cascade\ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 12 -h 12 -maxFalseAlarmRate 0.3 -minHitRate 0.9

# my final classifier training arguments:
# C:\Users\Ruslan2\Downloads\opencv\build\x64\vc14\bin\opencv_traincascade.exe -data cascade\ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 200 -numNeg 1000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999
