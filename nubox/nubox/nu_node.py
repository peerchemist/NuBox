#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Copyright 2016 Peerchemist
#
# This file is part of Peerbox project.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import os
import getpass
from jsonrpc import Server

class Node:
    
    def __init__(self, shares=True):
        self.username = ""
        self.password = ""
        self.shares = shares
        self.testnet = False
        self.testnet_check()
        self.userpass()

        if self.testnet == False:
            if shares == True:
                self.node = Server('http://127.0.0.1:14001', 
                    auth=(self.username, self.password))
            else:
                self.node = Server('http://127.0.0.1:14002',
                    auth=(self.username, self.password))

        if self.testnet == True:
            self.node = Server('http://127.0.0.1:15001', 
                auth=(self.username, self.password))


    def userpass(self):
        '''Reads .ppcoin/ppcoin.conf file for username/password'''

        with open('/home/{0}/.nu/nu.conf'.format(getpass.getuser()), 'r') as conf:
            for line in conf:
                if line.startswith('rpcuser'):
                    self.username = line.split("=")[1].strip()
                if line.startswith("rpcpassword"):
                    self.password = line.split("=")[1].strip()

    def testnet_check(self):
        with open('/home/{0}/.nu/nu.conf'.format(getpass.getuser()), 'r') as conf:
            for line in conf:
                if line.startswith("testnet"):
                    if (line.split("=")[1] == 1 or line.split("=")[1] == True):
                        #self.testnet = True
                        return True

    def walletpassphrase(self, passphrase, timeout=999999, mint_only=True):
        '''used to unlock wallet for minting'''
        return self.node.walletpassphrase(passphrase, timeout, mint_only)

    def getblock(self, blockhash):
        '''returns detail block info.'''
        return self.node.getblock(blockhash)

    def getblockcount(self):
        '''Retrieve last block index'''
        return self.node.getblockcount()

    def getblockhash(self, block):
        '''retrieve block hash'''
        return self.node.getblockhash(block)

    def getbalance(self):
        '''retrieve balance'''
        return self.node.getbalance()

    def getdifficulty(self):
        '''Get PoS/PoW difficulty'''
        return self.node.getdifficulty()

    def getpeerinfo(self):
        '''Get connected peer's info'''
        return self.node.getpeerinfo()

    def getinfo(self):
        return self.node.getinfo()

    def getaddressesbyaccount(self, account=""):
        '''can be used to list asociated addresses'''
        return self.node.getaddressesbyaccount(account)

    def createnewaddress(self):
        return self.node.createnewaddress()

    def sendtoaddress(self, recv_addr, amount, comment=""):
        '''send ammount to address, with optional comment. Returns txid.
        sendtoaddress(ADDRESS, AMMOUNT, COMMENT)'''
        return self.node.sendtoaddress(recv_addr, amount, comment)

    def getconnectioncount(self):
        '''Get number of active connections'''
        return self.node.get_conn_count()

    def getdifficulty(self):
        '''Get PoS/PoW difficulty'''
        return self.node.getdifficulty()

    def getrawtransaction(self, txid, verbose=1):
        '''get raw transaction'''
        return self.node.getrawtransaction(txid, verbose)

    def getrawmempool(self):
        '''returns raw mempool'''
        return self.node.getrawmempool()

    def listtransactions(self):
        '''list all transactions associated with this wallet'''
        return self.node.listtransactions()

    def listreceivedbyaddress(self, minconf=0, includeempty=True):
        '''get list of all accounts in the wallet'''
        return self.node.listreceivedbyaddress(minconf, includeempty)

    def listunspent(self):
        '''list only unspent UTXO's'''
        return self.node.listunspent()

    ## Nu specifics

    def getdatafeed(self):
        return self.node.getdatafeed()

    def getmotions(self):
        return self.node.getmotions()

    def setvote(self, vote):
        return self.node.setvote(vote)

    def setdatafeed(self, url, sig_url, addr, parts=""):

        if parts == "":
            return self.node.setdatafeed(url, sig_url, addr)
        else:
            return self.node.setdatafeed(url, sig_url, addr, parts)

    ### NBT only functions

    def getliquidityinfo(self):
        if self.shares == False:
            return self.node.getliquidityinfo("B")

    def getparkrates(self):
        if self.shares == False:
            return self.node.getparkrates()