class BaseDemodulator:
    def process_frame(self, frame):
        return {"stage1_output": frame}
