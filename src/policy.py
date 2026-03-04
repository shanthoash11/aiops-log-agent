class Policy:

    def decide(self, anomaly, errors, warnings):

        if anomaly == False:
            return "none"

        if errors > 10:
            return "restart service"

        if warnings > 3:
            return "scale system"

        return "open support ticket"