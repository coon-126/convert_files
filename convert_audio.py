import tkinter as tk
import tkinter.font as tkfont
import tkinter.filedialog as filedialog
from moviepy.editor import *
from tkinter import messagebox

def main(parent=None):
    root = tk.Tk()
    root.title("Audio Converter")

    window_width = 350
    window_height = 400

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.resizable(False, False)

    root.configure(bg="#A0A0A0")

    large_font = tkfont.Font(size=18)

    if parent:
        parent.withdraw()

    def go_back():
        root.destroy()
        if parent:
            parent.deiconify()

    file_path = tk.StringVar()
    display_file_path = tk.StringVar()
    target_format = tk.StringVar(root)
    target_format.set("mp3")

    def browse_video(event):
        video_file = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav;*.ogg;*.flac;*.m4a;*.aac;*.wma;*.opus")])
        if video_file:
            max_length = 45
            display_file = video_file
            if len(video_file) > max_length:
                display_file = video_file[:max_length - 3] + "..."
            else:
                display_file = video_file
            display_file_path.set(display_file)
            file_path.set(video_file)

    from pydub import AudioSegment

    def convert_video(event):
        input_file = file_path.get()
        if not input_file:
            return

        output_format = target_format.get()
        output_file = filedialog.asksaveasfilename(defaultextension=output_format,
                                                   filetypes=[(f"{output_format.upper()} files", f"*.{output_format}")])

        if not output_file:
            return

        try:
            audio = AudioFileClip(input_file)
            if audio is not None:
                if output_format in supported_formats:
                    audio_codec = None
                    if output_format == "mp3":
                        audio_codec = "libmp3lame"
                    elif output_format == "wav":
                        audio_codec = "pcm_s16le"
                    elif output_format == "ogg":
                        audio_codec = "libvorbis"
                    elif output_format == "flac":
                        audio_codec = "flac"
                    elif output_format == "m4a":
                        audio_codec = "aac"
                    elif output_format == "aac":
                        audio_codec = "aac"
                    elif output_format == "opus":
                        audio_codec = "libopus"

                    if output_format == "wma":
                        audio.write_audiofile("temp.wav", codec=audio_codec)
                        audio_segment = AudioSegment.from_wav("temp.wav")
                        audio_segment.export(output_file, format="wma")
                    else:
                        audio.write_audiofile(output_file, codec=audio_codec)

                    messagebox.showinfo("Conversion Finished", "Audio conversion was successful!")
                else:
                    print("Unsupported format.")
            else:
                print("Error: The audio file could not be loaded.")

        except Exception as e:
            print(f"Error converting audio: {e}")

    # Replace "video" with "audio" in labels
    lbl_convert_video = tk.Label(root, text="Select an audio file:", bg="#A0A0A0", fg="white", font=large_font,
                                 anchor="center")
    lbl_convert_video.pack(fill=tk.X, padx=10, pady=(20, 5))

    lbl_back = tk.Label(root, text="←", bg="#A0A0A0", fg="white", font=large_font, anchor="center")
    lbl_back.pack(fill=tk.X, padx=10, pady=(10, 0))
    lbl_back.bind("<Button-1>", lambda e: go_back())

    lbl_browse_video = tk.Label(root, text="Browse", bg="#A0A0A0", fg="white", font=large_font, anchor="center")
    lbl_browse_video.pack(fill=tk.X, padx=10, pady=10)
    lbl_browse_video.bind("<Button-1>", browse_video)

    lbl_file_path = tk.Label(root, textvariable=display_file_path, bg="#A0A0A0", fg="white", font=("Arial", 12),
                             width=30,
                             anchor="center")
    lbl_file_path.pack(fill=tk.X, padx=10, pady=10)

    supported_formats = ["mp3", "wav", "ogg", "flac", "m4a", "aac", "wma", "opus"]

    lbl_conversion_types = tk.Label(root, text="Supported conversions:", bg="#A0A0A0", fg="white", font=("Arial", 12),
                                    anchor="center")
    lbl_conversion_types.pack(fill=tk.X, padx=10, pady=20)

    supported_formats_frame = tk.Frame(root, bg="#A0A0A0")
    supported_formats_frame.pack(fill=tk.X, padx=25, pady=10)

    column_width = 60
    formats_per_row = 4
    total_width = column_width * formats_per_row
    remaining_space = window_width - total_width
    left_padding = remaining_space // 2

    for i, fmt in enumerate(supported_formats):
        row = i // formats_per_row
        col = i % formats_per_row
        supported_formats_label = tk.Label(supported_formats_frame, text=f"{fmt.upper()}",
                                           bg="#A0A0A0", fg="white", font=("Arial", 12), cursor="hand2",
                                           wraplength=column_width)
        padx = (left_padding, 2) if col == 0 else (2, 2)
        supported_formats_label.grid(row=row, column=col, padx=padx)
        supported_formats_label.bind("<Button-1>", lambda event, fmt=fmt: target_format.set(fmt))

    lbl_convert = tk.Label(root, text="Convert", bg="#A0A0A0", fg="white", font=large_font, anchor="center")
    lbl_convert.pack(fill=tk.X, padx=10, pady=10)
    lbl_convert.bind("<Button-1>", convert_video)

    root.mainloop()


if __name__ == "__main__":
    main()
