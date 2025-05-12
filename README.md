# 📅 MyRouteCalendar

Python 기반 장소 시각화 일정 관리 앱
날짜별 장소와 메모를 저장하고, Kakao 지도로 경로를 시각화합니다.

---

## ✨ 주요 기능

* 날짜별 장소 & 메모 입력
* 장소 저장/불러오기 (JSON 저장)
* Kakao 지도에 장소 핀 표시
* 자동 경로 연결 (Polyline)
* 총 이동 거리 계산 (km)

---

## 📷 사용 예시

> 장소: 서울특별시청
> 메모: 테스트1

![캔리더 UI](/Users/hyu/Documents/Project_Goplan/image copy.png)
![지도 출력](/Users/hyu/Documents/Project_Goplan/image.png)

---

## 🚀 실행 방법

### 1. 가상환경 실행

```bash
source venv/bin/activate
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 앱 실행

```bash
python main.py
```

---

## 🛠️ 프로젝트 구조

```
myroute_calendar/
├── ui/
│   └── calendar_ui.py      # Tkinter UI
├── map/
│   ├── map_view.html       # Kakao 지도 출력용 HTML
│   └── map_controller.py   # 지도 그린기 로직
├── utils/
│   └── save_load.py        # JSON 저장/불러오기
├── data/routes.json        # 장소 데이터 저장
├── main.py                 # 실행 진입점
└── README.md
```

---

## 📺 Kakao 지도 연동

* Kakao JavaScript SDK 사용
* Geocoder로 장소 → 좌표 변환
* 지도 위 링크와 표시 + 경로 연결
* Haversine 공식으로 거리 계산

---

## 💡 감사 가능성

* 장소 검색 자동완성
* 장소 순서 포함 편집
* PDF로 일정 요약 저장
* Flask 기반 웹 버전 확장 가능

---

## 📚 사용 기술

| 항목       | 사용 내용                |
| -------- | -------------------- |
| Language | Python 3.10+         |
| GUI      | Tkinter + tkcalendar |
| 지도 API   | Kakao JavaScript SDK |
| 저장       | JSON 파일 기반           |
