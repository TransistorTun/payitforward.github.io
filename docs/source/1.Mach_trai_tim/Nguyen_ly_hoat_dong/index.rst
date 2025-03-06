Nguyên lý hoạt động
*******************************************************************************
Mạch LED trái tim thường được thiết kế để tạo ra hiệu ứng nhấp nháy hoặc "chạy" LED theo các mẫu nhất định. Mạch này sử dụng một số linh kiện cơ bản như: IC tạo xung NE555, IC ghi dịch 74HC595, LED, điện trở, tụ điện,... Mạch được tạo thành từ hai phần chính: mạch tạo xung và mạch điều khiển LED.

Mạch tạo xung
------------------------
Mạch này có nhiệm vụ tạo ra các xung clock liên tục để điều khiển quá trình ghi dịch dữ liệu trong mạch bằng việc cấu hình NE555 ở chế độ astable. Tần số của các xung này phụ thuộc vào các điện trở và tụ điện được cấu hình cho NE555.

Giới thiệu về IC NE555 — một IC quen thuộc, thường dùng để tạo xung clock. Dưới đây là chức năng của từng chân:

GND - Ground (Chân 1): Chân nối đất, kết nối với cực âm của nguồn điện.

VCC (Chân 8): Chân cấp nguồn, nối với cực dương của nguồn điện (thường từ 4.5V đến 9V).

DIS - Discharge (Chân 7): Chân xả, giúp xả điện tích của tụ điện trong mạch tạo xung, đóng vai trò quan trọng trong cả chế độ astable và monostable.

OUT (Chân 3): Chân xuất tín hiệu, cung cấp tín hiệu đầu ra (cao hoặc thấp) tùy vào trạng thái của bộ định thời.

RST - Reset (Chân 4): Chân reset, dùng để đặt lại NE555 về mức thấp khi được kéo xuống 0V. Nếu không dùng, chân này thường được nối lên VCC.

THRS - Threshold (Chân 6): Chân ngưỡng, so sánh điện áp của tụ điện với 2/3 VCC. Khi điện áp tụ vượt qua mức này, đầu ra sẽ chuyển trạng thái.

TRIG - Trigger(Chân 2): Chân kích, khi điện áp giảm xuống dưới 1/3 VCC, NE555 sẽ kích hoạt và đưa đầu ra lên mức cao, bắt đầu một chu kỳ.

CV - Control Voltage (Chân 5): Chân điều khiển điện áp, cho phép điều chỉnh điện áp tham chiếu bên trong. Thường được nối với đất qua một tụ điện để tăng độ ổn định.

Xung clock này đóng vai trò tạo ra các hiệu ứng nhấp nháy của LED. VD: Nếu bạn muốn LED sáng theo kiểu từ trái sang phải, dữ liệu nạp vào mạch điều khiển LED có thể là: 00000001 → 00000010 → 00000100 → ... Mỗi xung clock sẽ đẩy từng bit này qua, làm LED sáng lần lượt.  Tần số xung clock càng lớn thì hiệu ứng nhấp nháy càng nhanh.

Từ đó, ta nhận thấy điểm thú vị của mạch này là bạn có thể thay đổi hiệu ứng của các LED bằng cách điều chỉnh tần số của xung clock tại ngõ ra NE555. 

Mạch điều khiển LED
------------------------
Mạch này có nhiệm vụ nhận dữ liệu từ mạch tạo xung và điều khiển LED sáng tương ứng. Mạch này sử dụng IC ghi dịch 74HC595 để ghi dữ liệu vào các LED. Mỗi bit của dữ liệu sẽ tương ứng với một LED. VD: 00000001 → LED 1 sáng, 00000010 → LED 2 sáng, ... Điều đặc biệt là mạch này có thể điều khiển nhiều LED cùng một lúc, giúp tạo ra các hiệu ứng nhấp nháy phức tạp. Để làm được điều này, các IC 74HC595 được kết nối theo kiểu daisy-chain, tức là dữ liệu từ mạch tạo xung sẽ được ghi vào IC đầu tiên, sau đó từ IC này sẽ được chuyển tiếp sang IC tiếp theo, và cứ tiếp tục như vậy cho đến khi dữ liệu đã gửi đủ, ngay khi có tín hiệu kích hoạt tại chân LATCH, các IC sẽ cập nhật trạng thái của các LED.