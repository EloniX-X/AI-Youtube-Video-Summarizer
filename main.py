import openai 

from youtube_transcript_api import YouTubeTranscriptApi

srt = YouTubeTranscriptApi.get_transcript("pJwR5pv0_gs", languages=['en'])

captions = " ".join([segment['text'] for segment in srt])




openai.api_key = 'WOAH WOAH WOAHHHH BUDDY SLOW DOWN GET YOUR OWN GYATDAMN KEY'

def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

    model=model,

    messages=messages,

    temperature=0,

    )

    return response.choices[0].message["content"]


def prompt(prompt):
    response = get_completion(prompt)

    print(response)



prpr = str(captions)
preprompt = "can you summarize this youtube video?: " + prpr

prompt(preprompt)
