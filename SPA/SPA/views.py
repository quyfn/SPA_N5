from django.shortcuts import render


def service_dashboard(request):
    services = [
        {
            "name": "Chăm sóc da mặt cao cấp",
            "description": "Liệu trình chăm sóc chuyên sâu với công nghệ Hàn Quốc",
            "price": "1.000.000",
            "status": "Hoạt động",
            "image_class": "peach",
        },
        {
            "name": "Massage body thư giãn",
            "description": "Massage toàn thân với tinh dầu thiên nhiên",
            "price": "800.000",
            "status": "Hoạt động",
            "image_class": "amber",
        },
        {
            "name": "Triệt lông công nghệ Diode",
            "description": "Công nghệ triệt lông vĩnh viễn an toàn",
            "price": "800.000",
            "status": "Hoạt động",
            "image_class": "sun",
        },
        {
            "name": "Gội đầu dưỡng sinh",
            "description": "Liệu trình chăm sóc tóc và da đầu",
            "price": "300.000",
            "status": "Hoạt động",
            "image_class": "sea",
        },
        {
            "name": "Trị mụn chuyên sâu",
            "description": "Làm sạch, lấy nhân mụn, phục hồi da",
            "price": "800.000",
            "status": "Hoạt động",
            "image_class": "rose",
        },
        {
            "name": "Acne Detox Therapy",
            "description": "Thanh lọc da mụn, làm sạch sâu lỗ chân lông",
            "price": "950.000",
            "status": "Hoạt động",
            "image_class": "mint",
        },
        {
            "name": "Post-Acne Recovery Therapy",
            "description": "Phục hồi da sau mụn, giảm thâm sẹo",
            "price": "1.200.000",
            "status": "Hoạt động",
            "image_class": "violet",
        },
    ]
    return render(request, "service_dashboard.html", {"services": services})


def customer_dashboard(request):
    customers = [
        {"id": 1, "name": "Nguyễn Thị Lan", "gender": "Nữ", "phone": "0901234567", "points": "500 điểm"},
        {"id": 2, "name": "Phạm Thị Hoài", "gender": "Nữ", "phone": "0905050323", "points": "200 điểm"},
        {"id": 3, "name": "Võ Bích Hợp", "gender": "Nữ", "phone": "0328775385", "points": "1.000 điểm"},
        {"id": 4, "name": "Nguyễn Thị Hoa", "gender": "Nữ", "phone": "0384726564", "points": "300 điểm"},
        {"id": 5, "name": "Lê Thị Bé Như", "gender": "Nữ", "phone": "0376258537", "points": "600 điểm"},
        {"id": 6, "name": "Nguyễn Cao Sang", "gender": "Nam", "phone": "0387642458", "points": "100 điểm"},
        {"id": 7, "name": "Đoàn Thanh Nhã", "gender": "Nam", "phone": "0927462684", "points": "100 điểm"},
    ]
    return render(request, "customer_dashboard.html", {"customers": customers})


def customer_detail(request, customer_id):
    customer = {
        "id": customer_id,
        "name": "Nguyễn Thị Lan",
        "gender": "Nữ",
        "age": "32",
        "email": "nguyenlanvn@gmail.com",
        "address": "Mỹ An, Ngũ Hành Sơn, TP Đà Nẵng",
        "history": [
            {
                "date": "30/01/2026",
                "service": "Chăm sóc da mặt cao cấp",
                "status": "Hoàn Thành",
                "price": "1.000.000",
            },
            {
                "date": "11/02/2026",
                "service": "Post-Acne Recovery Therapy",
                "status": "Hoàn Thành",
                "price": "1.200.000",
            },
        ],
    }
    return render(request, "customer_detail.html", {"customer": customer})


def feedback_dashboard(request):
    feedbacks = [
        {
            "id": 1,
            "name": "Hương Nguyễn",
            "time": "3 ngày trước",
            "service": "Chăm sóc da mặt Collagen",
            "rating": "5.0",
            "status": "Đã phản hồi",
            "status_class": "green",
            "content": "Mình rất hài lòng với dịch vụ chăm sóc da tại Mai Trâm! Chuyên viên tư vấn rất tận tình, quy trình làm chuyên nghiệp. Da mình sau liệu trình sáng mịn hơn, mụn cũng giảm đáng kể. Không gian cũng rất sang trọng và thư giãn. Chắc chắn sẽ quay lại!",
            "avatar_class": "avatar-peach",
        },
        {
            "id": 2,
            "name": "Luyện Đặng",
            "time": "19/01/2025",
            "service": "Massage body thư giãn",
            "rating": "4.0",
            "status": "Chưa phản hồi",
            "status_class": "yellow",
            "content": "Dịch vụ massage rất tốt! Nhân viên massage chuyên nghiệp, lực tay vừa phải. Tinh dầu thơm nhẹ nhàng không gây kích ứng. Sau 60 phút massage, cơ thể mình thư giãn hẳn, giảm đau mỏi vai gáy rất nhiều. Giá cả hợp lý, spa sạch sẽ thoáng mát.",
            "avatar_class": "avatar-neutral",
        },
        {
            "id": 3,
            "name": "Tuyết Sương",
            "time": "1 năm trước",
            "service": "Triệt lông Laser Diode",
            "rating": "4.0",
            "status": "Đã phản hồi",
            "status_class": "green",
            "content": "Dịch vụ triệt lông ổn, máy móc hiện đại. Nhân viên tư vấn kỹ về quy trình và số buổi cần thiết. Có điều mình thấy thời gian chờ hơi lâu một chút. Nhưng nhìn chung thì dịch vụ tốt, sau 3 buổi thấy lông mọc thưa hơn hẳn.",
            "avatar_class": "avatar-rose",
        },
    ]
    return render(request, "feedback_dashboard.html", {"feedbacks": feedbacks})


def feedback_detail(request, feedback_id):
    feedback = {
        "id": feedback_id,
        "name": "Luyện Đặng",
        "date": "19/01/2025",
        "service": "Massage body thư giãn",
        "rating": "4.0",
        "status": "Chưa phản hồi",
        "content": "Dịch vụ massage rất tốt! Nhân viên massage chuyên nghiệp, lực tay vừa phải. Tinh dầu thơm nhẹ nhàng không gây kích ứng. Sau 60 phút massage, cơ thể mình thư giãn hẳn, giảm đau mỏi vai gáy rất nhiều. Giá cả hợp lý, spa sạch sẽ thoáng mát.",
    }
    return render(request, "feedback_detail.html", {"feedback": feedback})
