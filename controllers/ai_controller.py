from flask import render_template

from models.scan_model import ScanModel

from services.vulnerability_service import (
    VulnerabilityService
)

from services.ai_service import (
    AIService
)


def ai_analysis_page():

    scans = ScanModel.get_all_scans()

    ai_findings = []

    if scans:

        latest_scan = scans[0]

        scan_id = latest_scan["id"]

        scan_results = (
            ScanModel.get_scan_results(
                scan_id
            )
        )

        vulnerabilities = (
            VulnerabilityService
            .analyze_scan_results(
                scan_results
            )
        )

        for vuln in vulnerabilities:

            ai_explanation = (
                AIService
                .generate_security_explanation(
                    vuln["service"],
                    vuln["risk"],
                    vuln["description"]
                )
            )

            ai_findings.append(
                {
                    "port": vuln["port"],
                    "service": vuln["service"],
                    "risk": vuln["risk"],
                    "description": vuln["description"],
                    "recommendation": vuln["recommendation"],
                    "ai_explanation": ai_explanation
                }
            )

    return render_template(
        "ai_analysis.html",
        findings=ai_findings
    )