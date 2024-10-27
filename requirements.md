## Requirements

To ensure CALCY functions correctly, especially for its text-to-speech capabilities, the following Python libraries and system packages are required:

1. **pyttsx3**:
   - This library enables CALCY's text-to-speech functionality, allowing the program to audibly respond to user inputs.
   - `pyttsx3` is an offline library, so it does not require an internet connection and supports multiple voices for added customization.

2. **pypiwin32**:
   - For **Windows** users, `pypiwin32` is essential as it enables `pyttsx3` to interact with the Windows Speech API (SAPI5), making text-to-speech possible on Windows systems.
   - This library is automatically installed on Windows via `requirements.txt`, but if any issues arise, it can be installed manually with `pip install pypiwin32`.

3. **espeak**:
   - For **Linux** users, `espeak` is required by `pyttsx3` to produce speech output.
   - To install `espeak` on Linux, users may need to run the following command in addition to installing it with `pip`:
     ```bash
     sudo apt install espeak
     ```

### Installing Requirements

To install all required libraries, simply run the following command in the project directory:
```bash
pip install -r requirements.txt
