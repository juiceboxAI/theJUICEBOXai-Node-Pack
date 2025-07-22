# File: __init__.py

"""
theJUICEBOXai Node Pack for ComfyUI
"""

# Import the node class from your other file
from .theJUICEBOXai_nodes import LatentPresetsJuicebox

# A dictionary that maps the node's internal class name to the node's class
NODE_CLASS_MAPPINGS = {
    "LatentPresetsJuicebox": LatentPresetsJuicebox
}

# A dictionary that maps the node's display name (what you see in the menu) to its internal class name
NODE_DISPLAY_NAME_MAPPINGS = {
    "LatentPresetsJuicebox": "theJUICEBOXai - Latent Presets"
}

# Optional: A print statement to confirm the pack loaded in the console
print("✅ Loaded: theJUICEBOXai Node Pack")

# This is a required variable for ComfyUI to discover and register the nodes
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']