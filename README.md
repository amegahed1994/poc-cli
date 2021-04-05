## mvt-cli:

A command line interface (built using Click) whose's goal is to unify all of our scripts. Click reduces boilerplate code significantly and is easy to use.

## Installation

1. Clone this repository
   ```sh
   git clone <URL>
   ```
2. Create a virtual environment
   ```sh
   virtualenv venv
   ```
3. Activate the environment
   ```sh
   . venv/bin/activate
   ```
5. Install the python application
   ```sh
   python3 install ./poc-cli
   ```
4. Start mvt-cli, hurray!
   ```sh
   mvt
   ```
   
## Example usage:

Let's use this cli to compare 2 BigQuery datasets; to see if they are equal (in terms of data).

   ```sh
   mvt bq datasets compare --from-json=sample.json
   ```

where `sample.json` needs to conform to the following format:

```json
[
   {
      "src_dataset_name":"mydataset",
      "src_project_id":"sourceproject",
      "dest_dataset_name":"mydataset",
      "dest_project_id":"destinationproject"
   },
   {
      "src_dataset_name":"mydataset2",
      "src_project_id":"sourceproject",
      "dest_dataset_name":"mydataset2",
      "dest_project_id":"destinationproject"
   }
]
```
