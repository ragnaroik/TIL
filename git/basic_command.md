# git command



## 설정

### init

* ```git init```
* 폴더를 git으로 관리하기 위해 .git 폴더를 생성
* 최초 한번만 실행하면 됨



### status

* ```git status```
* 현재 git의 상태를 출력



### log

* ```git log```
* 현재 쌓여있는 commit history 출력



### diff 

* ```git diff```
* 마지막 commit과 지금 working directory 상태 비교



### remote add

* ```git remote add <별명> <주소>```
* 원격저장소 주소 등록



## 조작

### add

* ```git add [filename]```
* ```[filename]``` 이 ```.``` 인 경우 전체 파일이 추가됨
* working directory의 파일을 staging area(INDEX)에 업로드



### commit

* ```git commit``` 
  * ```git commit -m [mention]``` : commit시에 mention 추가
* staging area에 올라간 파일들을 스냅샷으로 저장



### push

* git push [repo name] [branch name]
  * git push origin master
* commit history를 원격 저장소에 업로드