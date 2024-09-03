![Application image - main page]()

# APPLICATION UPDATING WEB DATA
## Objective
Support users in publishing data on different web platforms (WordPress, YouTube, Instagram, Pinterest) using API's and ChatGPT.

## Key results
1. Prepare prompts for YouTube, Instagram, and Pinterest based on templates (users must copy-paste prompts to ChatGPT because using API needs an extra fee so it is not included in this project).
2. Generate WordPress code which can be copy-paste to the WordPress application
3. Create an API to automatically publish posts on WordPress.
4. Create APIs to automatically publish videos/reels with descriptions and settings on three social platforms: YouTube, Instagram, and Pinterest.
5. Example templates for prompts generator and WordPress code
6. Before every run automatic backup preparation in the indicated location

Main functionalities for web platforms:
| WordPress | YouTube | Instagram | Pinterest |
| ----------- | ----------- | ----------- | ----------- |
| publishing new posts via API | publishing new video via API | publishing new reels via API | publishing new post via API |
| create copy-paste code for post based on templates | setup app video settings | setup reels settings | setup post settings |
| ability to copy the entire code or its fragments from the UI level or separate text files | input description prepared by ChatGPT | input description prepared by ChatGPT | input description prepared by ChatGPT |
| | prompt for ChatGPT | prompt for ChatGPT | prompt for ChatGPT | 

## Content
- [App examples](./README.md#app-examples)
- [How to run the app?](./README.md#how-to-run-the-app)
  - [Environment](./README.md#environment)
  - [Used technologies](./README.md#used-technologies)
  - [Database and data](./README.md#database-and-data)
  - [Run the app](./README.md#run-the-app)
- [Testing](./README.md#testing)
- [Documentation](./README.md#documentation)
- [License](./README.md#license)

## App examples

1. Input data for the application are stored in an Excel file (the application converts data from an Excel file for temporary data tables on which you can later invoke SQL commands)
2. Every web application's data contains example templates that include specific strings of characters to replace data from the database (example: '_EXAPLE_STRINGS_TOREPLACE'). Example templates are located in the folder: ..\prepare_data\templates
3. Prepared data are saved in the output file and visible to the user in the main application window. The main output file is located in the folder: ..\prepare_data\output. Smaller pieces of code generated when preparing the final output file are located in the folder: ..\prepare_data\templates
4. Prepared data for WordPress could be used to create new posts via API or copy-paste manually
5. Descriptions and titles for social media are managed in different parts of applications. Users can also set basic settings in the configuration file

## How to run the app?
### Environment
- Windows 11 (the application has not been tested on any other environment)

### Used technologies
- Visual Studio Code
- Python
- JSON
- Excel
- Txt files

### Run the app
Download files from GitHub
```
git clone https://github.com/FooodMoood/python-app_updating_web_data.git
```

The application is launched from the app.py file.
The application is prepared to run locally on a private computer.
To use the API on specific platforms, you must configure access to each and provide appropriate credentials in the configuration files.
Each API script contains a short description of the configuration of access to individual platforms.

## Note
-

## License
[MIT license](https://opensource.org/licenses/MIT)
