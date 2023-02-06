from locust import HttpUser, task, events, FastHttpUser


class HelloWorldUser(FastHttpUser):
    @task
    def inference_fish(self):
        self.client.post("/inference",files={'files': test_img})
    
    # @task
    # def inference_sashimi(self):
    #     self.client.post("/inference_sashimi",files={'files': test_img})
    
    @events.init.add_listener
    def on_test_start(environment, **kwargs):
        global test_img
        with open("/opt/ml/final-project-level3-cv-13/test/test_img.jpg", mode='rb') as file:
            img = file.read()
        test_img=img
