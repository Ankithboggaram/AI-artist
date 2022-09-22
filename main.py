# https://huggingface.co/blog/stable_diffusion used for reference

# Check the authtoken.py file before proceeding 
from authtoken import auth_token
# This variable must contain the huggingface security token received after creating a free account (Necessary to use the Stable Diffusion Pipeline) 
# Refer to for more https://huggingface.co/docs/hub/security-tokens information 

# Importing the necessary libraries
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
import torch
# Emptying the cache
torch.cuda.empty_cache()
from torch import autocast
# The model being used in this project
from diffusers import StableDiffusionPipeline

app = tk.Tk()
app.geometry("532x622")
app.title("AI Artist")

window = ctk.CTkEntry(height = 40, width = 512, text_font = ("Times New Roman", 14), text_color = "black", fg_color = "white")
window.place(x=10, y=10)

output = ctk.CTkLabel(height = 512, width = 512)
output.place(x=10, y=510)

def generate():
    with autocast(device):
        # Set guidance on a scale of 1 to 10 as a measure of how accurate the output should be to the text input
        image = pip(promt.get(), guidance_scale = 8.5)["sample"][0]
    image.save('result.png')
    img = ImageTk.PhotoImage(image)
    image.configure

button = ctk.CTkButton(height = 30, width = 120, text_font = ("Times New Roman", 14), text_color = "white", fg_color = "black")
button.configure(text = "Generate")
button.place(x= 206, y = 60)

# Other models can be used too, check link in the first line of code for more information
model = "CompVis/stable-diffusion-v1-4"
device = "cuda"
# Use "torch_dtype = torch.float16" if you have a GPU smaller than 10 Gb
pipe = StableDiffusionPipeline.from_pretrained(model, revision="fp16", torch_dtype = torch.float16, use_auth_token = auth_token)
pipe.to(device)

app.mainloop()