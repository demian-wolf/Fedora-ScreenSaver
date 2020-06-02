#!usr/bin/env python3

import tkinter as tk
import tkinter.messagebox as tk_mbox
import random


class ScreenSaver(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Fedora Screen Saver")

        for attribute in ("-fullscreen", "-topmost"):
            self.attributes(attribute, True)
            
        for event in ("<Motion>", "<Key>"):
            self.bind(event, lambda ev: self.destroy())
        self.bind("<F1>", lambda ev: tk_mbox.showinfo("Fedora Screen Saver", "(C) Demian Wolf, 2020"))

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
        x, y = random.randint(self.img_half_width, self.canv_width - self.img_half_width), random.randint(self.img_half_height, self.canv_height - self.img_half_height)
        self.previous_image_id = self.canvas.create_image(x, y, image=self.logo_image)

        self.after(2000, self.step)

if __name__ == "__main__":
    tk.Tk().withdraw()
    ScreenSaver()
