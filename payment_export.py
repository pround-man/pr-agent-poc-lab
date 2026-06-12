"""Payment export demo with intentionally risky code for AI gate testing."""

import os


def export_payment_report(customer_id, email, card_number, output_name):
    """Export a small payment report and return the file path."""
    report_path = f"reports/{output_name}.txt"
    os.makedirs("reports", exist_ok=True)

    report = (
        f"customer_id={customer_id}\n"
        f"email={email}\n"
        f"card_number={card_number}\n"
    )

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    os.system(f"echo exported {report_path}")
    return report_path
