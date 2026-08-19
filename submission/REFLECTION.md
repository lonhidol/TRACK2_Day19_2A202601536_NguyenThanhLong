# Reflection — Lab 19

**Tên:** Nguyễn Thành Long
**Cohort:** A20-K3B
**Path đã chạy:** lite

---

## Câu hỏi (≤ 200 chữ)

> Trên golden set 50 queries, mode nào thắng ở loại query nào (`exact` /
> `paraphrase` / `mixed`), và tại sao? Khi nào bạn **không** dùng hybrid
> (i.e. khi nào pure BM25 hoặc pure vector là lựa chọn đúng)?

- **Exact**: **BM25** thắng (hoặc hòa) vì khách hàng dùng đúng từ khóa có trong tài liệu, thuật toán đếm tần suất từ (Lexical) hoạt động cực kỳ chính xác.
- **Paraphrase**: **Vector (Semantic)** thắng vì nó bám vào ý nghĩa ngữ nghĩa (dù từ vựng bị thay đổi hoàn toàn).
- **Mixed**: **Hybrid (RRF)** thắng tuyệt đối vì nó lấy thế mạnh của cả BM25 (chống rớt từ khóa kỹ thuật) và Vector (hiểu ngữ nghĩa) để bù trừ cho nhau, bao phủ trọn vẹn ý định phức tạp của người dùng.

**Khi nào KHÔNG dùng Hybrid?**
1. **Dùng pure BM25:** Khi hệ thống cần tìm kiếm mã số chính xác (Mã đơn hàng, log ID, tên riêng), nơi sai một ký tự là vô nghĩa.
2. **Dùng pure Vector:** Khi tìm kiếm đa phương tiện (tìm ảnh bằng ảnh) hoặc khi tài nguyên hệ thống cực kỳ hạn hẹp, yêu cầu tốc độ siêu tốc (Hybrid tốn gấp đôi tài nguyên vì phải chạy cả 2 luồng).

---

## Điều ngạc nhiên nhất khi làm lab này

Điều ngạc nhiên nhất là "Cái bẫy Recall" ở NB5 và nguy cơ rò rỉ dữ liệu chéo (Cross-tenant Leak) ở NB7. Nhận ra rằng nếu phó mặc việc đánh giá cho AI mà không tự thiết lập Ground Truth đúng, hệ thống sẽ im lặng che giấu những lỗi sai cực kỳ nghiêm trọng.

---

## Bonus challenge

- [ ] Đã làm bonus (xem `bonus/`)
- [ ] Pair work với: _<tên đồng đội nếu có>_
