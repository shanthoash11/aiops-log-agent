class Executor:

    def run(self, action):

        if action == "none":
            print("System running normally")

        elif action == "restart service":
            print("Action taken: Restarting service")

        elif action == "scale system":
            print("Action taken: Scaling system resources")

        elif action == "open support ticket":
            print("Action taken: Opening support ticket")