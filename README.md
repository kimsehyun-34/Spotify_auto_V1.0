# Spotify_auto_V1.0
Spotify automatically adds to library program using CSV.
CSV를 이용하는 Spotify 자동으로 라이브러리에 추가 프로그램

<div>
  <img style="float:left" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" width="auto" height="40" />
</div>

-----

다른 음악 플랫폼에서 스포티파이로 플랫폼을 변경할때 가장귀찮은 작업인 라이브러리 이전작업을 좀더 쉽게 자동화 해주는 프로그램.
(2024년 6월 1일 기준 정상작동)

-----

- 파이썬 과 파이썬의 라이브러리 `pandas`와 `selenium`이 설치 되있어야 작동함
- 예제 파일(2022 - 1.csv)을 참조하여 주가하고자 하는 음악리스트 재작
  > (csv파일에서 가장위에 있는 음악은 자신의 리스트의 가장아래에 있는 음악이여야함)
- main.py의 33번줄 `data = pd.read_csv('2020-1.csv')`의 파일이름 수정 (ex `data = pd.read_csv('자신이 만든 파일이름.csv')`)
- main.py 실행
