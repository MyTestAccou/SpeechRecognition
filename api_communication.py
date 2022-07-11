import requests
from my_secret_api import API_SECRET_ASSEMBLYAI
import time


# upload 
# use doc example
# for record i use terminal arecord and namefile.wav and its save file in curent dir or home dir 
#  python main.py and filename.wav and we have path to you file 

upload_endpoint = 'https://api.assemblyai.com/v2/upload'

transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'


headers = {'authorization': API_SECRET_ASSEMBLYAI}

def upload(filename):
    def read_file(filename, chunk_size=5242880):       # number of mb 5Mb file 
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url

# transcribe
# this code from doc to 
def transcribe(audio_url):
    transcript_request = { "audio_url": audio_url}

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    # print(transcript_response.json())

    job_id = transcript_response.json()['id']
    
    return job_id



# poll
# id oh6om7pevo-2541-4543-97c9-1112a57d4ea8 from json file we need to understnd redy or not our transcription
def poll(transcript_id):
    poling_endpoint = transcript_endpoint + '/' + transcript_id
    poling_response = requests.get(poling_endpoint, headers=headers)
    return poling_response.json()



# get json status processing that means in job progress will be wait some times


def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']


        print('Waiting some couple of times')
        time.sleep(30)


# save transcrpt
def save_transcript(audio_url, filename):
    data , error = get_transcription_result_url(audio_url)

    if data:
        text_filename = filename + '.txt'
        with open(text_filename, 'w') as f:
            f.write(data['text'])
        print('Transcription save') 
    elif error:
        print('Error', error)