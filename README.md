# FastAPI-DEV

## 프로젝트 소개

FastAPI-DEV 프로젝트는 Python의 FastAPI 프레임워크를 활용하여 API 서버를 개발하는 예제 프로젝트입니다. 기존에 크롤링으로 수집된 데이터 및 Reddit API를 통해 추가 확보한 데이터를 FastAPI 엔드포인트와 연동하여,
* 데이터 요청(조회)
* 데이터 적재(저장) 등을 구현합니다. 또한 Jenkins와 컨테이너 환경(Docker 등)을 사용하여 CI/CD 파이프라인을 구축해 자동 배포를 목표로 합니다.
## 주요 기능

* FastAPI 엔드포인트를 통한 데이터 조회 및 저장
* Reddit API와 연동한 데이터 크롤링/저장 기능
* jenkins 기반 CI/CD 환경 설정
* Docker 컨테이너 자동 빌드 및 배포
## 개발 환경

* 개발 언어 : python 3.12
* 프레임워크 : FastAPI
* ORM : SQLAlchemy
* jenkins, Docker
계속 진행하면서 README파일 업데이트 예정
