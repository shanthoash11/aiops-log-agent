class Detector:

    def __init__(self):
        self.values = []

    def check(self, number):

        self.values.append(number)

        # wait until we have enough data
        if len(self.values) < 10:
            return False

        last_values = self.values[-10:]

        mean = sum(last_values) / len(last_values)

        variance = 0
        for v in last_values:
            variance += (v - mean) ** 2

        variance = variance / len(last_values)
        std = variance ** 0.5

        if std == 0:
            std = 1

        z = (number - mean) / std

        if z > 3:
            return True
        else:
            return False