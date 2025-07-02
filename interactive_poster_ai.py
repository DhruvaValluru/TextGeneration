#cd TextGeneration
#source poster-env/bin/activate
#python interactive_poster_ai.py

import cohere
import os

co = cohere.Client("ehLLrmB6T1PgQsHLtpVfPRQd8vNRTagGHJf0EGqX")  # Replace with your real API key

system_prompt = (
    "You are a generative design assistant. The user wants a science-fair-style trifold board layout, not a folded brochure. "
    "The output should reflect a three-panel presentation board viewed from the front, each panel 8.5 x 11 inches, standing vertically, side by side from left to right.\n\n"

    "**LAYOUT OVERVIEW**\n"
    "- Panel Count: 3 panels total (Left, Center, Right)\n"
    "- Orientation: Landscape view of three vertical panels placed side-by-side (not stacked or folded)\n"
    "- Dimensions: Each panel is exactly 8.5 inches wide by 11 inches tall\n"
    "- Margin: 1 inch padding on all sides of each panel\n"
    "- Panel Order: From left to right = Left Panel → Center Panel → Right Panel\n"
    "- Use consistent grid spacing (3-column layout) with symmetrical spacing between text and images.\n\n"

    "**PANEL STRUCTURE**\n"
    "For each of the 3 panels, provide the following in detail using HTML:\n"
    "- Panel Label: (Left Panel / Center Panel / Right Panel)\n"
    "- Title and Subtitle: Use <h1> and <h2> tags\n"
    "- Body Content: Use <p> tags with inline styles\n"
    "- Image Suggestion: Use <!-- comments --> to describe image placement\n"
    "- Font Styles: Apply inline styles like font-family and font-size\n"
    "- Colors: Apply styles for background, text, and highlights\n"
    "- Alignment and layout: Use <div class=\"panel left\"> etc.\n\n"

    "**DESIGN SPEC SHEET (AFTER PANELS)**\n"
    "Include the full design specification using proper HTML structure with clear classes and inline styles:\n"
    "- Font Guide\n"
    "- Color Palette\n"
    "- Grid Layout\n"
    "- Image Placement Rules\n"
    "- Poster Size\n"
    "- Visual Style Keywords\n\n"

    "**OUTPUT FORMAT**\n"
    "Format the output in valid HTML using <div>, <h1>, <h2>, <p>, <span>, and inline CSS styles. "
    "Wrap each panel in a <div class='panel left'>, <div class='panel center'>, or <div class='panel right'>. "
    "Use inline styles for font-family, font-size, color, text-align, background-color, and spacing. "
    "Use <!-- comments --> for image suggestions. Do NOT use Markdown or bullets.\n\n"
    "Output must be full, render-ready HTML for direct use in a poster designer."
)
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html

# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html
# SATVIK us the prompt belo for text  output instead of html

"""
system_prompt = (
    "You are a generative design assistant. The user wants a science-fair-style trifold board layout, not a folded brochure. "
    "The output should reflect a three-panel presentation board viewed from the front, each panel 8.5 x 11 inches, standing vertically, side by side from left to right.\n\n"
    "**LAYOUT OVERVIEW**\n"
    "- Panel Count: 3 panels total (Left, Center, Right)\n"
    "- Orientation: Landscape view of three vertical panels placed side-by-side (not stacked or folded)\n"
    "- Dimensions: Each panel is exactly 8.5 inches wide by 11 inches tall\n"
    "- Margin: 1 inch padding on all sides of each panel\n"
    "- Panel Order: From left to right = Left Panel → Center Panel → Right Panel\n"
    "- Use consistent grid spacing (3-column layout) with symmetrical spacing between text and images.\n\n"
    "**PANEL STRUCTURE**\n"
    "For each of the 3 panels, provide the following in detail:\n"
    "- Panel Label\n"
    "- Title\n"
    "- Subtitle (optional)\n"
    "- Body Content\n"
    "- Image Suggestion\n"
    "- Font Styles\n"
    "- Colors\n"
    "- Alignment\n"
    "- Visual Balance\n\n"
    "**DESIGN SPEC SHEET (After panels)**\n"
    "- Font Guide\n"
    "- Color Palette\n"
    "- Grid Layout\n"
    "- Image Placement Rules\n"
    "- Poster Size\n"
    "- Visual Style Keywords\n\n"
    "**OUTPUT FORMAT**\n"
    "Format in structured Markdown. DO NOT describe this as a brochure.\n"
)

# Load user input
with open("user_input.txt", "r") as file:
    user_text = file.read().strip()

print("📄 Starting poster draft from user_input.txt...\n")

response = co.chat(
    model="command-r-plus",
    message=user_text,
    temperature=0.6,
    prompt_truncation="auto",
    connectors=[],
    chat_history=[{"role": "SYSTEM", "message": system_prompt}],
)

output_text = response.text
print(output_text)





"""
# Load user input from file
with open("user_input.txt", "r") as file:
    user_text = file.read().strip()

print("📄 Starting poster draft from user_input.txt...\n")

response = co.chat(
    model="command-r-plus",
    message=user_text,
    temperature=0.6,
    prompt_truncation="auto",
    connectors=[],
    chat_history=[{"role": "SYSTEM", "message": system_prompt}],
)

output_text = response.text
print(output_text)

# ✅ Write to the React render folder
# ✅ Correct path to your real folder
output_path = os.path.abspath("/Users/dvalluru/Downloads/image-generation-v2-main/generated_spec.txt")

# ✅ Ensure folder exists (in case you move or re-clone it later)
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as f:
    f.write(output_text)

print(f"\n✅ HTML spec written to: {output_path}")
