from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)

pipe = pipe.to("cpu")

prompt = "a beautiful futuristic classroom with AI robots"

image = pipe(prompt).images[0]

image.save("generated_image.png")

print("Image generated successfully!")