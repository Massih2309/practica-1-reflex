import reflex as rx

# Estilo minimalista extremo para PCs lentas
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Mi Landing Page", size="8", color="blue"),
            rx.text("Desarrollado con Reflex para la Actividad 5.", font_size="1.2em"),
            rx.divider(),
            rx.text("Este es un diseño simplificado para optimizar el rendimiento."),
            rx.button(
                "Ver Repositorio", 
                on_click=rx.redirect("https://github.com/"), # Pon tu link luego
                color_scheme="blue"
            ),
            spacing="5",
            padding="2em",
            border="1px solid #ccc",
            border_radius="10px",
            align="center",
        ),
        width="100%",
        height="100vh",
        background_color="#f4f4f4", # Color sólido, nada de gradientes
    )

app = rx.App()
app.add_page(index)