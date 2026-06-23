from flask import Flask
from database.db import initialize_database

from controllers.target_controller import (
    target_page,
    delete_target
)

from controllers.scan_controller import (
    scan_page
)

from controllers.vulnerability_controller import (
    vulnerability_page
)

from controllers.ai_controller import (
    ai_analysis_page
)

app = Flask(__name__)

initialize_database()


@app.route("/")
def home():

    return """
    <!DOCTYPE html>
    <html>

    <head>

        <title>AI Security Copilot</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
              rel="stylesheet">

    </head>

    <body>

        <div class="container mt-5">

            <h1>AI Security Copilot</h1>

            <hr>

            <div class="list-group">

                <a href="/targets"
                   class="list-group-item list-group-item-action">

                    Target Management

                </a>

                <a href="/scans"
                   class="list-group-item list-group-item-action">

                    Nmap Scan Engine

                </a>

                <a href="/vulnerabilities"
                   class="list-group-item list-group-item-action">

                    Vulnerability Dashboard

                </a>

                <a href="/ai-analysis"
                   class="list-group-item list-group-item-action">

                    AI Security Analysis

                </a>

            </div>

        </div>

    </body>

    </html>
    """


@app.route(
    "/targets",
    methods=["GET", "POST"]
)
def targets():

    return target_page()


@app.route(
    "/delete-target/<int:target_id>"
)
def remove_target(target_id):

    return delete_target(target_id)


@app.route(
    "/scans",
    methods=["GET", "POST"]
)
def scans():

    return scan_page()


@app.route("/vulnerabilities")
def vulnerabilities():

    return vulnerability_page()


@app.route("/ai-analysis")
def ai_analysis():

    return ai_analysis_page()


if __name__ == "__main__":

    app.run(
        debug=True
    )