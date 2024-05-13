# WP Media Downloader

## Usage Instructions

1. **Export Media from WordPress:**

   - Go to your WordPress site.
   - Navigate to `Settings > Export`.
   - Select the option to export **media only**.

2. **Prepare the XML File:**

   - After exporting, place the XML file (`mint.WordPress.2024-04-30.xml`) inside the directory containing this script.

3. **Update the Script:**

   - Open the `download.py` file.
   - On line 31, change the file name to match your XML file. For example:
     ```python
     xml_file = 'icanq.WordPress.2024-04-30.xml'
     ```

4. **Install Required Packages:**

   - Ensure you have the `requests` package installed.
   - Run the following command in your terminal:
     ```bash
     pip install requests
     ```

5. **Run the Downloader:**

   - Execute the script by running:
     ```bash
     python download.py
     ```

6. **Download Media:**
   - If the XML file is correctly placed and your internet connection is stable, the media files will be downloaded shortly.

By following these steps, you should be able to download all your media files from the WordPress XML export.
