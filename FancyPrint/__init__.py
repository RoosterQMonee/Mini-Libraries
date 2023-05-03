import time
import random


class FancyPrinting:
    def get_wpm_delay(wpm):
        return 1 / wpm


    def typewriter(text, delay):
        full = ""

        for c in text:
            if c == "\n":
                print(full)
                full = ""

                continue
            
            full += c
            
            print(full, end = "_\r")
            time.sleep(delay)


    def autocomplete(text, delay):
        full = ""

        for c in text.split(" "):
            if c == "\n":
                print(full)
                full = ""

                continue
            
            full += c + " "
            
            print(full, end = "\r")
            time.sleep(delay)
            

    def corrections(text, delay):
        full = ""
        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        corrections = [random.randint(0, len(text)) for x in range(random.randint(1, len(text.split(" ")) // 2))]

        for i, c in enumerate(text):
            if c == "\n":
                print(full)
                full = ""

                continue

            if i in corrections:
                print(full + random.choice(chars), end = "\r")
                time.sleep(delay)

                print(full, end = "\r")
                time.sleep(delay / 2)
                
            full += c
            
            print(full, end = "\r")
            time.sleep(delay)


    def encrypted(text, delay):
        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        full = [random.choice(chars) for x in range(len(text))]

        for i, c in enumerate(text):
            full[i] = c
            
            print("".join(full), end = "\r")
            time.sleep(delay)


if __name__ == "__main__":
    FancyPrinting.typewriter("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.""", FancyPrinting.get_wpm_delay(100))
