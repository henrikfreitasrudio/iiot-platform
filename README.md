# 🚀 IIoT Platform (Base)

Plataforma base para aplicações de IIoT (Industrial Internet of Things), focada em coleta, processamento e disponibilização de dados de sensores em tempo real.

## 📌 Objetivo

Este projeto serve como fundação para sistemas IIoT mais complexos, permitindo:

* Recebimento de dados de dispositivos embarcados
* Processamento de leituras (ex: temperatura, pressão)
* Armazenamento com timestamp
* Exposição via API REST

## 🧱 Arquitetura

O sistema segue uma arquitetura modular baseada em:

* **API Backend**: Responsável por receber e processar dados
* **Camada de serviço**: Regras de negócio
* **Persistência**: Armazenamento de dados
* **Containerização**: Execução via Docker

## 🛠️ Tecnologias

* Python
* FastAPI
* Docker
* SQLite / PostgreSQL
* Uvicorn

## 📡 Exemplo de Payload

```json
{
  "device_id": "esp32_01",
  "temperature": 25.4,
  "pressure": 101.3,
  "timestamp": "2026-04-20T10:00:00Z"
}
```

## ▶️ Como executar

```bash
docker build -t iiot-platform .
docker run -p 8000:8000 iiot-platform
```

Acesse:

```
http://localhost:8000/docs
```

## 📁 Estrutura

```
app/
 ├── main.py
 ├── controllers/
 ├── services/
 ├── repositories/
 └── models/
```

## 🔮 Roadmap

* [ ] Autenticação com JWT
* [ ] Integração com MQTT
* [ ] Dashboard (Grafana)
* [ ] Deploy em Raspberry Pi
* [ ] Integração com ESP32

## 🤝 Objetivo profissional

Este projeto faz parte da minha evolução como desenvolvedor focado em:

* Sistemas embarcados
* Backend para IIoT
* Arquiteturas escaláveis

---
