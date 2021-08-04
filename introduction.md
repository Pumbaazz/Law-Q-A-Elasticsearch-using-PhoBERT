# 1. Môi trường cài đặt 
- **python3 **
- elasticsearch :
    Hướng dẫn cài đặt:
    B1: Truy cập vào page: https://www.elastic.co/downloads/elasticsearch -> Tải xuống bản cài cho Window
    B2: Copy vào thư mục bất kỳ rồi giải nén
    
- Install các thư viện cần thiết
    B1: mở powershell -> thay đổi tới thư mục này (XX\LAW)
    B2: pip install -r requirements.txt
- Ngoài ra còn 1 số thư viện có thể cài thêm trong quá trình chạy
# 2. Hướng dẫn chạy
- Khởi đông elastich
    B1: Vào thư mục giải nén trên-> vào thư mục Bin -> Chạy file elasticsearch.bat để khởi động elasticsearch
    B2: truy cập vào http://localhost:9200/ xem đã hiển thị dc chưa> Nếu hiển thị dc rồi thì đã khởi dộng elasticsearch thành công
- Index cho elasticsearch
    B1: mở powershell -> thay đổi tới thư mục này (XX\LAW)
    B2:  python .\convertdata.py
    Bước này thực hiện rất lâu tầm 3->4h để thực hiện xong
    Khi nào xuất hiện chữ: Done Index là đã đánh hết
    trên powershell sẽ xuát hiện các lệnh print: index 128, index 256 để xem có còn chạy Ok ko
    
- Start Web:
    B1: mở power shell -> thay đổi tới thư mục này (XX\LAW)
    B2:  python .\app.py



