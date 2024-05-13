# WP Media Downloader

## Usage Instructions

1. **Export Media from WordPress:**

   - Go to your WordPress site.
   - Navigate to `Settings > Export`.
   - Select the option to export **media only**.

2. **Prepare the XML File:**

   - After exporting, place the XML file (`example.2024-04-30.xml`) inside the directory containing this script.

3. **Install Required Packages:**

   - Ensure you have the `requests` package installed.
   - Run the following command in your terminal:
     ```bash
     pip install requests
     ```

4. **Run the Downloader:**

   - Execute the script by running:
     ```bash
     python download.py
     ```

5. **Download Media:**
   - If the XML file is correctly placed and your internet connection is stable, the media files will be downloaded shortly.

By following these steps, you should be able to download all your media files from the WordPress XML export.
Your internet connection affect the download speed.
