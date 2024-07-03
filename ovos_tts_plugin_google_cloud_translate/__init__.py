import requests
from gtts import gTTS
from ovos_plugin_manager.templates.tts import TTS, TTSValidator
from ovos_utils.log import LOG

class GoogleTranslateTTSPlugin(TTS):
    def __init__(self, *args, **kwargs):
        ssml_tags = ["speak", "s", "w", "voice", "prosody",
                     "say-as", "break", "sub", "phoneme"]
        super().__init__(*args, **kwargs, audio_ext="mp3", ssml_tags=ssml_tags)
        self._api_key = self.config.get('api_key')
        self._target_lang = self.config.get('lang', 'ko')
        if not self._api_key:
            raise ValueError("API key is required for Google Translate TTS")
        self.validator = GoogleTTSValidator(self)
        LOG.info(f"GoogleTranslateTTSPlugin initialized with lang={self._target_lang} and api_key={self._api_key}")

    def get_tts(self, sentence, wav_file):
        LOG.info(f"get_tts called with sentence: {sentence}")
        try:
            # 번역
            translated_text = self.translate_text(self._api_key, self._target_lang, sentence)
            LOG.info(f"Translated Text: {translated_text}")

            # TTS
            tts = gTTS(text=translated_text, lang=self._target_lang)
            tts.save(wav_file)
            LOG.info(f"TTS saved to {wav_file}")
            return wav_file, None
        except Exception as e:
            LOG.error(f"Error in get_tts: {str(e)}")
            return None, str(e)

    def translate_text(self, api_key: str, target: str, text: str) -> str:
        LOG.info(f"translate_text called with text: {text}")
        url = "https://translation.googleapis.com/language/translate/v2"
        params = {
            'q': text,
            'target': target,
            'key': api_key
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            LOG.error(f"Translation API error: {response.status_code}, {response.text}")
            raise Exception(f"Error: {response.status_code}, {response.text}")

        result = response.json()
        LOG.info("Translation successful")
        return result['data']['translations'][0]['translatedText']

    @property
    def available_languages(self):
        """Return languages supported by this TTS implementation in this state."""
        return {"en", "ko"}

class GoogleTTSValidator(TTSValidator):
    def __init__(self, tts):
        LOG.info("GoogleTTSValidator __init__ called")
        super().__init__(tts)

    def validate_lang(self):
        LOG.info("validate_lang called")
        # 필요한 경우 언어 검증 로직 추가

    def validate_connection(self):
        LOG.info("validate_connection called")
        # 필요한 경우 연결 검증 로직 추가

    def get_tts_class(self):
        return GoogleTranslateTTSPlugin

# 샘플 유효한 구성 설정
GoogleTranslateTTSConfig = {
    lang: [{"lang": lang,
            "display_name": f"GoogleTranslateTTS ({lang})",
            "priority": 70,
            "offline": False}]
    for lang in ["en", "ko"]
}
