# Labeling 설정 가이드

### 사용 프로그램 : mobaxterm

아래의 설정은 windows를 기준으로 작성되었습니다.

## 준비사항

1. [링크](https://download.mobatek.net/2202022022680737/MobaXterm_Installer_v22.0.zip)를 통해서 **mobaxterm**을 다운로드 및 설치합니다.
2. 아래의 파일 **`file.zip`**을 다운로드 받아서 바탕화면에 압축 해제합니다.
    
    [files.zip](Labeling%20%E1%84%89%20e0beb/files.zip)
    
3. [myip.com](http://myip.com) 사이트에 접속해서 아이피 정보를 전달 부탁드립니다.

![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled.png)

## 세팅 방법

- 설정 변경 없이 next만 눌러서 install 해주시면 됩니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%201.png)
    

- 실행시 아래와 같은 화면이 나오게 됩니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%202.png)
    

- 왼쪽 메뉴 리스트의 빈공간에서 마우스 우측 버튼을 누르고 `Import sessions from file` 을 클릭해줍니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%203.png)
    
- 압축 풀어둔 `files` 의 session 파일을 열어줍니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%204.png)
    

- 아래처럼 황금키 모양이 추가되었습니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%205.png)
    

- 해당 아이템을 마우스 우측 클릭하여 `Edit session` 을 클릭합니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%206.png)
    

- 아래쪽에 `Adavanced SSH settings` 탭을 누르면 메뉴가 뜨는데 여기서 `Use private key` 의 푸른색 서류 모양을 눌러서 `fiels/id_rsa` 파일을 선택해줍니다. **OK**를 눌러서 저장해줍니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%207.png)
    

- 이제 좌측 메뉴에서 해당 아이템을 더블 클릭시 자동으로 연결되며 프로그램이 실행됩니다.

## 레이블링 방법

이번에 진행할 레이블링(이미지에 정답을 표시하는 것)은 사각형 영역으로 물체를 저장하는 것 입니다.

- 대상이 되는 물체는 아래와 같습니다.
    
    
    | 대상 | object label | 설명 |
    | --- | --- | --- |
    | 모니터 | monitor | 단일 모니터의 경우 하나, 듀얼 모니터 이상일 경우 각각 표기 |
    | 손 | hand | 양손이 따로 위치하는 경우 각각, 겹치는 경우 하나만 표기 |
    | 책상 위  책 | book | 책장의 책은 제외 |
    | 책상 위 필기 노트 | notebook |  |
    | 포스트잇 | notepad |  |
- 작업시 주의할 점
    - 위의 항목이 하나도 없는 경우는 표기 없이 넘어갑니다.

### 레이블링 순서

- 좌측의  `OpenDir` 버튼을 눌러서 이미지 폴더를 열어줍니다.
    - 이미지 폴더는 작업자분 이메일 아이디로 되어 있습니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%208.png)
    
- 상단 메뉴에서 `File` - `Save Automatically`를 선택해줍니다.
    
    ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%209.png)
    

- 이미지가 뜨면 우측 하단에서 이미지 리스트를 볼 수 있습니다.
    - 상단의 메뉴에서 `Edit` - `Create Rectangle` 을 선택해줍니다.
        
        ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%2010.png)
        
    - 이제 클릭을 두번 해서 위에서 말씀드린 대상 물체를 사각형 박스로 선택합니다. 그 후 위 표의 `object label`에 해당하는 값을 입력해주세요. 여기서는 손을 선택했으니 hand를 입력합니다.(**두번째부터는 미리 입력되어 있으므로 선택만 해주시면 됩니다.**) 같은 방법으로 위의 표에 있는 물체가 보이면 전부 체크 해주시면 됩니다.
        
        **빠르게 하다보면 실수하는 경우가 많으니 주의해주세요!**
        
        ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%2011.png)
        
    - 전부 체크하시고 저장하시면 우측 하단의 리스트에 체크 됩니다. 다음 이미지를 눌러서 이어서 진행하시면 됩니다.
        
        ![Untitled](Labeling%20%E1%84%89%20e0beb/Untitled%2012.png)
        

## 기타 정보

- 이미지 파일은 외부로 유출 금지
- 1장당 30원, 1인당 **11,513**장
- 진행 중 **검은색 또는 단색 화면**이거나 **이상한 사진일 경우(일부가 잘린 사진 등)** 레이블링 없이 다음 이미지 진행 (**정산 제외**)
- 잘 모르겠는 상황에서는 소통방 이용 (카카오톡 예정, 직접적인 업로드 이미지 불가)