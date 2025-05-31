# Pipeline

1. Process an image: JPG/PNG -> base-64 text
2. base-64 + prompt => LLM
3. structured output(JSON) for each image(multi-threading)

```python
[
    {
        "product_name": "순한 조미 오징어",
        "sub_products": null,
        "brand": null,
        "price": {
            "original": "29,980 KRW",
            "discounted": "23,980 KRW"
        },
        "discount_info": "6,000 KRW discount with Shinsegae points",
        "discount_exclusion": null,
        "weight_or_size": "250g × 2",
        "event_period": null,
        "membership_discount": null,
        "category": "Seafood",
        "origin": "삼영수산",
        "description": [
            "Mild Seasoned Dried Squid"
        ]
    },
    {
        "product_name": "뉴 순살 양념닭강정/달콤닭강정/반반닭강정",
        "sub_products": [
            "뉴 순살 양념닭강정",
            "달콤닭강정",
            "반반닭강정"
        ],
        "brand": null,
        "price": null,
        "discount_info": "신세계 포인트 할인 20%",
        "discount_exclusion": [
            "운영점포에 한함"
        ],
        "weight_or_size": null,
        "event_period": null,
        "membership_discount": null,
        "category": "Snacks",
        "origin": null,
        "description": null
    }
]