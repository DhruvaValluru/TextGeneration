require('dotenv').config();
const axios = require('axios');

const prompt = "Create a compelling headline and subtext for an AI-powered poster on climate change awareness.";

async function generateText() {
  try {
    const response = await axios.post(
      'https://api.cohere.ai/v1/generate',
      {
        model: 'command-r-plus',
        prompt,
        max_tokens: 150,
        temperature: 0.8,
      },
      {
        headers: {
          Authorization: `Bearer ${process.env.COHERE_API_KEY}`,
          'Content-Type': 'application/json',
        },
      }
    );

    console.log("Generated Text:\n", response.data.generations[0].text.trim());
  } catch (error) {
    console.error("Error generating text:", error.response?.data || error.message);
  }
}

generateText();
