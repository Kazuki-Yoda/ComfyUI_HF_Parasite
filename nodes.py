from PIL import Image


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
    ) -> Image.Image:
        # Mock output
        return Image.new("RGB", (100, 100))
