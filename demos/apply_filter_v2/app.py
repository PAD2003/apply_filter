import pyrootutils
import gradio as gr
from src.ApplyFilter import apply_filter_on_image, apply_filter_on_video

pyrootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

# examples
package_dir = pyrootutils.find_root(search_from=__file__, indicator=".project-root")
example_1_dir = package_dir / "test/data/images/example_1.png"
example_list = [[example_1_dir]]

# for app
title = "Filter app"
description = "Using simple resnet 18 to detect landmarks and then applying filter on faces"
article = "Created at PAD"

# Create the Gradio demo
demo = gr.Interface(fn=apply_filter_on_image, # mapping function from input to output
                    inputs=gr.Image(), # what are the inputs?
                    outputs=gr.Image(type="pil"),
                    examples=example_list, 
                    title=title,
                    description=description,
                    article=article)

# Launch the demo!
demo.launch(debug=False, # print errors locally?
            share=False) # generate a publically shareable URL?