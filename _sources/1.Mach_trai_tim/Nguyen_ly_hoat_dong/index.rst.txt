Nguyên lý hoạt động
*******************************************************************************
Mạch LED trái tim thường được thiết kế để tạo ra hiệu ứng nhấp nháy hoặc "chạy" LED theo các mẫu nhất định. Mạch này sử dụng một số linh kiện cơ bản như: IC tạo xung NE555, IC ghi dịch 74HC595, LED, điện trở, tụ điện,... Mạch được tạo thành từ hai phần chính: mạch tạo xung và mạch điều khiển LED.

Mạch tạo xung
------------------------
Mạch này có nhiệm vụ tạo ra các xung clock liên tục để điều khiển quá trình ghi dịch dữ liệu trong mạch bằng việc cấu hình NE555 ở chế độ astable. Tần số của các xung này phụ thuộc vào các điện trở và tụ điện được cấu hình cho NE555.

Giới thiệu về IC NE555 — một IC quen thuộc, thường dùng để tạo xung clock. Dưới đây là chức năng của từng chân:

- 1 (GND) và 8 (VCC): dùng để cấp nguồn cho IC.
- 2 (Trigger): chân ngõ vào so áp với áp chuẩn là :math:`1/3 VCC`
- 3 (Output): chân ngõ ra tín hiệu.
- 4 (Reset): reset trạng thái ngõ ra, để IC  có thể tạo xung, cần nối chân này với VCC.
- 5 (Control Voltage): chân này dùng để điều chỉnh độ rộng xung, chân này có thể không kết nối.
- 6 (Threshold): chân ngõ vào so áp với áp chuẩn là :math:`2/3 VCC`.
- 7 (Discharge): chân này được nối với cực C của BJT bên trong IC, dùng để xả điện.

.. image:: img/ne555_block_diagram.png
   :align: center
   :alt: Priority
   :scale: 100%

Từ sơ đồ khối, ta cùng tìm hiểu chức năng từng khối bên trong NE555:

- Khối so sánh: bao gồm hai OPAMP được cấu hình theo mạch so sánh (khoanh đỏ),  OPAMP1 so sánh áp tại chân Trigger điện áp chuẩn :math:`\frac{1}{3} VCC` và đưa ra mức logic cho ngõ vào S của chốt SR. Khi áp tại chân Trigger thấp hơn áp chuẩn :math:`\frac{1}{3} VCC`, ngõ ra sẽ ở mức cao, ngược lại, ngõ ra sẽ ở mức thấp. Mặt khác, OPAMP2 so sánh áp tại chân Threshold với áp chuẩn :math:`\frac{2}{3} VCC` và đưa ra mức logic cho ngõ vào R của chốt SR. Khi áp tại chân Threshold cao hơn áp chuẩn :math:`\frac{2}{3} VCC`, ngõ ra sẽ ở mức cao, ngược lại, ngõ ra sẽ ở mức thấp. 

.. image:: img/ne555_comparator_block.png
   :align: center
   :alt: Priority
   :scale: 100%

- Khối phần tử nhớ: gồm chốt SR (khoanh đỏ) đóng vai trò lưu trữ trạng thái thông tin. Trạng thái của ngõ ra Q phụ thuộc vào trạng thái ngõ vào của chân S và R. Trạng thái của ngõ ra :math:`\overline{Q}` là ngõ ra đảo của Q.

.. image:: img/ne555_latch_sr.png
   :align: center
   :alt: Priority
   :scale: 100%

.. image:: img/latch_sr_truth_table.png
   :align: center
   :alt: Priority
   :scale: 100%

- Khối cổng logic: thường nhà sản xuất sẽ nối chân OUTPUT với ngõ ra Q của chốt SR, tuy nhiên có vài trường hợp, ngõ ra :math:`\overline{Q}` sẽ qua một cổng NOT và kết nối với chân OUTPUT. Nhiệm vụ của cổng NOT đơn giản là đảo trạng thái của ngõ vào và đưa ra ngõ ra.

Từ đó, ta có thể suy ra bảng chân trị cho NE555 như sau:

.. image:: img/ne555_truth_table.png
   :align: center
   :alt: Priority
   :scale: 90%


Như vậy, từ sơ đồ khối, ta nhận thấy có thể dùng NE555 tạo xung clock bằng cách thay đổi điện áp trên chân Trigger và Threshold.

Mạch điều khiển LED
------------------------
Mạch này có nhiệm vụ nhận dữ liệu từ mạch tạo xung và điều khiển LED sáng tương ứng. Mạch này sử dụng IC ghi dịch 74HC595 để ghi dữ liệu vào các LED. Mỗi bit của dữ liệu sẽ tương ứng với một LED. VD: 00000001 → LED 1 sáng, 00000010 → LED 2 sáng, ... Điều đặc biệt là mạch này có thể điều khiển nhiều LED cùng một lúc, giúp tạo ra các hiệu ứng nhấp nháy phức tạp. IC 74HC595 là một thanh ghi dịch 8 bit kèm theo một thanh ghi chốt (latch) giúp mở rộng số chân đầu ra của vi điều khiển. Nó thường được sử dụng để điều khiển nhiều LED, màn hình 7 đoạn, hoặc các thiết bị cần nhiều chân I/O. Cấu tạo chính của 74HC595:

- DS (Data Serial, Chân 14): Chân dữ liệu nối tiếp, dùng để nhận dữ liệu.
- SHCP (Shift Clock, Chân 11): Chân xung clock để dịch dữ liệu vào. Mỗi xung clock, dữ liệu ở DS sẽ được đẩy vào hàng đợi.
- STCP (Storage Clock, Chân 12): Chân chốt (latch). Khi có cạnh lên ở chân này, dữ liệu từ thanh ghi dịch sẽ được chốt sang thanh ghi lưu trữ và đưa ra các chân đầu ra Q0-Q7.
- OE (Output Enable, Chân 13): Cho phép hoặc vô hiệu hóa đầu ra (mức thấp để kích hoạt đầu ra).
- MR (Master Reset, Chân 10): Reset toàn bộ thanh ghi nếu kéo xuống mức thấp.
- Q0-Q7 (Chân 15, 1-7): 8 chân đầu ra song song.
- Q7’ (Chân 9): Đầu ra nối tiếp, dùng để kết nối với IC 74HC595 khác để mở rộng số đầu ra.
- VCC (Chân 16): Nguồn dương (4.5V - 5.5V).
- GND (Chân 8): Nối đất.