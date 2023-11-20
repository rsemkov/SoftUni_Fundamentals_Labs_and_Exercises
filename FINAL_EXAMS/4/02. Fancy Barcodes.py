import re
pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"
barcodes_count = int(input())
for _ in range(barcodes_count):
    current_barcode = input()
    matches = re.findall(pattern, current_barcode)
    if matches:
        match = matches[0]
        product_group = ""
        for item in match:
            if item.isdigit():
                product_group += item
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
