from flask import render_template

from models.scan_model import ScanModel

from services.vulnerability_service import (
    VulnerabilityService
)

from services.remediation_service import (
    RemediationService
)


def remediation_page():

    scans = ScanModel.get_all_scans()

    remediation_findings = []

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

            remediation_plan = (
                RemediationService
                .generate_remediation_plan(
                    vuln["service"],
                    vuln["risk"],
                    vuln["description"]
                )
            )

            remediation_findings.append(
                {
                    "port": vuln["port"],
                    "service": vuln["service"],
                    "risk": vuln["risk"],
                    "description": vuln["description"],
                    "recommendation": vuln["recommendation"],
                    "remediation_plan": remediation_plan
                }
            )

    return render_template(
        "remediation.html",
        findings=remediation_findings
    )