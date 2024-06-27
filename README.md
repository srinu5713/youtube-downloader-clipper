# YouTube Downloader and Clipper

This repository contains a Streamlit app for downloading and clipping YouTube videos and audio. The app allows users to download videos in the highest resolution, convert audio to MP3, and clip both video and audio to desired lengths.

## Features

- **Download YouTube Videos:** Download videos in the highest available resolution.
- **Convert Audio to MP3:** Extract and convert audio from YouTube videos to MP3 format.
- **Clip Video:** Select and download specific segments of YouTube videos.
- **Clip Audio:** Select and download specific segments of audio from YouTube videos.

## How to Run

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/srinu5713/youtube-downloader-clipper.git
    cd youtube-downloader-clipper
    ```

2. **Install the Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App:**

    ```bash
    streamlit run yt.py
    ```

4. **Use the App:**
    - Open your browser and navigate to the URL provided by Streamlit.
    - Enter the YouTube video URL.
    - Choose your desired action: Download Video, Download Audio (MP3), Clip Video, or Clip Audio.
    - Follow the instructions provided in the app to complete your action.

## Project Structure

```plaintext
.
├── app.py                 # Main Streamlit application file
├── requirements.txt       # Required Python packages
└── README.md              # This readme file

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to explore the code, experiment with different configurations, and contribute to the advancement of file management tools. For any questions or issues, please open an issue in the repository. Thank you for your interest and contributions!
