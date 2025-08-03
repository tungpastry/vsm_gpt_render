# 📊 VSM GPT Query Server (Render Deployment)

API server cho phép người dùng gửi truy vấn SQL đến cơ sở dữ liệu PostgreSQL đang chạy trên máy chủ nội bộ (Ubuntu Desktop – 192.168.1.15) thông qua Cloudflare Tunnel (`db.vnstockaimentor.com`).

---

## 🚀 Mô hình triển khai

```text
[Client] ---> POST /query (SQL text)
                    |
                    v
         [Render FastAPI/Flask server]
                    |
                    v
        [PostgreSQL Local DB via Cloudflare Tunnel]
            (db.vnstockaimentor.com:5432)
