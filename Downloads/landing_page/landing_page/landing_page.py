import reflex as rx

def index() -> rx.Component:
    return rx.box(
        # Navbar simplificada
        rx.hstack(
            rx.heading("Reflex App", size="6", color="white"),
            rx.spacer(),
            rx.button("Get Started", variant="outline", color_scheme="whiteAlpha"),
            width="100%", padding="1.5em", bg="#9333ea"
        ),
        
        # Hero Section (Inspirado en el Drone de la imagen)
        rx.vstack(
            rx.heading("DRONE? YOU NEED A REFLEX X.", size="9", color="white"),
            rx.text(
                "La mejor tecnología de vuelo controlada 100% con Python.",
                color="whiteAlpha.800", font_size="1.2em"
            ),
            rx.image(
                src="https://reflex.dev/reflex_logo.png", # Usa una imagen liviana
                width="300px",
                margin_y="2em"
            ),
            rx.button("Buy Now", size="4", color_scheme="purple", px="10"),
            padding_y="5em",
            align="center",
            bg="linear-gradient(180deg, #9333ea 0%, #6366f1 100%)",
        ),
        
        # Sección de Características (Cards simples)
        rx.container(
            rx.grid(
                rx.vstack(rx.icon(tag="camera"), rx.text("4K Camera"), padding="2em", border="1px solid #eee"),
                rx.vstack(rx.icon(tag="battery"), rx.text("Long Battery"), padding="2em", border="1px solid #eee"),
                columns=[1, 2],
                spacing="4",
                padding_y="4em"
            ),
            size="3"
        ),
        min_height="100vh",
        bg="white"
    )

app = rx.App()
app.add_page(index)