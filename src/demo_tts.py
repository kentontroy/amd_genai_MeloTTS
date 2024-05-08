from melo.api import TTS
import getopt
import os
import sys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

SPEECH_SPEED = 0.80
# CPU is sufficient for real-time inference.
# You can set it manually to 'cpu' or 'cuda' or 'cuda:0' or 'mps'
DEVICE = "cpu"
EN_ACCENT = "EN_INDIA"

def show_help():
  print("demo_tts.py -t <text> -o <output_file>")
  sys.exit(1)

def generate_speech_from_text(text: str, file_output_path: str):
# Indian accent
  file_output_path = "en-india.wav"
  model.tts_to_file(text, speaker_ids[EN_ACCENT], file_output_path, speed=SPEECH_SPEED)

if __name__== '__main__':
  c_args = sys.argv[1:]
  if len(c_args) == 0:
    show_help()
  c_options = "t:o:"
  c_long_options = ["text=", "output_file="]
  try:
    args, vals = getopt.getopt(c_args, c_options, c_long_options)
    found_all_options = False
    for arg, val in args:
      if arg in ["-t", "--text"]:
        text = val
      elif arg in ["-o", "--output_file"]:
        file_output_path = val
    if len(text) > 0 and len(file_output_path) > 0:
      found_all_options = True
    if found_all_options:
      model = TTS(language="EN", device=DEVICE)
      speaker_ids = model.hps.data.spk2id
      generate_speech_from_text(text, file_output_path)
    else:
      show_help()

  except getopt.error as err:
    print(str(err))
