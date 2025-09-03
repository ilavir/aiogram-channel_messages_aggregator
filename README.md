# Aiogram Channel Messages Aggregator Bot

A Telegram bot that aggregates gambling conversion messages from multiple source channels to a destination channel.

## Quick Start with Docker

### Prerequisites
- Docker and Docker Compose installed
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd aiogram-channel_messages_aggregator
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Edit `.env` file with your configuration:
```bash
nano .env
```

4. Start the bot:
```bash
docker-compose up -d
```

### Configuration

Edit the `.env` file with your values:

- `BOT_TOKEN`: Your Telegram bot token from BotFather
- `DESTINATION_CHANNEL`: Channel ID where aggregated messages will be sent
- `SOURCE_CHANNELS`: Comma-separated list of source channel IDs to monitor

### Commands

```bash
# Start bot
docker-compose up -d

# View logs
docker-compose logs -f

# Stop bot
docker-compose down

# Rebuild and restart
docker-compose up --build -d
```

### Getting Channel IDs

1. Add your bot to the channels as an admin
2. Forward a message from the channel to [@userinfobot](https://t.me/userinfobot)
3. Use the channel ID (including the minus sign for channels)
