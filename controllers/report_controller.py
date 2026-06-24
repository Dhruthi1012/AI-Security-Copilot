from flask import (
    render_template,
    send_file
)

from models.scan_model import ScanModel

from services.vulnerability_service import (
    VulnerabilityService
)

from services.report_service import (
    ReportService
)


def report_page():

    scans = ScanModel.get_all_scans()

    findings = []

    pdf_path = None

    if scans:

        latest_scan = scans[0]

        scan_id = latest_scan["id"]

        scan_results = (
            ScanModel.get_scan_results(
                scan_id
            )
        )

        findings = (
            VulnerabilityService
            .analyze_scan_results(
                scan_results
            )
        )

        print("\nFINDINGS:")
        print(findings)
        print()

        pdf_path = (
            ReportService
            .generate_pdf_report(
                findings
            )
        )

    return render_template(
        "reports.html",
        findings=findings,
        pdf_path=pdf_path
    )


def download_report():

    pdf_path = (
        "reports/generated/"
        "security_report.pdf"
    )

    return send_file(
        pdf_path,
        as_attachment=True
    )