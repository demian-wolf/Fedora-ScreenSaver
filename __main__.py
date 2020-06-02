#!usr/bin/env python3

import tkinter as tk
import tkinter.messagebox as tk_mbox
import webbrowser
import random


class ScreenSaver(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fedora ScreenSaver")

        for attribute in ("-fullscreen", "-topmost"):
            self.attributes(attribute, True)

        for event in ("<Motion>", "<Key>"):
            self.bind(event, lambda ev: self.destroy())

        self.bind("<F1>", self.about)
        self.bind("<F12>", self.visit_github)

        self.canvas = tk.Canvas(self, bg="#eeeeee", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        self.logo_image = tk.PhotoImage(file="logo.png")
        self.img_half_width, self.img_half_height = self.logo_image.width() // 2, self.logo_image.height() // 2
        self.previous_image_id = 0

        self.update()
        self.canv_width, self.canv_height = self.canvas.winfo_width(), self.canvas.winfo_height()

        self.after(0, self.step)

        self.wait_window()

    def step(self):
        if self.previous_image_id:
            self.canvas.delete(self.previous_image_id)
        x, y = random.randint(self.img_half_width, self.canv_width - self.img_half_width), random.randint(
            self.img_half_height, self.canv_height - self.img_half_height)
        self.previous_image_id = self.canvas.create_image(x, y, image=self.logo_image)

        self.after(2000, self.step)

    def about(self, event=None):
        tk_mbox.showinfo("About...",
                         ("Fedora ScreenSaver\n"
                         "(C) Demian Wolf 2020\n" 
                         "A simple screensaver for Fedora (moving Fedora logo on a gray background).\n"
                         "Thank you for using my program!\n"
                         "Visit my Github: https://github.com/demian-wolf/ (press F12 key)"))

    def visit_github(self, event=None):
        webbrowser.open("https://github.com/demian-wolf/")
        self.destroy()


if __name__ == "__main__":
    ScreenSaver().mainloop()
