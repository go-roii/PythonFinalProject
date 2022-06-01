import tkinter as tk

class DashboardCard(tk.Frame):
    def __init__(self, container, title, data, accentColor):
        bgColor='#1e1e2e'

        super().__init__(
            container,
            height=150,
            width=350,
            bg=bgColor,
            highlightthickness=2,
            highlightbackground=accentColor,
            padx=24,
            pady=20
        )
        self.pack_propagate(0)

        titleLabel = tk.Label(self, text=title, font='arial 12', bg=bgColor, fg='#c6d0f5')
        titleLabel.pack(anchor='w', expand=1)

        graph = tk.Frame(self, bg=bgColor)
        graph.pack(expand=1, fill=tk.BOTH)

        dataLabel = tk.Label(graph, text=data, font='arial 26 bold', bg=bgColor, fg=accentColor)
        dataLabel.pack(anchor='w')