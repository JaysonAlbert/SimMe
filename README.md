# SimMe

A simulation of me on my wechat history

use wechat history to train a model, then use the model to chat on behalf of me.

## Technical details

- use ItChat-UOS to connect wechat
- use wechaty as the Chat Bot framework
- use gemma 2b as base model
- use Lara/Q-Lora to Fine-Tune the model
- use [WeChatMsg](https://github.com/LC044/WeChatMsg.git) to export wechat history

## Environment

- Python 3.10
- nvidia 4090

## How to use

```shell

pip install poetry

poetry install

poetry shell

python src/bot.py

```
