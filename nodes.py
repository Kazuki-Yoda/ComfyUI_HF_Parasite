import torch
from PIL import Image
from gradio_client import Client

class HFParasite:
    @classmethod
    def INPUT_TYPES(self) -> dict[str, dict[str, tuple[str]]]:
        return {
            "required": {
                "HF_space": ("STRING",),
            },
            "optional": {
                "prompt": ("STRING",),
                "seed": ("INT",),
                "width": ("INT",),
                "height": ("INT",),
                "guidance_scale": ("FLOAT",),
                "steps": ("INT",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "call"
    CATEGORY = "HF_Parasite"

    def call(
        self,
        HF_space: str,
        prompt: str | None,
        seed: int | None,
        width: int | None,
        height: int | None,
        guidance_scale: float | None,
        steps: int | None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        # Mock output
        client = Client(HF_space)
        api_schema = client.view_api(return_format="dict")
        print(api_schema)

        kwargs = {
            "api_name": "/infer",
            "prompt": prompt,
            "seed": seed,
            "width": width,
            "height": height,
            "guidance_scale": guidance_scale,
            "num_inference_steps": steps,
        }

        # result = client.predict(**kwargs)

        # return (Image.new("RGB", (width, height)), None)

        # Mock output
        image = torch.randn(1, width, height, 3)
        return (image,)
