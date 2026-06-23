from flask import render_template, request

from models.target_model import TargetModel
from models.scan_model import ScanModel
from services.nmap_service import NmapService


def scan_page():

    targets = TargetModel.get_all_targets()

    print("TARGETS FOUND:")
    print(targets)

    scan_results = []

    if request.method == "POST":

        target_id = request.form["target_id"]

        selected_target = None

        for target in targets:

            if str(target["id"]) == str(target_id):
                selected_target = target
                break

        if selected_target:

            target_name = selected_target["target_name"]

            scan_id = ScanModel.create_scan(
                selected_target["id"]
            )

            results = NmapService.run_scan(
                target_name
            )

            for result in results:

                ScanModel.save_scan_result(
                    scan_id,
                    result["port"],
                    result["protocol"],
                    result["service"],
                    result["state"]
                )

            scan_results = ScanModel.get_scan_results(
                scan_id
            )

    return render_template(
        "scans.html",
        targets=targets,
        scan_results=scan_results
    )