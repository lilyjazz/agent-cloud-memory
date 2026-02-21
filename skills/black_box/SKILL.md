# Black Box (Powered by TiDB Zero)

## Goal
A "Flight Data Recorder" for Agents. Streams logs to a persistent cloud database, ensuring audit trails survive local crashes.

## Usage
*   **Log:** `python run.py --action log --level ERROR --message "System crash imminent"`
*   **Read:** `python run.py --action read --limit 5`
