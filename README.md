
# Audio Transcription and Text-to-Speech API

## Project Overview

This project provides a FastAPI-based API capable of accepting audio files, converting them to a compatible format if necessary, and transcribing the speech to text. Additionally, it includes Text-to-Speech (TTS) functionality.

## Approach to the Problem

- The objective was to develop a FastAPI-based API capable of accepting audio files in various formats, converting them to a compatible WAV format if necessary, and transcribing the speech to text.
  
- To achieve this, I utilized the `pydub` library for audio format conversion and the `speech_recognition` library for transcription. Additionally, I used the `pyttsx3` library for text-to-speech (TTS) functionality.

- The process involved:
  1. **File Validation:** Ensuring the uploaded file is an audio file.
  2. **File Conversion:** Using `pydub` to convert the audio to WAV format if it wasn't already in that format.
  3. **Transcription:** Employing `speech_recognition` to transcribe the audio to text.
  4. **Error Handling:** Implementing appropriate error handling to manage unsupported file types, transcription errors, and other exceptions.

## Future Enhancements

If more time were available, the following improvements could be considered:

1. **Support for Multiple Audio Formats:** Expanding support to include additional audio formats beyond MP3 and WAV.
2. **Enhanced Error Handling:** Providing more detailed error messages and handling edge cases more gracefully.
3. **Performance Optimization:** Implementing asynchronous processing for audio conversion and transcription to improve performance.
4. **User Authentication:** Adding user authentication and authorization to secure the API endpoints.
5. **Logging and Monitoring:** Integrating logging and monitoring to track usage and detect issues proactively.

## Libraries Chosen for STT (Speech-to-Text)

- **`pydub`:** Selected for its simplicity and ease of use in handling various audio formats. It provides a high-level interface for audio operations, making it suitable for tasks like format conversion.
  
- **`speech_recognition`:** Chosen for its straightforward integration with multiple speech recognition engines, including Google's Web Speech API. It offers a simple interface for transcribing audio to text.

## Library for TTS (Text-to-Speech)

- **`pyttsx3`:** Chosen for its ability to generate speech from text. It is an offline library, which allows for text-to-speech functionality without requiring an internet connection. It also supports multiple speech engines and is cross-platform.

These libraries were chosen to balance ease of use, functionality, and performance for the project's requirements.

  ![image](https://github.com/user-attachments/assets/81a86e89-8adb-4756-979a-4a9d8c6fdebc)
  
  Audible
  ![image](https://github.com/user-attachments/assets/162bc081-71fe-473e-9f2b-2db09f61d359)

