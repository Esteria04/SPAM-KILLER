from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
import timeit
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


### settings ###
youtube = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253Ffeature%253Dyoutu.be&hl=ko&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
modeA = "https://www.youtube.com/feed/trending"
#acntId = input("구글 이메일을 입력해 주세요: ")  # 구글 아이디 할당
#acntPw = input("비밀번호를 입력해 주세요: ")    # 구글 비밀번호 할당
programMode = input("인기동영상 전체의 댓글 정리를 원하시면 A, 특정 동영상의 댓글 정리를 원하시면 B를 입력해 주세요: ")
driver = webdriver.Chrome(r"C:\Users\huiju\Desktop\2021년\Programming\spamkiller\chromedriver.exe")
driver.get(youtube)
action = ActionChains(driver)
### functions settings ###
def preSetting():
    driver.execute_script('document.getElementsByTagName("video")[0].pause()') #일시정지 구현 완료, 음소거 미구현
def scrolling():
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
            
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
def replyCtrl():
    replies = driver.find_elements_by_xpath('//*[@id="more-replies"]')
    moreReplies = driver.find_elements_by_xpath('//*[@id="continuation"]/yt-next-continuation/tp-yt-paper-button')
    for reply in replies:
        try:
            reply.click()
        except:
            pass
    for rep in moreReplies:
        try:
            rep.click()
        except:
            pass
    
    print("reply function complete")
def userFilter():
    nickname = driver.find_elements_by_xpath("//*[@id='author-text']/span") # the comment writers
    Comments = driver.find_elements_by_xpath('//*[@id="content-text"]') # the comment text
    nameText = ["신고자"]#["구독", "채널", "체널", "팔아서", "돈벌기", "누르지 마세요", "자세히 보기", "찍기", "내 채널 들어오면 큰일남"]
    cmtText = ["자세히보기를 누르지", "↰", "↖", "⇖", "←", "쭈물", "조물", "주물", "들어오지 마세요", "내 채널에", "BIJ", "비제이", "핫한 여캠", "韩国是中国的属国", "영상 원본은 내 채널에 있음"]
    while Comments:
        for text in cmtText:
            spmTexts = driver.find_elements_by_partial_link_text(text)
            for spmText in spmTexts:
                txtParent = spmText.find_element_by_xpath('../..').find_element_by_xpath('../..').find_element_by_xpath('./..')
                t_actMenu = txtParent.find_element_by_id('action-menu')
                b = t_actMenu.find_element_by_tag_name('ytd-menu-renderer')
                t_menuBtn = b.find_element_by_tag_name('yt-icon-button')
                action.move_to_element(t_menuBtn).click(on_element=None).perform()
                time.sleep(0.4)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentWrapper"]/ytd-menu-popup-renderer'))).click()
                time.sleep(1.3)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yt-options-renderer-options"]/tp-yt-paper-radio-button[1]'))).click()
                submit = driver.find_element_by_id('submit-button')
                time.sleep(1.2)
                submit.click()
                time.sleep(3)
                confirm = driver.find_element_by_id('confirm-button')
                time.sleep(0.2)
                confirm.click()
                if spmTexts == []:
                    break
                else: 
                    continue
            break
        break
    
    while nickname:
        for name in nameText:
            spmUsers = driver.find_elements_by_partial_link_text(name)
            for spmUser in spmUsers:
                parent = spmUser.find_element_by_xpath('../..').find_element_by_xpath('../..').find_element_by_xpath('../..')
                actMenu = parent.find_element_by_id("action-menu")
                a = actMenu.find_element_by_tag_name("ytd-menu-renderer")
                menuBtn = a.find_element_by_tag_name("yt-icon-button")
                action.move_to_element(menuBtn).click(on_element=None).perform()
                time.sleep(0.4)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentWrapper"]/ytd-menu-popup-renderer'))).click()
                time.sleep(1.3)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yt-options-renderer-options"]/tp-yt-paper-radio-button[1]'))).click()
                submit = driver.find_element_by_id('submit-button')
                time.sleep(1.2)
                submit.click()
                time.sleep(3)
                confirm = driver.find_element_by_id('confirm-button')
                time.sleep(0.2)
                confirm.click()
            break
        break
    print("user filter function complete")

idInput = driver.find_element_by_xpath('//*[@id="identifierId"]')
idInput.send_keys("functionuseitem2021")   # inputting google id
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()    # clicking next
time.sleep(3)
pwInput = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pwInput.send_keys("sine30deg")
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
### Mode A ###
if programMode =='A':
    print("모드 A 가 활성화 되었습니다")
    driver.get(modeA)
    vidList = driver.find_elements_by_class_name("style-scope ytd-video-renderer")
    for vid in vidList:
        vid.click()
        scrolling()
        replyCtrl()
### Mode B ###
if programMode == 'B':
    print("모드 B가 활성화 되었습니다")
    time.sleep(2)
    #modeB = input("댓글 정리를 원하시는 영상의 url을 입력해 주세요: ")
    modeB = "https://www.youtube.com/watch?v=YFapIjhV82c"
    driver.get(modeB)
    time.sleep(3)
    preSetting()
    scrolling()
    print("댓글 탐색을 시작합니다")
    time.sleep(1)
    print("댓글 탐색중...")
    time.sleep(3)
    replyCtrl()
    print("댓글 탐색 완료")
    time.sleep(1)
    print("댓글 정리 시작")
    time.sleep(1)
    print("댓글 정리중...")
    userFilter()
    print("댓글 정리 완료")