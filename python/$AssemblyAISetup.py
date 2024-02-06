# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API token
aai.settings.api_key = f"41e787662ee947c3aeffaa42931b49db"

# URL of the file to transcribe
# FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
# FILE_URL = 'C:\venetianSQL.mp3'
# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'
# FolderUrl = r'C:\Users\mmoha\OneDrive\07InterviewRecordings'
FolderUrl = r'C:\pyNeetCode400Dec\leetcode\python'
FILE_URL = 'JHV1hLi5Sd8.m4a'
FullUrl = FolderUrl+ "\\" + FILE_URL
config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FullUrl,
  config=config
)

for utterance in transcript.utterances:
  print(f"Speaker {utterance.speaker}: {utterance.text}")
