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

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("HF_space",)
    FUNCTION = "call"
    CATEGORY = "CustomNodesTemplate"

    def call(
        self,
        HF_space: str,
        prompt: str,
        seed: int,
        width: int,
        height: int,
        guidance_scale: float,
        steps: int,
    ) -> str:
        return HF_space
