import tkinter as tk
import pyperclip

def generate_flipbook_code(num_images):
    # HTML Code
    html_code = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flipbook Effect</title>
    <link rel="stylesheet" href="style.css">\n"""
    for i in range(0, num_images + 1):
        html_code += f'\t<link rel="preload" as="image" href="Frames/Frame {i}.png">\n'
    html_code += "</head>\n<body>\n\t<div id=\"flipbook-container\">\n"
    for i in range(0, num_images + 1):
        html_code += f'\t\t<div class="flipbook-image" style="background-image: url(\'Frames/Frame {i}.png\');"></div>\n'
    html_code += "\t</div>\n<script src=\"script.js\"></script>\n</body>\n</html>"

    # CSS Code
    css_code = """body, html {
    margin: 0;
    padding: 0;
    height: 1000%;
    overflow-x: hidden;
    background-color: black;
}

#flipbook-container {
    position: relative;
    width: 100%;
    height: 100vh;
}

.flipbook-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    display: none;
}

.flipbook-image.active {
    display: block;
}"""

    # JavaScript Code
    js_code = """document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.flipbook-image');
    const frameChange = 10; // pixels scrolled per frame

    const changeImage = (index) => {
        images.forEach((img, idx) => {
            img.style.display = idx === index ? 'block' : 'none';
        });
    };

    window.addEventListener('scroll', () => {
        const currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop;
        let currentIndex = Math.floor(currentScrollPosition / frameChange);

        if(currentIndex >= images.length) {
            currentIndex = images.length - 1;
        }

        changeImage(currentIndex);
    });

    changeImage(0);
});"""

    return html_code, css_code, js_code

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Copied to clipboard!")

def create_code_window(title, code):
    code_window = tk.Toplevel()
    code_window.title(title)

    text_widget = tk.Text(code_window, height=15, width=60)
    text_widget.insert(tk.END, code)
    text_widget.pack(pady=10)
    text_widget.config(state='disabled')

    copy_button = tk.Button(code_window, text=f"Copy {title.split()[0]}", command=lambda: copy_to_clipboard(code))
    copy_button.pack(pady=10)

def main_app():
    def replace_with_copy_buttons():
        num_images = int(section_entry.get())
        html_code, css_code, js_code = generate_flipbook_code(num_images)

        # Remove/hide the initial widgets
        section_entry.pack_forget()
        generate_button.pack_forget()
        section_label.pack_forget()

        # Open new windows with code and copy buttons
        create_code_window("HTML Code", html_code)
        create_code_window("CSS Code", css_code)
        create_code_window("JavaScript Code", js_code)

    main_window = tk.Tk()
    main_window.title("Image Generator")

    # Set window size (width x height)
    main_window.geometry("500x300")  # You can adjust the size as needed

    # Disable resizing
    main_window.resizable(False, False)

    section_label = tk.Label(main_window, text="Enter Number of Images:")
    section_label.pack(pady=10)

    section_entry = tk.Entry(main_window)
    section_entry.pack(pady=10)

    generate_button = tk.Button(main_window, text="Generate", command=replace_with_copy_buttons)
    generate_button.pack(pady=20)

    main_window.mainloop()

# Run the main application
main_app()