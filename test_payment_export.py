from pathlib import Path

import pytest

from payment_export import export_payment_report


def test_export_payment_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    path = export_payment_report(
        customer_id="cust-001",
        email="user@example.com",
        card_number="4111111111111111",
        output_name="daily",
    )

    assert Path(path) == Path("reports") / "daily.txt"
    assert Path(path).exists()
    contents = Path(path).read_text(encoding="utf-8")
    assert "card_number=" not in contents
    assert "card_last4=1111" in contents


@pytest.mark.parametrize("output_name", ["../secret", "nested/report", "daily.txt", "daily report"])
def test_export_payment_report_rejects_unsafe_output_names(tmp_path, monkeypatch, output_name):
    monkeypatch.chdir(tmp_path)

    with pytest.raises(ValueError):
        export_payment_report(
            customer_id="cust-001",
            email="user@example.com",
            card_number="4111111111111111",
            output_name=output_name,
        )
