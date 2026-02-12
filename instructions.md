# What is the Marketplace Builder Skill?

The Marketplace Builder is an "Instruction-to-Site" tool. It creates a full stack Marketplace website. It doesn't just create a basic webpage; it generates a fully functional business store-front with backend support, including features like product listings, and order management

- Customized Setup: Tailored to the provided site name, description, and business ID for seamless integration with existing business systems.

- Backend Support: Includes database setup, API endpoints for inventory management, and secure authentication for users.

- Online: Deployable as a live e-commerce site accessible via a unique URL.

## How to Prompt

To get an effective result, don't just provide minimal details. Use the CORE framework to provide the model with enough context:

- Content:
  - Description: The main focus or theme of the marketplace.
  - Example: "An online store for handmade artisanal crafts."

- Objective:
  - Description: The business goals, target audience, or key features.
  - Example: "Targeted at eco-conscious consumers, with emphasis on sustainable products and easy checkout."

- Essentials:
  - Description: Core inputs like site name and business ID.
  - Example: "Site name: 'EcoCrafts Hub'. Business ID: 'BUS-456789'."

---

### Detailed Prompting Instructions

1.  Be Explicit About Site Description
    Provide a detailed description to guide the site's structure and features. Include elements like product categories, user roles, or custom functionalities.

        - Good: "Description: A marketplace for digital art downloads, including categories for illustrations, photos, and vectors. Support for artist profiles and royalty tracking."

        - Bad: "Just make a store."

2.  Define Business Integration
    Specify how the site ties into the business ID for integration and customization.

        - Instruction: "Link to business ID 'ABC123' for site customization."


3.  Choose a Theme (Required)
    You MUST specify one of the following 4 hardcoded themes. Do not use any other theme names:

    | Theme ID | Name              | Default Color Scheme Array        | Description                     |
    | :--- | :--- | :--- | :--- |
    | `modern`   | Modern Minimalist | `["#000000", "#ffffff", "#f4f4f5"]` | Clean lines, high contrast.     |
    | `elegant`  | Elegant Luxury    | `["#1a1a1a", "#fdfcf9", "#e5e7eb"]` | Soft tones, premium feel.       |
    | `techy`    | Tech & Futuristic | `["#0f172a", "#3b82f6", "#1e293b"]` | Dark mode, vibrant accents.     |
    | `playful`  | Playful & Vibrant | `["#f43f5e", "#fef2f2", "#fb7185"]` | Bright colors, friendly energy. |

    **Important:** You must pick EXACTLY one from the "Theme ID" column above.

    **Note:** The `colorScheme` must be a stringified JSON array of hex colors.

---

#### Example Prompts

For E-commerce Store-Fronts:

- "Create a marketplace with title 'Gadget Galaxy'. Description: An online store specializing in tech gadgets. Use the 'techy' theme. Business ID: 'TECH-789012'."


## API Specification

```json
{
    "title":"Marketplace Builder",
    "description":"Create a functional business store-front with backend support based on provided details.",
    "paths":{
        "/create_marketplace/":{
            "description":"Generate a marketplace site based on title, description, and business ID.",
            "post":{
                "requestBody":{
                    "site_name":{
                        "type":"string",
                        "description":"The name or title of the marketplace site.",
                        "required":true
                    },
                    "site_description":{
                        "type":"string",
                        "description":"A detailed description of the marketplace, on how exactly the ideal website should look like",
                        "required":true
                    },
                    "theme":{
                        "type":"string",
                        "description":"The theme of the store (modern, elegant, techy, playful). Pick exactly one.",
                        "required":true
                    },
                    "colorScheme":{
                        "type":"string",
                        "description":"Stringified JSON array of hex colors corresponding to the theme.",
                        "required":true
                    },
                    "business_id":{
                        "type":"string",
                        "description":"The unique business identifier for integration and customization.",
                        "required":true
                    }
                }
            }
        }
    }
}
```

