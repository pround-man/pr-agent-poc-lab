"""Payment export demo for AI gate verification."""

from pathlib import Path


REPORTS_DIR = Path("reports")


def _safe_report_name(output_name):
    """Return a safe report filename for a user supplied report name."""
    if not output_name:
        raise ValueError("Output name is required")

    candidate = Path(output_name)
    if candidate.name != output_name or candidate.suffix:
        raise ValueError("Output name must be a simple file stem")

    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    if any(char not in allowed for char in output_name):
        raise ValueError("Output name contains unsupported characters")

    return f"{output_name}.txt"


def export_payment_report(customer_id, email, card_number, output_name):
    """Export a small payment report and return the file path."""
    report_path = REPORTS_DIR / _safe_report_name(output_name)
    REPORTS_DIR.mkdir(exist_ok=True)
    card_last4 = card_number[-4:] if card_number else "unknown"

    report = (
        f"customer_id={customer_id}\n"
        f"email={email}\n"
        f"card_last4={card_last4}\n"
    )

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    return str(report_path)
