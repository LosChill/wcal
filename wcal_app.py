import pandas
import datetime
import core
from textual.app import App
from textual.widgets import Button, Footer, Header

today = datetime.date.today()
current_year = today.year

df = core.create_year_df(current_year)

class Wcal(App):
    BINDINGS = [
        ("d", "toggle_light_mode", "Toggle light mode"),
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    def on_mount(self):
        self.sub_title = f"{current_year}"

    def action_toggle_light_mode(self):
        self.dark = not self.dark

if __name__ == "__main__":
    Wcal().run()
