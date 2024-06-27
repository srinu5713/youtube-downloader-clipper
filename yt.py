import os
import streamlit as st
from pytube import YouTube
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip

# Streamlit App
st.title('YouTube Video/Audio Downloader and Clipper')

# Define the download directory
download_directory = 'C:/Users/HP/Downloads'

# Input field for YouTube video URL
video_url = st.text_input('Enter YouTube Video URL')

# Initialize variable to keep track of the chosen option
chosen_option = None

if video_url:
    try:
        # Create YouTube object
        yt = YouTube(video_url)

        # Display video details
        st.write(f"Title: {yt.title}")
        st.write(f"Author: {yt.author}")
        st.write(f"Views: {yt.views}")
        st.write(f"Length: {yt.length} seconds")
        st.write(f"Rating: {yt.rating}")

        # Get the highest resolution stream
        highest_resolution_stream = yt.streams.get_highest_resolution()

        # Display download options
        st.subheader('Download Options')

        # Options for selecting download type using tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Video", "Audio (MP3)", "Clip Video", "Clip Audio"])

        with tab1:
            st.header("Video")
            st.write("Instructions for downloading video:")
            st.write("1. Click the 'Download Video' button.")
            st.write(
                "2. Your video will start downloading. Check your Downloads directory.")

            if st.button("Download Video"):
                st.write("Downloading video...")
                filename = os.path.basename(
                    highest_resolution_stream.default_filename)
                base_name, extension = os.path.splitext(filename)
                file_number = 1
                while os.path.exists(os.path.join(download_directory, filename)):
                    filename = f"{base_name}[{file_number}]{extension}"
                    file_number += 1
                highest_resolution_stream.download(
                    output_path=download_directory, filename=filename)
                st.success(
                    "Download complete! Check your Downloads directory.")

        with tab2:
            st.header("Audio")
            st.write("Instructions for downloading audio (MP3):")
            st.write("1. Click the 'Download Audio (MP3)' button.")
            st.write(
                "2. Your audio will start converting and downloading. Check your Downloads directory.")

            if st.button("Download Audio (MP3)"):
                st.write("Converting to MP3...")
                audio_stream = yt.streams.filter(only_audio=True).first()
                filename = os.path.basename(audio_stream.default_filename)
                base_name, extension = os.path.splitext(filename)
                file_number = 1
                while os.path.exists(os.path.join(download_directory, filename)):
                    filename = f"{base_name}[{file_number}]{extension}"
                    file_number += 1
                audio_file = audio_stream.download(
                    output_path=download_directory, filename=filename)
                audio_file_mp3 = os.path.splitext(audio_file)[0] + ".mp3"
                os.rename(audio_file, audio_file_mp3)
                st.success(
                    "Audio (MP3) conversion complete! Check your Downloads directory.")

        with tab3:
            st.header("Clip Video")
            st.write("Instructions for clipping video:")
            st.write(
                "1. Adjust the sliders to select the start and end times of the clip.")
            st.write(
                "2. Click the 'Preview Clip' button to preview the selected range.")
            st.write(
                "3. If satisfied, the 'Download Clipped Video' button will be enabled.")

            st.write("Adjust the sliders to select start and end times:")
            start_time_video = st.slider(
                "Start Time", 0, yt.length, 0, key="start_time_video")
            end_time_video = st.slider(
                "End Time", start_time_video, yt.length, yt.length, key="end_time_video")

            preview_generated_video = False

            if start_time_video < end_time_video:
                st.write(
                    f"Selected Range: {start_time_video} seconds to {end_time_video} seconds")

                # Show button to preview the clip
                if st.button("Preview Clip"):
                    st.write("Preview of Selected Range:")
                    with st.spinner('Loading video...'):
                        video_path = highest_resolution_stream.download()
                        clip = VideoFileClip(video_path).subclip(
                            start_time_video, end_time_video)
                        clip_path = os.path.join(
                            download_directory, "preview_clip.mp4")
                        clip.write_videofile(clip_path)
                        st.video(clip_path, format='video/mp4')
                        preview_generated_video = True

                if preview_generated_video:
                    if st.button("Download Clipped Video", key="download_clip_video"):
                        st.write("Clipping video...")
                        # Set output filename
                        output_filename = f"{yt.title}_clipped.mp4"
                        # Clip the video using moviepy
                        clip_output_path = os.path.join(
                            download_directory, output_filename)
                        clip = VideoFileClip(video_path).subclip(
                            start_time_video, end_time_video)
                        clip.write_videofile(clip_output_path)
                        st.success(
                            "Video clipping complete! Check your Downloads directory.")
            else:
                st.warning("End time should be greater than start time.")

        with tab4:
            st.write("Instructions for clipping audio:")
            st.write(
                "1. Adjust the sliders to select the start and end times of the clip.")
            st.write(
                "2. Click the 'Preview Clip' button to preview the selected range.")
            st.write(
                "3. If satisfied, the 'Download Clipped Audio' button will be enabled.")

            st.write("Adjust the sliders to select start and end times:")
            start_time_audio = st.slider(
                "Start Time", 0, yt.length, 0, key="start_time_audio")
            end_time_audio = st.slider(
                "End Time", start_time_audio, yt.length, yt.length, key="end_time_audio")

            preview_generated_audio = False

            if start_time_audio < end_time_audio:
                st.write(
                    f"Selected Range: {start_time_audio} seconds to {end_time_audio} seconds")

                # Show button to preview the clip
                if st.button("Preview Clip", key="preview_clip_audio"):  # Unique key
                    st.write("Preview of Selected Range:")
                    with st.spinner('Loading audio...'):
                        audio_stream = yt.streams.filter(
                            only_audio=True).first()
                        audio_path = os.path.join(
                            download_directory, "original_audio.mp3")
                        audio_stream.download(
                            output_path=download_directory, filename="original_audio.mp3")
                        audio_clip = AudioFileClip(audio_path).subclip(
                            start_time_audio, end_time_audio)
                        audio_clip_path = os.path.join(
                            download_directory, "preview_audio_clip.mp3")
                        audio_clip.write_audiofile(audio_clip_path)
                        st.audio(audio_clip_path, format='audio/mp3')
                        preview_generated_audio = True

                if preview_generated_audio:
                    if st.button("Download Clipped Audio", key="download_clip_audio"):  # Unique key
                        st.write("Clipping audio...")
                        # Set output filename
                        output_filename = f"{yt.title}_clipped_audio.mp3"
                        # Clip the audio using moviepy
                        audio_clip_output_path = os.path.join(
                            download_directory, output_filename)
                        audio_clip = AudioFileClip(audio_path).subclip(
                            start_time_audio, end_time_audio)
                        audio_clip.write_audiofile(audio_clip_output_path)
                        st.success(
                            "Audio clipping complete! Check your Downloads directory.")
                else:
                    st.warning(
                        "Please generate a preview before downloading the clipped audio.")
            else:
                st.error("End time should be greater than start time.")


    except Exception as e:
        st.error(f"An error occurred: {e}")