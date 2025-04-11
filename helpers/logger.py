class Logger:

    @classmethod
    def print(cls, message=""):
        print(f"{message}", flush=True)

    @classmethod
    def log_success(cls, message=""):
        print(f"[OK] {message}", flush=True)
    
    @classmethod
    def log_error(cls, error=""):
        print(f"[!] {error}", flush=True)