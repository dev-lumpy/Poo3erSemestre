import logging

from frontend.main_gui import SistemaPrincipal

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def main() -> None:
    app = SistemaPrincipal()
    app.mainloop()


if __name__ == "__main__":
    main()
