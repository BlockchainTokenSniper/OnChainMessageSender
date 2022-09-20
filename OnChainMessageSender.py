################## Fill in with your details ##########################

walletAddress = "Your wallet address to send message from"
walletPrivateKey = "Your wallet private key"

whereToSend = "Wallet address to send message to"
messageToSend = "This is an example message to send. Testing testing 123."
sendValue = 0

# Setup as default for BSC mainnet
ethNodeURL = "https://bsc-dataseed.binance.org"
gasPrice = 5

#######################################################################

from web3 import Web3

web3 = Web3(Web3.HTTPProvider(ethNodeURL))

rawTX = {
    'from': walletAddress,
    'to': whereToSend,
    'value': web3.toWei(sendValue, 'ether'),
    'data': messageToSend.encode("utf-8").hex(),
    'gasPrice': web3.toWei(gasPrice, 'gwei'),
    'nonce': web3.eth.get_transaction_count(walletAddress),
    'chainId': web3.eth.chain_id
}

rawTX['gas'] = web3.eth.estimateGas(rawTX)

signedTX = web3.eth.account.sign_transaction(rawTX, walletPrivateKey)
txHash = web3.eth.send_raw_transaction(signedTX.rawTransaction)

print("Successfully sent message TX: " + web3.toHex(txHash))
