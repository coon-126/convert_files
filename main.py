import tkinter as tk
import tkinter.font as tkfont
import os


def main():
    root = tk.Tk()
    root.title("Converter Menu")

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

    def open_audio_converter():
        os.system('python convert_audio.py')

    def open_video_converter():
        os.system('python convert_video.py')

    def exit_program():
        root.destroy()

    lbl_convert_menu = tk.Label(root, text="Converter Menu", bg="#A0A0A0", fg="white", font=large_font, anchor="center")
    lbl_convert_menu.pack(fill=tk.X, padx=10, pady=(20, 50))

    lbl_audio_converter = tk.Label(root, text="Audio Converter", bg="#A0A0A0", fg="white", font=large_font, anchor="center", cursor="hand2")
    lbl_audio_converter.pack(fill=tk.X, padx=10, pady=20)
    lbl_audio_converter.bind("<Button-1>", lambda event: open_audio_converter())

    lbl_video_converter = tk.Label(root, text="Video Converter", bg="#A0A0A0", fg="white", font=large_font, anchor="center", cursor="hand2")
    lbl_video_converter.pack(fill=tk.X, padx=10, pady=20)
    lbl_video_converter.bind("<Button-1>", lambda event: open_video_converter())

    lbl_exit = tk.Label(root, text="Exit", bg="#A0A0A0", fg="white", font=large_font, anchor="center", cursor="hand2")
    lbl_exit.pack(fill=tk.X, padx=10, pady=20)
    lbl_exit.bind("<Button-1>", lambda event: exit_program())

    root.mainloop()


if __name__ == "__main__":
    main()
