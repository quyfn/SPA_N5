from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


def get_public_reviews():
    return [
        {
            "name": "Nguyễn Hà My",
            "time": "2 ngày trước",
            "rating": 5,
            "service": "Chăm sóc da mặt chuyên sâu",
            "content": "Không gian spa sang và thoáng. Kỹ thuật viên soi da kỹ, làm rất nhẹ tay và tư vấn routine sau liệu trình rõ ràng. Da mình đều màu và mềm hơn chỉ sau một buổi.",
            "image_urls": [
                "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=900&q=80",
                "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=900&q=80",
            ],
        },
        {
            "name": "Trần Khánh Linh",
            "time": "5 ngày trước",
            "rating": 5,
            "service": "Gội đầu dưỡng sinh",
            "content": "Mùi tinh dầu dễ chịu, phòng làm việc sạch và yên tĩnh. Phần massage đầu vai gáy rất đã, đúng kiểu dịch vụ để quay lại sau những ngày làm việc căng thẳng.",
            "image_urls": [],
        },
        {
            "name": "Lê Bảo Ngọc",
            "time": "1 tuần trước",
            "rating": 4,
            "service": "Post-Acne Recovery Therapy",
            "content": "Liệu trình phục hồi sau mụn làm mình hài lòng. Độ đỏ giảm rõ, da được hướng dẫn chăm sóc tại nhà khá chi tiết. Nếu có thêm gói combo thì sẽ rất hợp lý.",
            "image_urls": [
                "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=900&q=80",
            ],
        },
        {
            "name": "Phạm Thu Hằng",
            "time": "2 tuần trước",
            "rating": 5,
            "service": "Massage body thư giãn",
            "content": "Phòng hương nhẹ, nhạc vừa đủ và thao tác rất chuyên nghiệp. Sau 60 phút massage mình thấy cơ thể được thả lỏng hoàn toàn. Trải nghiệm đồng đều từ lúc check-in đến lúc ra về.",
            "image_urls": [],
        },
        {
            "name": "Võ Minh Anh",
            "time": "3 tuần trước",
            "rating": 4,
            "service": "Triệt lông công nghệ Diode",
            "content": "Máy móc mới, nhân viên giải thích quy trình kỹ và nhắc lịch tái khám đầy đủ. Lần đầu hơi hồi hộp nhưng làm xong thấy yên tâm. Hiệu quả cần thêm vài buổi nữa để đánh giá trọn vẹn.",
            "image_urls": [
                "https://images.unsplash.com/photo-1519415943484-9fa1873496d4?auto=format&fit=crop&w=900&q=80",
                "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=900&q=80",
                "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=900&q=80",
            ],
        },
        {
            "name": "Đoàn Ngọc Thảo",
            "time": "1 tháng trước",
            "rating": 5,
            "service": "Acne Detox Therapy",
            "content": "Mình đánh giá cao cách spa theo dõi da trước và sau buổi trị liệu. Phong cách phục vụ lịch sự, sạch sẽ và không bị tạo cảm giác bán hàng quá đà. Sẽ giới thiệu thêm bạn bè.",
            "image_urls": [],
        },
    ]


def user_login(request):
    """Xử lý đăng nhập người dùng"""
    if request.user.is_authenticated:
        # Nếu là admin/staff, vào service_dashboard
        if request.user.is_staff:
            return redirect('service_dashboard')
        # Nếu là người dùng thường, vào customer_dashboard
        return redirect('about_page')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f'Chào mừng {user.first_name or user.username}!')
                    # Nếu là admin/staff, vào service_dashboard
                    if user.is_staff:
                        return redirect('service_dashboard')
                    # Nếu là người dùng thường, vào customer_dashboard
                    return redirect('about_page')
                else:
                    messages.error(request, 'Mật khẩu không chính xác.')
            except User.DoesNotExist:
                messages.error(request, 'Email này không tồn tại.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_register(request):
    """Xử lý đăng ký tài khoản người dùng"""
    if request.user.is_authenticated:
        # Nếu là admin/staff, vào service_dashboard
        if request.user.is_staff:
            return redirect('service_dashboard')
        # Nếu là người dùng thường, vào customer_dashboard
        return redirect('about_page')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('email')
            user.save()

            messages.success(request, 'Đăng ký thành công! Vui lòng đăng nhập.')
            return redirect('user_login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def user_logout(request):
    """Xử lý đăng xuất"""
    logout(request)
    messages.success(request, 'Bạn đã đăng xuất thành công!')
    return redirect('user_login')


def service_dashboard(request):
    services = [
        {
            "name": "Chăm sóc da mặt cao cấp",
            "description": "Liệu trình chăm sóc chuyên sâu với công nghệ Hàn Quốc",
            "price": "1.000.000",
            "status": "Hoạt động",
            "image_class": "peach",
            "image_url": "https://tourdanangcity.vn/wp-content/uploads/2024/06/review-spa-hoi-an.jpg",
        },
        {
            "name": "Massage body thư giãn",
            "description": "Massage toàn thân với tinh dầu thiên nhiên",
            "price": "800.000",
            "status": "Hoạt động",
            "image_class": "amber",
            "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/63/9f/04/sakura-massage-spa.jpg?w=900&h=500&s=1",
        },
        {
            "name": "Triệt lông công nghệ Diode",
            "description": "Công nghệ triệt lông vĩnh viễn an toàn",
            "price": "800.000",
            "status": "Hoạt động",
            "image_class": "sun",
            "image_url": "https://images.virginexperiencedays.co.uk/images/product/large/mychocolate-chocoholic-workshop-with-29145629.jpg?auto=compress%2Cformat&w=1440&q=80&fit=max",
        },
        {
            "name": "Gội đầu dưỡng sinh",
            "description": "Liệu trình chăm sóc tóc và da đầu",
            "price": "300.000",
            "status": "Hoạt động",
            "image_class": "sea",
            "image_url": "https://static.vinwonders.com/production/2025/09/spa-ha-noi-topbanner.jpg",
        },
        {
            "name": "Trị mụn chuyên sâu",
            "description": "Làm sạch, lấy nhân mụn, phục hồi da",
            "price": "800.000",
            "status": "Hoạt động",
            "image_class": "rose",
            "image_url": "https://static.hotdeal.vn/images/1535/1534508/60x60/349662-dang-cap-massage-bau-5-thu-gian-toan-than-cho-me-khoe-be-thong-minh-tai-bloomy-spa.jpg",
        },
        {
            "name": "Acne Detox Therapy",
            "description": "Thanh lọc da mụn, làm sạch sâu lỗ chân lông",
            "price": "950.000",
            "status": "Hoạt động",
            "image_class": "mint",
            "image_url": "https://file.hstatic.net/200000827051/article/facial_treatment_f73cebb667794301afd01348897774e7.jpg",
        },
        {
            "name": "Post-Acne Recovery Therapy",
            "description": "Phục hồi da sau mụn, giảm thâm sẹo",
            "price": "1.200.000",
            "status": "Hoạt động",
            "image_class": "violet",
            "image_url": "https://hd1.hotdeal.vn/images/uploads/2016/Thang%208/31/285824/285824-dung-spa-body%20%289%29.jpg",
        },
    ]
    return render(request, "service_dashboard.html", {"services": services})


def appointment_dashboard(request):
    appointments = [
        {
            "id": 1,
            "customer": "Nguyễn Thị Trà My",
            "phone": "0901234567",
            "service": "Trị mụn chuyên sâu",
            "date": "25/02/2026",
            "time": "16:00",
            "status": "Đang Tiến Hành",
            "status_class": "green",
            "note": "Khách yêu cầu phòng riêng",
        },
        {
            "id": 2,
            "customer": "Phạm Thị Hoài",
            "phone": "0905050323",
            "service": "Triệt lông công nghệ Diode",
            "date": "10/02/2026",
            "time": "9:00",
            "status": "Hoàn Thành",
            "status_class": "blue",
            "note": "Đã hoàn tất liệu trình theo lịch đặt",
        },
        {
            "id": 3,
            "customer": "Võ Bích Hợp",
            "phone": "0328775385",
            "service": "Gội đầu dưỡng sinh",
            "date": "10/02/2026",
            "time": "13:00",
            "status": "Hoàn Thành",
            "status_class": "blue",
            "note": "Khách thanh toán tại quầy",
        },
        {
            "id": 4,
            "customer": "Nguyễn Thị Hoa",
            "phone": "0384726564",
            "service": "Post-Acne Recovery Therapy",
            "date": "11/02/2026",
            "time": "9:00",
            "status": "Hoàn Thành",
            "status_class": "blue",
            "note": "Khách đặt lại lịch tái khám",
        },
        {
            "id": 5,
            "customer": "Lê Thị Bé Như",
            "phone": "0376258537",
            "service": "Acne Detox Therapy",
            "date": "11/02/2026",
            "time": "13:00",
            "status": "Đã Hủy",
            "status_class": "red",
            "note": "Khách báo hủy trước 2 giờ",
        },
        {
            "id": 6,
            "customer": "Nguyễn Cao Sang",
            "phone": "0387642458",
            "service": "Acne Detox Therapy",
            "date": "12/02/2026",
            "time": "13:00",
            "status": "Hoàn Thành",
            "status_class": "blue",
            "note": "Khách yêu cầu xuất hóa đơn",
        },
        {
            "id": 7,
            "customer": "Đoàn Thanh Nhã",
            "phone": "0927462684",
            "service": "Post-Acne Recovery Therapy",
            "date": "9/02/2026",
            "time": "7:00",
            "status": "Đã Hủy",
            "status_class": "red",
            "note": "Khách đến trễ nên lịch bị hủy",
        },
    ]
    modal_state = request.GET.get("modal", "")
    return render(
        request,
        "appointment_dashboard.html",
        {
            "appointments": appointments,
            "modal_state": modal_state,
        },
    )


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


def get_consultation_data():
    return {
        1: {
            "id": 1,
            "name": "Mai Hồng Ngọc",
            "avatar_class": "chat-avatar-one",
            "messages": [
                {"side": "left", "text": "Cho em hỏi về dịch vụ bên mình bao nhiêu......", "time": "19:30"},
            ],
        },
        2: {
            "id": 2,
            "name": "Trần Thiên Hà",
            "avatar_class": "avatar-neutral",
            "messages": [
                {"side": "left", "text": "Shop ơi tư vấn này giúp e với .....", "time": "Hôm qua"},
            ],
        },
        3: {
            "id": 3,
            "name": "Ngô Thanh Vân",
            "avatar_class": "chat-avatar-two",
            "messages": [
                {"side": "left", "text": "Shop ơi tư vấn này giúp e với .....", "time": "23/01/2026"},
            ],
        },
        4: {
            "id": 4,
            "name": "Lê Thư Ý",
            "avatar_class": "chat-avatar-three",
            "messages": [
                {"divider": "23/01/2026"},
                {"side": "left", "text": "Shop ơi", "time": ""},
                {
                    "side": "right",
                    "text": "Dạ em chào chị, chị cần bên em tư vấn dịch vụ nào ạ?",
                    "time": "09:03",
                },
                {"side": "left", "text": "Mình muốn đặt lịch gội đầu dưỡng sinh vào cuối tuần này", "time": ""},
                {
                    "side": "right",
                    "text": "Dạ cuối tuần bên em còn slot 15:00 và 17:00, chị chọn giờ nào để em giữ lịch nhé.",
                    "time": "09:05",
                },
            ],
        },
        5: {
            "id": 5,
            "name": "Lê Trà Thư",
            "avatar_class": "avatar-neutral",
            "messages": [
                {"divider": "23/01/2026"},
                {"side": "left", "text": "Ngày mai nha", "time": ""},
                {
                    "side": "right",
                    "text": "Dạ em đã note lịch ngày mai cho chị rồi ạ.",
                    "time": "21:40",
                },
                {"side": "left", "text": "Khoảng 10h chị qua được không em?", "time": ""},
                {
                    "side": "right",
                    "text": "Dạ được chị nha, em giữ lịch 10:00 và sẽ nhắn xác nhận trước 30 phút ạ.",
                    "time": "21:42",
                },
            ],
        },
    }


def consultation_dashboard(request):
    conversation_data = get_consultation_data()
    conversations = []

    for item in conversation_data.values():
        messages = item["messages"]
        latest_message = next((msg for msg in reversed(messages) if "text" in msg), None)

        conversations.append(
            {
                "id": item["id"],
                "name": item["name"],
                "avatar_class": item["avatar_class"],
                "preview": latest_message["text"] if latest_message else "",
                "time": latest_message.get("time", "") if latest_message else "",
            }
        )

    search = request.GET.get("q", "").strip()
    empty_state = request.GET.get("empty", "") == "1"
    if search:
        lowered = search.lower()
        conversations = [item for item in conversations if lowered in item["name"].lower()]
    if empty_state:
        conversations = []
    return render(
        request,
        "consultation_dashboard.html",
        {
            "conversations": conversations,
            "search": search,
        },
    )


def consultation_detail(request, conversation_id):
    conversations = get_consultation_data()
    conversation = conversations.get(conversation_id, conversations[3])
    modal_state = request.GET.get("modal", "")
    return render(
        request,
        "consultation_detail.html",
        {
            "conversation": conversation,
            "modal_state": modal_state,
        },
    )


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


def about_page(request):
    return render(request, 'about.html')


def public_review_page(request):
    reviews = get_public_reviews()
    average_rating = round(sum(item["rating"] for item in reviews) / len(reviews), 1) if reviews else 0
    total_reviews = 120
    with_images = sum(1 for item in reviews if item["image_urls"])
    highlighted_reviews = reviews[:3]

    context = {
        "reviews": reviews,
        "highlighted_reviews": highlighted_reviews,
        "average_rating": average_rating,
        "total_reviews": total_reviews,
        "with_images": with_images,
    }
    return render(request, "public_reviews.html", context)
