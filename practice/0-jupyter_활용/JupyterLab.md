<h1 style="text-align:center;"> &lt;Jupyter Lab으로 코딩하기&gt;</h1>
<h2>1. Jupyter Lab란?
    <h3>Jupyter 공식 사이트의 JupyterLab 페이지에서 제일 먼저 보이는 첫 문장</h3>
    <h4 style="color: rgb(80,80,80); font-size: 1.5rem; display: inline-block; padding: 0.5rem 1rem; margin-top: 1rem; background: rgb(230, 230, 230);">JupyterLab is a next-generation web-based user interface for Project Jupyter.<br>...<br>JupyterLab will eventually replace the classic Jupyter Notebook.  </h4><br>
        <span>사이트 -></span><a href="https://jupyterlab.readthedocs.io/en/latest/">https://jupyterlab.readthedocs.io/en/latest/</a><br>
        ※참고 2018년 2월에 발표  <br>
    
<hr>
<h2>2. Lab vs Notebook</h2>
<h3>2-1. 비교</h3>
<ul>
    <li><h3>Interface</h3></li><br>
    <img src="https://jupyterlab.readthedocs.io/en/stable/_images/jupyterlab.png" ><br>
    <p>분리돼 있던 File Browser와 Ipython Notebook이 통합 되었다.</p><br>
    <li><h3>화면 분할</h3></li>
    <img src="https://jupyterlab.readthedocs.io/en/latest/_images/interface_jupyterlab.png"><br><br>
    <p>출처: <a href="https://jupyterlab.readthedocs.io/en/latest/_images/interface_jupyterlab.png">https://jupyterlab.readthedocs.io/en/latest/_images/interface_jupyterlab.png</a></p><br>
    <li><h3>좀 더 편리한 docstring 보기(Tab+Shift)</h3></li>
    <h4 style=" color: navy;">&lt;Notebook ver&gt;</h4>
    <img src="https://postfiles.pstatic.net/MjAxOTA3MThfMTE2/MDAxNTYzNDUzNjg4MDkz.wpQ5pa16MuDs3MRWULOUsZ4dWAtqhtN4WlpqnoGv3mMg.qxfctRa2nswCXeUesqq-8_2_l_nHLwTXfro0eGwr_ssg.JPEG.gyul611/SE-271fc7eb-0504-43a0-a8dc-1efc35fa21e1.jpg?type=w773"><br>
    <p>자세한 정보를 보기 위해서는 한번의 <strong>'클릭'</strong>이 필요하다..(귀찮)</p><br>
    <h4 style=" color: navy;">&lt;Lab ver&gt;</h4>
    <img src="https://postfiles.pstatic.net/MjAxOTA3MThfMTE5/MDAxNTYzNDUzNjg5MzAx.i1O95VUEfzBX4hiAccA0AMD8Pn2J1VG-iEw12QZqP-0g.-2ewD8Xq5MkZNh1n7Ti_WrQZrhz0XLJJN7NDU9pWa-Mg.JPEG.gyul611/SE-096d4e68-c4c9-412e-8e12-bf9f4d0c85d1.jpg?type=w773"><br>
    <p><strong>Tab + Shift</strong>만으로 자세한 정보를 볼 수 있다.</p><br>
</ul>
<ul>
    <li><h3>기본적으로 테마 변경 제공</h3></li>
    <h4>Menu bar -> Settings -> Jupyter Lab theme</h4>
</ul>
<hr>
<br>
<h3>2-2. Lab 설치하기 & 사용</h3>
<ul>
    <li>Anaconda Navigator</li>
    <img src="https://postfiles.pstatic.net/MjAxOTA3MThfNDgg/MDAxNTYzNDUwNTI4MjQy.F_lGcBXwnbn96P9-p2Jdw0xzga8PaJ4yGU7XjI_U7NIg.PZQSy0aorn0gMAXR4C6GsR4_vvcCNw25UOwhX_Vz788g.JPEG.gyul611/navigator.JPG?type=w773">
    <p style="margin-top: 1rem;">jupyter lab <strong>Install</strong> 클릭!</p>
    <li> 터미널에서 설치</li>
    <div style="font-size: 1.5rem; background: rgb(230,230,230); padding: 0.5rem 1rem; margin-top: 0.5rem; display: inline-block;">
        >> pip install jupyterlab<br>  
        >> conda install -c conda-forge jupyterlab<br>
    </div><br><br>
    <li> 실행시키기</li>
    <div style="font-size: 1.5rem;background: rgb(230,230,230); padding: 0.5rem 1rem; margin-top: 0.5rem; display: inline-block;">
        >> jupyter lab
    </div>
</ul>
<hr>
<h2>3. R in Jupyter!</h2>
<h4>Anaconda Prompt에 다음 명령어를 입력한다</h4>
<div style="font-size: 2rem; background: rgb(230,230,230); padding: 0.5rem 1rem; margin-top: 0.5rem; display: inline-block;"> >>conda install -c r r-essentials </div> <br><br>
  
<img src="https://postfiles.pstatic.net/MjAxOTA3MThfMjkz/MDAxNTYzNDI4NzA1Mjc1.GxLv5I3Nae4cI_UpbZDOnynfImF0N6sE6oxzKza83MUg.OC4Z7BrrvWYXpbsqwTF7D99Zo-X867WWvxbiMN77Heog.JPEG.gyul611/SE-65bac0cb-64a8-486c-9150-40d6f320edd7.jpg?type=w773">
<br>
<h4> 설치될 패키지들이 보여진다.</h4>
<img src="https://postfiles.pstatic.net/MjAxOTA3MThfMjkx/MDAxNTYzNDI4NzAyOTI4.TTuIrIOyXYEfYyTRiKeKt9tmlMgIW-WVAbbV7VZWtjAg.5E0IF0qiRwFmO1hIaE9fzBDfG89OgrbB3nGcb9ftbYMg.JPEG.gyul611/SE-db62bab0-015c-49fe-bd16-30143884c8dc.jpg?type=w773" >
<h4><p>Proceed([y/n])?에서 y입력하면 설치가 진행된다.</p></h4>
<img src="https://postfiles.pstatic.net/MjAxOTA3MThfMjIg/MDAxNTYzNDI4NzMyMDcw.IyLzCFy4PW05UU41e04BSa9kssXf3blx-kKG3YaL85gg.4Qg6nt1sAxZn58alwqvFuiyd2voN1HmLLb1Aid31x6Qg.JPEG.gyul611/SE-b9c0a087-506a-4909-b9b5-6b06751cffaa.jpg?type=w773">

<h4>Jupyter에서 R Notebook이 생긴 것을 확인 할 수 있다!</h4>