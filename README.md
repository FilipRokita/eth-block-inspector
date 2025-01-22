# ETH Block Inspector

A Python script that connects to the Ethereum network using Infura and analyzes a specific Ethereum block. It identifies:
- The most common **sender** (from address) in the block.
- The most common **receiver** (to address) in the block.
- The **transaction with the highest gas price**.

## Features

- Connects to the Ethereum network via the Infura API.
- Fetches and analyzes all transactions in a specified block.
- Identifies:
    - The most frequent sender and receiver addresses.
    - The transaction with the highest gas price.
- Outputs detailed results for quick analysis.
- Error handling for network or data issues.

## Prerequisites

1. Python 3.12 or later installed.
2. An Infura account with a registered project.
3. Installed required Python dependencies.

## Installation

1. Clone this repository.
2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the script directory and add your Infura URL:
    ```
    INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
    ```

## Usage

1. Open the script and ensure the block number to analyze is set:
    - Default block number (placeholder): **13507875**
    - To change it, modify the `block_number` variable in the script.
2. Run the script:
    ```bash
    python eth-block-inspector.py
    ```
3. The script will output:
    - The most common sender and the number of transactions they sent.
    - The most common receiver and the number of transactions they received.
    - The transaction with the highest gas price, including:
        - Transaction hash
        - Gas price in wei
        - Sender address
        - Receiver address

## Example Output

```markdown
Analyzing block 13507875 with 503 transactions...

Results:
Most Common Sender: 0x46340b20830761efd32832A74d7169B29FEB9758 with 16 transactions
Most Common Receiver: 0xA090e606E30bD747d4E6245a1517EbE430F0057e with 98 transactions
Transaction with the Highest Gas Price:
  Hash: dbac7f98d43874d28c8cff965acda3ddf6a868dba2df4ac618b451a5c8361654
  Gas Price: 324000000000 wei
  From: 0x8Fe748F51D4c7893BE9Ee177091e8e8e20Af3029
  To: 0xe66B31678d6C16E9ebf358268a790B763C133750
```

## Troubleshooting

- **Failed to connect to the Ethereum network**:
    - Verify the Infura URL in the `.env` file.
    - Ensure your internet connection is active.
- **Invalid or empty block**:
    - Confirm that the block number exists on the Ethereum mainnet.

## Customization

- **Dynamic Block Input**:
    - Uncomment the `block_number = int(input(...).strip())` line to allow user input for the block number.
- **Logging**:
    - Replace `print()` with `logging` for more structured outputs.

## Author
[Filip Rokita](https://www.filiprokita.com/)
