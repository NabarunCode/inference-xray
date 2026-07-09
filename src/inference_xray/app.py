import gradio as gr
import datetime

def greet(name: str):
    """Return the greeting message"""
    
    print(
        f"[{datetime.datetime.now().strftime('%H:%M:%S')}] greet() called with: {name}"
    )
    
    return f"Hello {name} ! Welcome to Inference X-Ray !"

import inspect

print("=" * 60)
print("Exploring the greet function")
print("=" * 60)

print(f"Object           : {greet}")
print(f"Type             : {type(greet)}")
print(f"Name             : {greet.__name__}")
print(f"Module           : {greet.__module__}")
print(f"Docstring        : {greet.__doc__}")
print(f"Annotations      : {greet.__annotations__}")
print(f"Signature        : {inspect.signature(greet)}")

print("=" * 60)

demo = gr.Interface (
        fn = greet,
        inputs = gr.Textbox (
                    label = "Your name ",
                    placeholder = "Enter your name " ),
        outputs = gr.Textbox (
                    label = "Greeting" ),
        title = "Inference X-Ray",
        description = "Our first Gradio application",  
        flagging_mode = "never",
        )

if __name__ == "__main__":
    demo.launch()
