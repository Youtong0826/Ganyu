[Ganyu](https://discord.com/oauth2/authorize?client_id=921673886049910795) | 一款使用 Pycord 製作的 Discord 機器人！

分層目錄介紹:
```
src
├── cogs ─ [cog 的操作指令] 
├── command_lib ─ [指令暫存檔/舊指令] 
├── commands - [主要指令的存放目錄]
│   ├── help.py
│   └── ...
│
├── core - [核心架構]
│   └── bot.py
│
├── database - [資料庫]
├── events - [各類事件的監聽器]
│   ├── interaction.py
│   └── ...
│
├── lib - [函式庫]
│   ├── functions.py
│   └── ...
│
└── bot.py [執行檔]
```