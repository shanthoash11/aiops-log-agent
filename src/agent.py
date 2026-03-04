from detector import Detector
from policy import Policy
from executor import Executor

detector = Detector()
policy = Policy()
executor = Executor()

file = open("runs/app.log")

errors = 0
warnings = 0

for line in file:

    if "ERROR" in line:
        errors += 1

    if "WARNING" in line:
        warnings += 1

    score = errors + warnings

    anomaly = detector.check(score)

    action = policy.decide(anomaly, errors, warnings)

    executor.run(action)

file.close()