You are an expert in OCR, layout analysis, and text extraction. Your task is to analyze a high-density E-mart promotional flyer image and extract structured product-level information as accurately and completely as possible.

## Output Schema
Each product in the flyer should be represented as an object with the following fields:
1. **Product Name (product_name):** The exact product name as shown on the flyer.
2. **Brand/Manufacturer (brand):** The brand or manufacturer (if available).
3. **Price (price):** The listed price. If there's a separate sale price, include both the original and discounted price. Otherwise, just return: "X KRW"
4. **Discount/Promotion Information (discount_info):** Any promotion details, such as discount rates, validity periods, or “Buy 1 Get 1 Free”, “30% off”, or “2+1” offers.
5. **Weight or Size (weight_or_size):** The weight or size of the product (in kg, g, ml, L, etc.), if provided.
6. **Event Period (event_period):** The overall promotional period stated on the flyer (if applicable).
7. **Membership Discount (membership_disctount):** Include any price or percentage discounts specifically for members (e.g., “Member Price: 2,200 KRW” or “10% off for members”).
8. **Category (category):** The general category of the product, such as “Beverage”, “Snacks”, “Meat”, “Dairy”, etc., if it can be inferred from the text.

## Guidelines for Extraction
- Use OCR and layout understanding to parse all product blocks in the flyer, even in densely packed areas.
- For each product block:
  - Extract all text and contextual clues to populate the output schema.
  - Use flyer layout (e.g., section titles or grouped items) to infer the category.
- Normalize price format: always return in "#,### KRW" style.
- If a field is missing or unclear, return null for that field.
- The final output should be a JSON array of product objects.
- Ensure no product is skipped. Aim for maximum recall.

## Example Output Format
[
  {
    "product_name": "Korean Beef Prime Ribeye",
    "brand": "E-mart",
    "price": "25,900 KRW",
    "discount_info": "2+1 Promotion",
    "weight_or_size": "600g",
    "event_period": "2025.03.20 ~ 2025.03.26",
    "membership_discount": "Member Price: 2,400 KRW",
    "category": "Dairy"
  },
  {
    "product_name": "Shin Ramyun",
    "brand": "Nongshim",
    "price": {
      "original": "3,500 KRW",
      "discounted": "2,500 KRW"
    },
    "discount_info": "28% Off",
    "weight_or_size": "120g x 5 pack",
    "event_period": null,
    "membership_discount": null,
    "category": "Instant Noodles"
  }
]