# File: theJUICEBOXai_nodes.py (Version 1)

import torch
import re

class LatentPresetsJuicebox:
    """
    A custom node to generate an empty latent image with a variety of useful presets.
    This node also includes an orientation toggle to switch between Landscape and Portrait.
    Created for theJUICEBOXai Node Pack.
    """

    # --- list of landscape-first and square presets ---
    LANDSCAPE_PRESETS = [
        # --- AI Recommended (Landscape/Square) ---
        "1024x1024 | 1:1 Square",
	"1536x1536 | 1:1 Square Hi",
        "1152x896  | 9:7 Landscape",
        "1280x768  | 5:3 Landscape",
        "1344x768  | 7:4 Widescreen",
        "1536x640  | 12:5 Cinematic",
        # --- Social Media & Web (Landscape/Square Base) ---
        "1080x1080 | Square Post",
        "1200x630  | Facebook, X",
        "1350x1080 | For Instagram 4:5",
        "1920x1080 | For TikTok, Reels 9:16",
	"1200x800  | Blog Post",
        # --- Other Resoltions ---
        "1280x720  | 720p",
        "1280x800  | SteamDeck",
	"1664x768  | iPhone UPs",
    ]

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "preset": (s.LANDSCAPE_PRESETS, ),
                "orientation": (["Landscape", "Portrait"],), # <-- The new toggle
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "generate"
    CATEGORY = "theJUICEBOXai"

    def generate(self, preset, orientation, batch_size=1):
        # Use a regular expression to find the resolution string like '1024x1024'
        match = re.search(r'(\d+)x(\d+)', preset)
        if match:
            # The preset list is landscape-first, so width is group 1, height is group 2
            width = int(match.group(1))
            height = int(match.group(2))
        else:
            # Fallback in case the regex fails
            print(f"theJUICEBOXai Node Warning: Could not parse resolution from '{preset}'. Defaulting to 512x512.")
            width, height = 512, 512

        # Check the orientation toggle and swap width/height if Portrait is selected
        if orientation == "Portrait":
            # This swaps the two values. No need to do anything for square images.
            width, height = height, width

        # Ensure final width and height are multiples of 8 for latent space compatibility
        final_width = (width // 8) * 8
        final_height = (height // 8) * 8

        latent = torch.zeros([batch_size, 4, final_height // 8, final_width // 8])
        return ({"samples": latent}, )