from PIL import Image, ImageTk
import tkinter as tk

#Image 2 is on top of image 1.
IMAGE1_DIR = "images/water.jpg"
IMAGE2_DIR = "images/result.PNG"

#Brush size in pixels.
BRUSH = 5
#Actual size is 2*BRUSH

def create_image(filename, width=0, height=0):
    """
    Returns a PIL.Image object from filename - sized
    according to width and height parameters.

    filename: str.
    width: int, desired image width.
    height: int, desired image height.

    1) If neither width nor height is given, image will be returned as is.
    2) If both width and height are given, image will resized accordingly.
    3) If only width or only height is given, image will be scaled so specified
    parameter is satisfied while keeping image's original aspect ratio the same. 
    """
    #Create a PIL image from the file.
    img = Image.open(filename, mode="r")

    #Resize if necessary.
    if not width and not height:
        return img
    elif width and height:
        return img.resize((int(width), int(height)), Image.ANTIALIAS)
    else:  #Keep aspect ratio.
        w, h = img.size
        scale = width/float(w) if width else height/float(h)
        return img.resize((int(w*scale), int(h*scale)), Image.ANTIALIAS)


class Home(object):
    """
    master: tk.Tk window.
    screen: tuple, (width, height).
    """
    def __init__(self, master, screen):
        self.screen = w, h = screen
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.can = tk.Canvas(self.frame, width=w, height=h)
        self.can.pack()

        self.image1 = create_image(IMAGE1_DIR, w, h)
        self.image2 = create_image(IMAGE2_DIR, w, h)        

        #Center of screen.
        self.center = w//2, h//2
        #Start with no photo on the screen.
        self.photo = False

        #Draw photo on screen.
        self.draw()

        #Key bindings.
        self.master.bind("<Return>", self.reset)
        self.master.bind("<B1-Motion>", self.erase)

    def draw(self):
        """
        If there is a photo on the canvas, destroy it.
        Draw self.image2 on the canvas.
        """            
        if self.photo:
            self.can.delete(self.photo)
            self.label.destroy()

        p = ImageTk.PhotoImage(image=self.image2)
        self.photo = self.can.create_image(self.center, image=p)
        self.label = tk.Label(image=p)
        self.label.image = p

    #### Key Bindings ####
    def reset(self, event):
        """ Enter/Return key. """
        self.frame.destroy()
        self.__init__(self.master, self.screen)

    def erase(self, event):
        """
        Mouse motion binding.
        Erase part of top image (self.photo2) at location (event.x, event.y),
        consequently exposing part of the bottom image (self.photo1).
        """        
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

    #Place window in center of screen.
    # root.eval('tk::PlaceWindow %s center'%root.winfo_pathname(root.winfo_id()))

    root.mainloop()


if __name__ == '__main__':
    main()