from setuptools import setup, find_packages

PLUGIN_ENTRY_POINT = 'google_translate_tts = ovos_tts_plugin_google_cloud_translate:GoogleTranslateTTSPlugin'

setup(
    name='ovos-tts-plugin-google-cloud-translate',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ovos-core',
        'ovos-plugin-manager',
        'gtts',
        'requests'
    ],
    entry_points={'mycroft.plugin.tts': [PLUGIN_ENTRY_POINT]},
    author='Mosi',
    author_email='zxcvbnm914121@pinklab.art',
    description='A Google Translate TTS plugin for OVOS',
    license='Apache License 2.0',
    keywords='OVOS TTS Google Translate',
    url='http://your.plugin.url',   # 프로젝트 URL 또는 GitHub URL
)
