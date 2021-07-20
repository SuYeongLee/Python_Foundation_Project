# 패키지

# 방법 1 - 모듈 X 패키지 묶음으로 점이 안으로 들어간다는 것
import game.sound.echo
game.sound.echo.echo_test()

# 방법 2 - form 게임의 사운드라는 폴더 안쪽에 있는 에코라는 모듈만 불러오겠다.
from game.sound import echo
echo.echo_test()


# 방법 3 - from game이라는 패키지 안에 sound라는 폴더 안에 echo라는 걸 불러와서
# 그 중에서 import echo_test라는 함수만 불러와서 사용하겠다.

from game.sound.echo import echo_test
echo_test()

# 방법 4 - from 패키지 경로 import 함수 as 이름변경

from game.sound.echo import echo_test as e
e()

# 방법 5 - from 패키지 경로 import * <- 전부 불러온다.
from game.sound import *
echo.echo_test()

# relative 패키지 - render.py 참고
from game.graphic.render import render_test
render_test()