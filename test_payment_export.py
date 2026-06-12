from pathlib import Path

from payment_export import export_payment_report


def test_export_payment_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    path = export_payment_report(
        customer_id="cust-001",
        email="user@example.com",
        card_number="4111111111111111",
        output_name="daily",
    )

    assert path == "reports/daily.txt"
    assert Path(path).exists()
