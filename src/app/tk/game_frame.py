import tkinter

from src.app.game_matrix import Matrix


class GameFrame(tkinter.Frame):
    SCALE = 20
    MARGIN = 20
    MATRIX_HEIGHT = 20
    MATRIX_WIDTH = 20
    SCREEN_WIDTH = MATRIX_WIDTH * SCALE
    SCREEN_HEIGHT = MATRIX_HEIGHT * SCALE
    OUTLINE_WIDTH = 2
    PERIOD = 250

    def __init__(self):
        super().__init__()
        self.matrix = Matrix.create(20, 20)
        # self.matrix = Matrix.random_fill(self.matrix)
        self.canvas = tkinter.Canvas(self, bg="white", height=self.SCREEN_HEIGHT, width=self.SCREEN_WIDTH)
        self.pause = True
        self.initUI()

    def initUI(self):
        self.master.title("Life Classic")
        self.pack()
        self.draw_field()

    def update_screen(self):
        if not self.pause:
            self.matrix = Matrix.next_epoch(self.matrix)
            self.draw_field()

    def switch_pause(self, event):
        self.pause = not self.pause

    def handle_mouse_click(self, event):
        row = event.y // self.SCALE
        col = event.x // self.SCALE
        cell_val = self.matrix[row][col]
        self.matrix = Matrix.set_cell(self.matrix, row, col, not cell_val)
        self.draw_field()

    def draw_field(self):
        self.canvas.delete("all")
        for i in range(self.MATRIX_HEIGHT):
            for j in range(self.MATRIX_WIDTH):
                color = "black" if self.matrix[i][j] else "white"
                self.canvas.create_rectangle(
                    j * self.SCALE,
                    i * self.SCALE,
                    (j + 1) * self.SCALE,
                    (i + 1) * self.SCALE,
                    fill=color, outline="black",
                    width=self.OUTLINE_WIDTH
                )
        self.canvas.pack()


def tk_main():
    def update():
        gf.update_screen()
        root.after(gf.PERIOD, update)

    root = tkinter.Tk()
    gf = GameFrame()
    root.geometry(f"{gf.SCREEN_WIDTH}x{gf.SCREEN_HEIGHT}+{gf.MARGIN}+{gf.MARGIN}")
    root.bind("<ButtonPress-1>", gf.handle_mouse_click)
    root.bind("<space>", gf.switch_pause)
    root.after(gf.PERIOD, update)
    root.mainloop()
