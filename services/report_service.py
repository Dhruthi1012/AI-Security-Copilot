import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class ReportService:

    @staticmethod
    def generate_pdf_report(
        findings
    ):

        output_folder = (
            "reports/generated"
        )

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        pdf_path = (
            f"{output_folder}/security_report.pdf"
        )

        document = (
            SimpleDocTemplate(
                pdf_path
            )
        )

        styles = (
            getSampleStyleSheet()
        )

        content = []

        content.append(
            Paragraph(
                "AI Security Copilot Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        for finding in findings:

            content.append(
                Paragraph(
                    f"Service: "
                    f"{finding['service']}",
                    styles["Heading2"]
                )
            )

            content.append(
                Paragraph(
                    f"Port: "
                    f"{finding['port']}",
                    styles["BodyText"]
                )
            )

            content.append(
                Paragraph(
                    f"Risk: "
                    f"{finding.get('risk','unkown')}",
                    styles["BodyText"]
                )
            )

            content.append(
                Paragraph(
                    f"Description: "
                    f"{finding.get('description','No description available')}",
                    styles["BodyText"]
                )
            )

            content.append(
                Paragraph(
                    f"Recommendation: "
                    f"{finding.get('recommendation', 'No recommendation available')}",
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 15)
            )

        document.build(
            content
        )

        return pdf_path