Ethiopian Medical Businesses Data Warehouse
Project OverviewThis project is designed to detect medical tools from images shared in the Chemed Telegram Channel. 
The pipeline consists of five main components:

1.Telegram Scraping: Collects images from Telegram channels.

2.Storing Data in PostgreSQL: Organizes and stores scraped image data in a PostgreSQL database.

3.DBT (Data Build Tool) Transformation: Processes and transforms stored data for efficient querying.

4.Image Detection using YOLO: Identifies and classifies medical tools in images.

5.API Development with FastAPI: Provides an interface to interact with processed data and detection results.
