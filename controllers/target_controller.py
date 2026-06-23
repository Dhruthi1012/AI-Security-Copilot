from flask import (
    render_template,
    request,
    redirect,
    url_for
)

from models.target_model import TargetModel


def target_page():

    if request.method == "POST":

        target_name = request.form["target_name"]

        if "." in target_name:
            target_type = "Domain"
        else:
            target_type = "IP"

        TargetModel.add_target(
            target_name,
            target_type
        )

        return redirect(url_for("targets"))

    targets = TargetModel.get_all_targets()

    return render_template(
        "targets.html",
        targets=targets
    )


def delete_target(target_id):

    TargetModel.delete_target(target_id)

    return redirect(url_for("targets"))