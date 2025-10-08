from amazon_paapi import AmazonApi
import json

# ==== Amazon Credentials ====
ACCESS_KEY = "YOUR_AMAZON_ACCESS_KEY"
SECRET_KEY = "YOUR_AMAZON_SECRET_KEY"
PARTNER_TAG = "YOUR_PARTNER_TAG"
MARKETPLACE = "IN"   # Example: IN (India), US, UK, etc.

# ==== Initialize API ====
amazon = AmazonApi(ACCESS_KEY, SECRET_KEY, PARTNER_TAG, MARKETPLACE)

# Example product (ASIN code from Amazon product URL)
asin = "B0C5W34XSW"

# Fetch product info
result = amazon.get_items(asin)

if "ItemsResult" in result and "Items" in result["ItemsResult"]:
    item = result["ItemsResult"]["Items"][0]

    # Extract details
    title = item["ItemInfo"]["Title"]["DisplayValue"]
    product_url = item["DetailPageURL"]
    price = item["Offers"]["Listings"][0]["Price"]["DisplayAmount"]
    original_price = item["Offers"]["Listings"][0].get("SavingBasis", {}).get("DisplayAmount", "Not Available")
    image_url = item["Images"]["Primary"]["Large"]["URL"]
    features = item["ItemInfo"]["Features"]["DisplayValues"]

    # Reviews (rating + count, no review text in API)
    review_rating = item["ItemInfo"].get("ProductInfo", {}).get("UnitCount", {}).get("DisplayValue", "N/A")
    review_count = item.get("CustomerReviews", {}).get("Count", "Not Available")

    # Save as dictionary
    product_details = {
        "title": title,
        "price": price,
        "original_price": original_price,
        "features": features,
        "image_url": image_url,
        "product_url": product_url,
        "review_rating": review_rating,
        "review_count": review_count
    }

    print(json.dumps(product_details, indent=4, ensure_ascii=False))

else:
    print("❌ No item found")
