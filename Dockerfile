# Backend stage
FROM python:3.11-slim as backend

WORKDIR /app

COPY apps/back-chatbot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/back-chatbot/ .

EXPOSE 8000

CMD ["python", "run_server.py"]

# Frontend stage
FROM node:18-alpine as frontend

WORKDIR /app

COPY apps/front-chatbot/package*.json ./
RUN npm ci

COPY apps/front-chatbot/ .

RUN npm run build

EXPOSE 5173

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "5173"]