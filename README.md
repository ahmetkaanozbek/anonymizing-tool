This tool is designed to anonymize legal documents, ensuring data privacy when sharing them with remote LLMs. While some LLMs claim they don’t utilize shared data for model training, trust levels regarding confidential information are currently uncertain. Therefore, I created this tool to prevent potential data breaches by anonymizing private or confidential data.

There are currently two versions available. Both versions accept `.pdf` files as input since most of the documents are in that format. They convert the `.pdf` file into a `.txt` file for easier replacement, then perform the replacement and provide a new `.txt` file with the specified name and location.
In the first version, which is in the `textAnonymizer.py` file, you need to manually provide the words or groups of words to be replaced. You can do this by setting the `words_to_replace` variable with your desired replacements.

The second version, found in `llama3TextAnonymizer.py`, uses a local model called Meta-Llama-3-8B. This model works offline and doesn't require internet access, ensuring data privacy for confidential information. However, it has limitations, especially with non-English languages, and is not suitable for complex tasks. It identifies private data based on the given prompt and returns the output in JSON format. The rest of the process remains the same as the first version.

It's worth noting that the second version may give incorrect outputs when attempting to anonymize long texts, making it less practical for now.

The program is still under development. Therefore, I will add more features in the future.

If you encounter any issues or have suggestions or want to contribute code, I would be very happy. Thank you for your interest in my project, and I appreciate your support!
