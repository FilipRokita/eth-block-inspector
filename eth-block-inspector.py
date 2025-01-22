# Description: This script connects to the Ethereum network using Infura and analyzes a specific block to find
#              the most common sender and receiver addresses, as well as the transaction with the highest gas price.
# Author: Filip Rokita


# Import required libraries
import os
from web3 import Web3
from collections import Counter
from dotenv import load_dotenv


def main():
    """
    Main function that connects to the Ethereum network using Infura and analyzes a specific block
    to find the most common sender and receiver addresses, as well as the transaction with thehighest gas price.
    """
    # Connect to the Ethereum network
    load_dotenv()
    INFURA_URL = os.getenv("INFURA_URL")
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))
    
    # Check if connection was successful
    if not web3.is_connected():
        print("Failed to connect to the Ethereum network. Check your INFURA_URL.")
        return

    # Block number to analyze (can be changed ofc)
    block_number = 13507875

    # Option 2: Let user input block number
    # Commented out, due to the task requirements.
    # block_number = int(input("Enter block number to analyze: ").strip())

    # Fetch block details
    block = web3.eth.get_block(block_number, full_transactions=True)
    print(f"Analyzing block {block_number} with {len(block['transactions'])} transactions...")

    # Analyze transactions
    senders = Counter()
    receivers = Counter()
    highest_gas_price_tx = None

    for tx in block['transactions']:
        # Increment sender and receiver counters
        senders[tx['from']] += 1
        if tx['to']:
            receivers[tx['to']] += 1
        
        # Check for highest gas price transaction
        if not highest_gas_price_tx or tx['gasPrice'] > highest_gas_price_tx['gasPrice']:
            highest_gas_price_tx = tx

    # Find the most common sender and receiver
    most_common_sender = senders.most_common(1)
    most_common_receiver = receivers.most_common(1)

    # Display results
    print("\nResults:")

    # Display most common sender
    if most_common_sender:
        print(f"Most Common Sender: {most_common_sender[0][0]} with {most_common_sender[0][1]} transactions")
    else:
        print("No sender data available.")

    # Display most common receiver
    if most_common_receiver:
        print(f"Most Common Receiver: {most_common_receiver[0][0]} with {most_common_receiver[0][1]} transactions")
    else:
        print("No receiver data available.")

    # Display transaction with the highest gas price
    if highest_gas_price_tx:
        print(f"Transaction with the Highest Gas Price:")
        print(f"  Hash: {highest_gas_price_tx['hash'].hex()}")
        print(f"  Gas Price: {highest_gas_price_tx['gasPrice']} wei")
        print(f"  From: {highest_gas_price_tx['from']}")
        print(f"  To: {highest_gas_price_tx['to']}")
    else:
        print("No transaction data available.")


# Run the main function
if __name__ == "__main__":
    main()
