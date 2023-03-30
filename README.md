# Voicet
Step 1: 🎥 Voicet is an innovative Python-based application that facilitates the translation of videos from one language to another via a Progressive Web Application.

Step 2: 🚪 Upon accessing voicet.tech, users are directed to the Login Page. In the event that they don't possess an existing account, they can register via email by navigating to the Sign Up page located within the Navbar.

Step 3: 📝 To create an account, users are prompted to input their email address, username, and password. Upon completing registration, they will be directed to the Login Page, where they can input their login credentials to access their account.

Step 4: 📷 The Gallery exhibits all the videos that the User has posted. To upload a video, users must click on the Upload button located in the Navbar. Users have the option to download any YouTube short or upload any video of their own. After selecting their video, users must click on the Upload button.

Step 5: 🌐 To translate a video, users must select the Translate Button located on the desired video. They must then choose the language into which they wish to translate the video, as well as the gender of the audio. Once these preferences are selected, users must click on the Translate Button.

Step 6: 🤖 In order to translate the video, we generate captions from the video using OpenAI's Whisper STT (Speech To Text) Machine Learning Model. Next, we translate the English subtitles to the target language using Facebook's NLLB ML Model. Finally, we generate audio files from the translations utilizing Vakyansh TTS, merge the audio files, and superimpose them onto the original video. Additionally, we perform lexical and syntactic analysis to ensure the utmost grammatical precision.

Check it out at https://voicet.tech 🌎🗣️

# Setup & Installation on Linux

Install Python packages : `pip install -r requirments.txt`

Install Linux tools : `sudo apt install ffmpeg sox`

Fetch VakyanshTTS Models from https://github.com/Open-Speech-EkStep/vakyansh-models#tts-models
