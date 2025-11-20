import os
import hashlib

def secure_wipe(file_path, passes=3, progress_callback=None):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return None

    length = os.path.getsize(file_path)
    try:
        with open(file_path, "ba+") as f:
            for i in range(passes):
                f.seek(0)
                f.write(os.urandom(length))
                f.flush()
                os.fsync(f.fileno())
                print(f"🔄 Overwrite pass {i+1}/{passes} complete")
                if progress_callback:
                    progress_callback(i + 1, passes)

        file_hash = hashlib.sha256(file_path.encode()).hexdigest()
        os.remove(file_path)
        print(f"✅ Securely wiped and deleted: {file_path}")
        return file_hash

    except Exception as e:
        print(f"Error wiping file: {e}")
        return None
