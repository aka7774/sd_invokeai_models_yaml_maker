import gradio as gr

from modules import script_callbacks, sd_models, shared

from py.make import make_yaml

def make_button_click():
    return make_yaml()

def on_ui_tabs():
    with gr.Blocks() as invokeai_interface:
        with gr.Row(equal_height=True):
            with gr.Column():
                make_button = gr.Button(value='Make')
                gr.HTML("Copy and paste your InvokeAI/configs/models.yaml")
                models_yaml = gr.Textbox(lines=30,label="models.yaml")

        make_button.click(
            fn=make_button_click,
            inputs=[],
            outputs=[models_yaml]
        )

    return (invokeai_interface, "InvokeAI", "invokeai_interface"),


script_callbacks.on_ui_tabs(on_ui_tabs)
