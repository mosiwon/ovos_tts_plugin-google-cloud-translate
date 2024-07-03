###
```bash
pip install git+https://github.com/mosiwon/ovos_stt_plugin-google-cloud-translate.git
```

## Configuration

* in mycroft.conf
```json
{
  "tts": {
    "module": "google_translate_tts",
    "google_translate_tts": {
      "api_key": "YOUR_GOOGLE_API_KEY",
      "lang": "ko"
    }
  }
}