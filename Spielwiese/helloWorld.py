
def main():
    pass


class HalloWelt:

    def intro(self):
        print("Hello World!")
        name = input("Sag mir bitte deinen Namen: ")
        # print("Hallo %s, ist heute nicht ein wunderschöner Tag!?" % name)
        print("Hallo " + name + ", ist heute nicht ein wunderschöner Tag!?")


if __name__ == "__main__":
    hw = HalloWelt()
    hw.intro()
