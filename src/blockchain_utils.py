from web3 import Web3
import os

class BlockchainUtils:
    def __init__(self, web3_provider, private_key, source_address, target_address, contract_address, abi, chain_id):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to the blockchain network")
        
        self.private_key = private_key
        self.address = source_address
        self.target_address = target_address
        self.contract = self.web3.eth.contract(
            address=self.web3.to_checksum_address(contract_address), abi=abi
        )
        self.chain_id = chain_id

    def get_balance(self):
        balance = self.contract.functions.balanceOf(self.address).call()
        return balance

    def transfer_token(self, amount):
        nonce = self.web3.eth.get_transaction_count(self.address)
        tx = self.contract.functions.transfer(self.web3.to_checksum_address(self.target_address), amount).build_transaction({
            "chainId": self.chain_id,
            "gas": 70000,
            "gasPrice": self.web3.to_wei("5", "gwei"),
            "nonce": nonce,
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        return tx_hash.hex()
