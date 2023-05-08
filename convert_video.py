import tkinter as tk
import tkinter.font as tkfont
import tkinter.filedialog as filedialog
from moviepy.editor import *
from tkinter import messagebox
from tqdm import tqdm

def main(parent=None):
    root = tk.Tk()
    root.title("Video Converter")

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
    display_file_path = tk.StringVar()  # New StringVar to hold the shortened path
    target_format = tk.StringVar(root)
    target_format.set("mp4")

    def browse_video(event):
        video_file = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.mkv;*.avi;*.flv;*.mov;*.wmv;*.webm;*.mpeg")])
        if video_file:
            max_length = 45
            display_file = video_file
            if len(video_file) > max_length:
                display_file = video_file[:max_length - 3] + "..."
            else:
                display_file = video_file
            display_file_path.set(display_file)  # Update display_file_path
            file_path.set(video_file)  # Store the full path in file_path



    lbl_convert_video = tk.Label(root, text="Select a video file:", bg="#A0A0A0", fg="white", font=large_font,
                                 anchor="center")
    lbl_convert_video.pack(fill=tk.X, padx=10, pady=(20, 5))
    def convert_video(event):
        input_file = file_path.get()
        if not input_file:
            return

        output_format = target_format.get()
        output_file = filedialog.asksaveasfilename(defaultextension=output_format,
                                                   filetypes=[(f"{output_format.upper()} files", f"*.{output_format}")])

        if not output_file:
            return

        codec = None
        if output_format == "mp4":
            codec = "libx264"
        elif output_format == "mkv":
            codec = "libx265"
        elif output_format == "avi":
            codec = "mpeg4"
        elif output_format == "flv":
            codec = "flv"
        elif output_format == "mov":
            codec = "libx264"
        elif output_format == "wmv":
            codec = "wmv2"
        elif output_format == "webm":
            codec = "libvpx"
        elif output_format == "mpeg":
            codec = "mpeg2video"

        try:
            video = VideoFileClip(input_file)
            video.write_videofile(output_file, codec=codec)

            messagebox.showinfo("Conversion Finished", "Video conversion was successful!")  # Display popup window
        except Exception as e:
            print(f"Error converting video: {e}")

    lbl_back = tk.Label(root, text="←", bg="#A0A0A0", fg="white", font=large_font, anchor="center")
    lbl_back.pack(fill=tk.X, padx=10, pady=(10, 0))
    lbl_back.bind("<Button-1>", lambda e: go_back())

    lbl_browse_video = tk.Label(root, text="Browse", bg="#A0A0A0", fg="white", font=large_font, anchor="center")
    lbl_browse_video.pack(fill=tk.X, padx=10, pady=10)
    lbl_browse_video.bind("<Button-1>", browse_video)

    lbl_file_path = tk.Label(root, textvariable=display_file_path, bg="#A0A0A0", fg="white", font=("Arial", 12), width=30,
                             anchor="center")  # Use display_file_path instead of file_path
    lbl_file_path.pack(fill=tk.X, padx=10, pady=10)

    supported_formats = ["mp4", "mkv", "avi", "flv", "mov", "wmv", "webm", "mpeg"]

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
