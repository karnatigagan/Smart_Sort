
# Smart_Sort
Smart Sort: AI powered Custom File Explorer
=======

# SmartSortAI

SmartSortAI is an AI-powered file organizer that automatically categorizes files, detects the operating system (Mac/Windows), and moves files into designated folders based on predefined rules or AI-driven categorization. It aims to simplify file management by monitoring folders (such as Downloads) and automating the organization process for the user.

# Features

	•	Cross-Platform Support: Automatically detects and adjusts file commands for macOS and Windows.
	•	AI-Powered File Categorization: Sorts files into categories based on file extensions, names, and content.
	•	Customizable Sorting Rules: Users can define custom rules for sorting files into specific folders.
	•	Automatic File Monitoring: Continuously monitors designated folders (e.g., Downloads) for new files and automatically moves them to the appropriate location.
	•	User-Friendly Interface: A planned GUI (Graphical User Interface) will allow users to easily adjust settings, view logs, and manage their files.

Features

	•	Cross-Platform Support: Automatically detects and adjusts file management for macOS and Windows.
	•	Initial Categorization: Files are sorted into predefined categories like Documents, Media, Images, and Others based on their file types.
	•	AI-Powered Categorization: Using GPT-4 and LangChain, SmartSortAI further categorizes files based on their titles and content.
	•	Handles Duplicate Files: Automatically appends a numeric suffix (e.g., _1, _2, _3) to files with the same name to avoid overwriting.
	•	Automatic File Monitoring: Continuously monitors designated folders (e.g., Downloads) for new files and categorizes them in real-time.
	•	User-Friendly Interface: Plans for a graphical user interface (GUI) for adjusting settings, viewing logs, and managing files.

How It Works

Step 1: Initial Categorization

When a new file is detected in the monitored folder (e.g., Downloads), it is categorized based on its file type:

	•	.pdf, .docx, etc. are categorized as Documents.
	•	.mp4, .mp3, etc. are categorized as Media.
	•	.jpg, .png, etc. are categorized as Images.
	•	All other files are categorized under Others.

Step 2: AI-Powered Refinement

After the initial categorization, the file’s title is fed into GPT-4 via LangChain. GPT analyzes the title and provides a more specific category for the file. For example, a file named corolla_ebrochure.pdf may be categorized as Automobiles based on its title.

If the AI determines a more specific folder is appropriate, the file is moved to that folder inside the initial category folder.

Installation

Prerequisites

	1.	Python 3.8+
	2.	OpenAI API Key: You will need an OpenAI API key to use GPT-4.
	3.	LangChain: The AI backend for enhanced file categorization.
Future Plans

	•	Graphical User Interface (GUI): We have one created, but it could be improved, it includes color coded files, and other features, etc. An easy-to-use GUI for adjusting 		settings and managing file categorizations. 
	•	Content-Based Categorization: Use AI to categorize files based on their contents, not just their titles.
	•	Multi-Level Categorization: Enable sub-folder creation based on more detailed AI analysis.

Contributing
- Hackathon group - 4 people
  

License

This project is licensed under the MIT License - see the LICENSE file for details.





>>>>>>> AI powered file organizer, with GUI created by ChickenGamer.
>>>>>>> 
