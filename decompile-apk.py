import os
import subprocess
import sys

def decompile_apk(apk_path):
    # Check if the APK file exists
    if not os.path.isfile(apk_path):
        print(f"APK file not found: {apk_path}")
        return

    base_name = os.path.splitext(os.path.basename(apk_path))[0]

    # Step 1: Use apktool to decode APK
    decoded_dir = f"{base_name}_decoded"
    subprocess.run(["apktool", "d", apk_path, "-o", decoded_dir], check=True)

    # Step 2: Use dex2jar to convert .dex to .jar
    dex_files = [f for f in os.listdir(decoded_dir) if f.endswith('.dex')]
    for dex in dex_files:
        dex_path = os.path.join(decoded_dir, dex)
        jar_path = f"{base_name}.jar"
        subprocess.run(["d2j-dex2jar", dex_path, "-o", jar_path], check=True)
    
    # Step 3: Open the .jar file in a Java decompiler (manual step)
    print(f"Decompiled JAR file: {jar_path}")
    print("Please open the above JAR file in a Java decompiler like JD-GUI to view the source code.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decompile_apk.py <path_to_apk>")
        sys.exit(1)

    apk_file_path = sys.argv[1]
    decompile_apk(apk_file_path)
