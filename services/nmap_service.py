import nmap


class NmapService:

    @staticmethod
    def run_scan(target):

        scanner = nmap.PortScanner()

        scanner.scan(
            hosts=target,
            arguments="-sV -Pn"
        )

        results = []

        for host in scanner.all_hosts():

            protocols = scanner[host].all_protocols()

            for protocol in protocols:

                ports = scanner[host][protocol].keys()

                for port in ports:

                    port_data = scanner[host][protocol][port]

                    results.append(
                        {
                            "port": port,
                            "protocol": protocol,
                            "service": port_data.get(
                                "name",
                                "unknown"
                            ),
                            "state": port_data.get(
                                "state",
                                "unknown"
                            )
                        }
                    )

        return results