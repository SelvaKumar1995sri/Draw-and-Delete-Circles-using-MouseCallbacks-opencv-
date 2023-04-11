from PIL import Image, ImageTk
import tkinter as tk

#Image 2 is on top of image 1.
IMAGE1_DIR = "images/bg_result.jpg"
IMAGE2_DIR = "images/water.jpg"

#Brush size in pixels.
BRUSH = 20
#Actual size is 2*BRUSH

def create_image(filename, width=0, height=0):
    img = Image.open(filename, mode="r")

    if not width and not height:
        return img
    elif width and height:
        return img.resize((int(width), int(height)), Image.ANTIALIAS)
    else:  #Keep aspect ratio.
        w, h = img.size
        scale = width/float(w) if width else height/float(h)
        return img.resize((int(w*scale), int(h*scale)), Image.ANTIALIAS)


class Home(object):
    def __init__(self, master, screen):
        self.screen = w, h = screen
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.can = tk.Canvas(self.frame, width=w, height=h)
        self.can.pack()

        self.image1 = create_image(IMAGE1_DIR, w, h)
        self.image2 = create_image(IMAGE2_DIR, w, h)        

        self.center = w//2, h//2
        self.photo = False

        self.draw()

        self.master.bind("<Return>", self.reset)
        self.master.bind("<B1-Motion>", self.erase)

    def draw(self):
        if self.photo:
            self.can.delete(self.photo)
            self.label.destroy()

        p = ImageTk.PhotoImage(image=self.image2)
        self.photo = self.can.create_image(self.center, image=p)
        self.label = tk.Label(image=p)
        self.label.image = p
    def reset(self, event):
        self.frame.destroy()
        self.__init__(self.master, self.screen)

    def erase(self, event):
        for x in range(event.x-BRUSH, event.x+BRUSH+1):
            for y in range(event.y-BRUSH, event.y+BRUSH+1):
                try:
                    p = self.image1.getpixel((x, y))
                    self.image2.putpixel((x, y), p)
                except IndexError:
                    pass

        self.draw()



def main(screen=(500, 500)):
    root = tk.Tk()
    root.resizable(0, 0)
    Home(root, screen)
    root.mainloop()


if __name__ == '__main__':
    main()