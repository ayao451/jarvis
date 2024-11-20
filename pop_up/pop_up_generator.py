import easygui

class PopUpGenerator:
    def generate_regular_box(self, prompt, text):
        easygui.msgbox(text, title=prompt)