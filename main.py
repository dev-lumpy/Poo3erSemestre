from frontend.main_gui import SistemaPrincipal


def main() -> None:
    app = SistemaPrincipal()
    app.root.mainloop()


if __name__ == "__main__":
    main()