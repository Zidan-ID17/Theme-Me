import os
import subprocess
import sys

def main():
    theme_me_dir = '../Theme-Me'

    if os.path.exists(theme_me_dir):
        print(f"Menghapus folder lama: {theme_me_dir}")
        os.system(f"rm -rf {theme_me_dir}")

    parent_dir = os.path.dirname(theme_me_dir)
    if not os.path.exists(parent_dir):
        print(f"Membuat direktori induk: {parent_dir}")
        os.makedirs(parent_dir)

    print("Meng-clone repository...")
    result = subprocess.run(['git', 'clone', 'https://github.com/Zidan-ID17/Theme-Me'], 
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Gagal meng-clone repository:")
        print(result.stderr.decode())
        sys.exit(1)

    os.chdir(theme_me_dir)

    print("Update berhasil!")

if __name__ == "__main__":
    main()
