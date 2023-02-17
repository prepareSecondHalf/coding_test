# git 기본 사용법

1. 본인 컴퓨터에 작업할 폴더 하나 만들어 주시고 터미널에서 cd명령어(change directory) 를 사용해 해당 폴더로 이동 (Ex. C://Users -> C://Users/repo/test 이면 cd repo/test)

2. git clone https://github.com/prepareSecondHalf/coding_test.git

3. git checkout -b 브랜치이름 (Ex. git checkout -b jehyuk)

4. 본인 브랜치 확인 : git branch 색 들어온 곳(main or master 사용 금지, 반드시 본인 branch 에서 작업)

5. 개인 작업

6. git add .

7. git commit -m "커밋 메세지(작업한 내용을 그냥 글로 작성)" (Ex. git commit -m "파이썬 문법")

8. git push origin 브랜치이름 (Ex. git push origin jehyuk)

9. 이후 5~8 반복
