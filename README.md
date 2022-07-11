Use it only for english speech 

# Install or settings
python3 -m venv venv (or psrecogenv like in my case) 
pip install -r rerequirements.txt (i dont export some libs but...)

# Record or take some file with speech
Before start get API key in https://assemblyai.com/

cd to dir when proj exists 

I use linux CMD line you may use what you favor
arecord + yournamefile.wav or .mp3 or .mp4
arecord myfile.wav  

and your have a .wav file to recognition 

# Start 

python3 main.py myfile.wav (or how you named it)
and after you see text file in current directory 
Open and enjoy !
