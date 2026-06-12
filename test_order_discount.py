from order_discount import calculate_final_price, format_receipt


def test_calculate_final_price_for_vip_customer():
    assert calculate_final_price(100.0, 20, "vip") == 80.0


def test_calculate_final_price_caps_vip_discount():
    assert calculate_final_price(100.0, 90, "vip") == 20.0


def test_format_receipt():
    assert format_receipt("cust-123", 80.0) == "Customer cust-123 paid 80.0"


def test_apply_coupon_percent_code():
    from order_discount import apply_coupon

    assert apply_coupon(100.0, "PERCENT:10", "vip") == 90.0
