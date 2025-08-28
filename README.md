# FT Algo Bot - FINNIFTY Options Trading Strategy

This repository contains a Python-based trading bot that automates a specific options strategy for the FINNIFTY index. The bot is designed to run on a Virtual Private Server (VPS) and uses the Flattrade API for live trading or paper trading.

---

## Strategy Overview

The bot implements a predefined options trading strategy on FINNIFTY monthly expiry contracts with the following logic:

* *Entry:* After 9:20 AM, the bot enters a position by simultaneously buying and selling options.
    * *Buy:* 5th OTM CE (Call) and 5th OTM PE (Put)
    * *Sell:* 3rd OTM CE (Call) and 3rd OTM PE (Put)
* *Lot Size:* The standard lot size for FINNIFTY, which is 40.
* *Trailing Stop Loss (SL):*
    * Activates after the overall strategy profit reaches ₹300.
    * Trailing buffer is ₹50.
    * The SL trails the highest profit achieved with a step of ₹1.
* *Re-entry:* If the stop loss is hit, the bot waits for 5 minutes before attempting a new entry.
* *Exit:*
    * The bot exits all positions if the trailing stop loss is hit.
    * On the monthly expiry day (the last Tuesday of the month), all positions are forcibly exited at 2:00 PM to avoid any risk from illiquid contracts.
* *Manual Control:* You can manually pause or resume the bot by creating or deleting a specific file on the VPS.

---

## Prerequisites

Before you can run the bot, you need to set up your environment and obtain the necessary API credentials.

1.  *Flattrade API Credentials:* You must have an active Flattrade account and have generated your API Key, API Secret, and TOTP Secret.
2.  *Python 3:* The bot requires Python 3.8 or newer.
3.  *Virtual Private Server (VPS):* A Linux-based VPS is recommended for reliable, 24/7 operation.

---

## Installation & Setup

Follow these steps to get the bot running on your VPS.

### 1. Clone the Repository

Log in to your VPS via SSH and clone this repository.

```bash
git clone [https://github.com/Pradyushm24/ft_algo_new.git](https://github.com/Pradyushm24/ft_algo_new.git)
cd ft_algo_new.git
