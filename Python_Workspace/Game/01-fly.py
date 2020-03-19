import pygame
import random
import math


# 初始化界面
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 设置标题
pygame.display.set_caption("飞机大战")

# 设置图标
icon = pygame.image.load("./resource/ufo.png")
pygame.display.set_icon(icon)

# 设置背景
bgImg = pygame.image.load("./resource/bg.png")

# 添加背景音效
pygame.mixer.music.load("./resource/bg.wav")
# -1表示循环播放
pygame.mixer.music.play(-1)

# 添加射中的音效
sound = pygame.mixer.Sound("./resource/exp.wav")

# 设置分数
score = 0
# 设置分数显示的字体(使用pygame自带的字体文件)
font = pygame.font.Font("freesansbold.ttf", 32)

# 设置飞机
playerImg = pygame.image.load("./resource/player.png")
# 设置飞机的坐标
playerX = 400
playerY = 500
playerStep = 0

# 判断游戏结束
is_over = False
# 设置游戏结束时显示的字体
over_font = pygame.font.Font("freesansbold.ttf", 64)

# 添加多个敌人
numbers_of_enemies = 6
class Enemy():
    """敌人类"""
    def __init__(self):
        self.img = pygame.image.load("./resource/enemy.png")
        # 随机化敌人的位置
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(1, 4)
    
    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 200)


enemies = []
for i in range(numbers_of_enemies):
    enemies.append(Enemy())


# 设置子弹
class Bullet():
    """子弹类"""
    def __init__(self):
        self.img = pygame.image.load("./resource/bullet.png")
        self.x = playerX + 16  # 子弹的x坐标和飞机的一致 +16是为了从飞机中间发射
        self.y = playerY + 10  # 子弹的y坐标略大于飞机的y坐标
        self.step = 10
    
    def hit(self):
        global score
        for enemy in enemies:
            if (distance(self.x, self.y, enemy.x, enemy.y) < 25):
                # 击中敌人
                sound.play( )
                bullets.remove(self)
                # 重置敌人位置
                enemy.reset()
                score += 1


# 保存子弹
bullets = []


def distance(bx, by, ex, ey):
    """计算子弹和敌人之间的欧氏距离"""
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)


def show_bullets():
    """显示子弹"""
    for bullet in bullets:
        screen.blit(bullet.img, (bullet.x, bullet.y))
        # 判断是否击中
        bullet.hit()
        bullet.y -= bullet.step
        # 子弹超出边界时，移除这个子弹
        if bullet.y < 0:
            bullets.remove(bullet)


def show_enemy():
    """显示敌人"""
    global is_over
    for enemy in enemies:
        screen.blit(enemy.img, (enemy.x, enemy.y))
        enemy.x += enemy.step
        if enemy.x > 736 or enemy.x < 0:
            # 让敌人左右移动
            enemy.step *= -1
            enemy.y += 120
            if enemy.y > 450:
                is_over = True
                # 游戏结束，清空敌人
                enemies.clear()


def show_score():
    """显示得分"""
    text = "Score:{}".format(score)
    # 渲染字符
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (0, 0))


def check_is_over():
    """显示游戏结束提示"""
    if is_over:
        text = "Game Over!"
        # 渲染字符
        over_render = over_font.render(text, True, (255, 0, 0))
        screen.blit(over_render, (200, 250))


def process_event(running):
    """处理事件"""
    global playerStep
    for event in pygame.event.get():
        # 判断是否要退出(QUIT表示点叉退出)
        if event.type == pygame.QUIT:
            running = False
        
        # 判断键盘是否按下
        if event.type == pygame.KEYDOWN:
            # 按下右方向键
            if event.key == pygame.K_RIGHT:
                playerStep = 5
            # 按下左方向键
            elif event.key == pygame.K_LEFT:
                playerStep = -5
            # 按下空格键发射子弹
            elif event.key == pygame.K_SPACE:
                # 创建一颗子弹
                bullets.append(Bullet())
            
        # 判断键盘是否抬起
        if event.type == pygame.KEYUP:
            playerStep = 0
    return running


def move_player():
    """移动飞机"""
    global playerX
    playerX += playerStep
    # 飞机是64x64的，所以边界是736
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

def main():
    # 游戏主循环
    running = True
    while running:
        # 显示背景(从坐标(0,0)(左上角)开始画背景)
        screen.blit(bgImg, (0,0))

        # 显示分数
        show_score()

        # 处理事件
        running = process_event(running)
        
        # 显示飞机，设置飞机位置
        screen.blit(playerImg, (playerX, playerY))

        # 移动飞机，控制飞机不出边界
        move_player()

        # 显示敌人
        show_enemy()

        # 显示子弹
        show_bullets()

        # 显示游戏结束
        check_is_over()

        # 更新屏幕，显示背景
        pygame.display.update()


if __name__ == "__main__":
    main()