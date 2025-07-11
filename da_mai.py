import time
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import fake_useragent
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class DamaiTicketAssistant:
    def __init__(self):
        # 初始化用户代理
        self.user_agent = fake_useragent.UserAgent().random
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        
        # 抢票配置
        self.target_url = "https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_0.208d23e1shtSLE&id=944838388752"
        self.target_performance = ""
        self.ticket_price = "108"
        self.ticket_count = 1
        self.login_status = False
        self.running = False
        
        # 创建GUI界面
        self.create_gui()

    def create_gui(self):
        """创建图形用户界面"""
        self.root = tk.Tk()
        self.root.title("大麦网抢票助手 v1.0")
        self.root.geometry("680x550")
        self.root.resizable(False, False)
        
        # 设置主题
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Microsoft YaHei", 9))
        style.configure("TButton", font=("Microsoft YaHei", 9))
        style.configure("Title.TLabel", font=("Microsoft YaHei", 16, "bold"), foreground="#e53935")
        
        # 标题
        title_frame = ttk.Frame(self.root)
        title_frame.pack(pady=10, fill="x")
        title_label = ttk.Label(title_frame, text="大麦网抢票助手", style="Title.TLabel")
        title_label.pack()
        
        # 配置区域
        config_frame = ttk.LabelFrame(self.root, text="抢票配置")
        config_frame.pack(padx=20, pady=10, fill="x")
        
        ttk.Label(config_frame, text="演出URL:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.url_entry = ttk.Entry(config_frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.url_entry.insert(0, "https://www.damai.cn/show/")
        
        ttk.Label(config_frame, text="演出名称:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.performance_entry = ttk.Entry(config_frame, width=30)
        self.performance_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.performance_entry.insert(0, "7.25霉霉专场「Lover限定」Taylor Swift金曲演唱会")
        
        ttk.Label(config_frame, text="票档选择:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.price_combobox = ttk.Combobox(config_frame, values=["现场108元", "vip188元"], width=15)
        self.price_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.price_combobox.current(2)
        
        ttk.Label(config_frame, text="购票数量:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.count_spinbox = ttk.Spinbox(config_frame, from_=1, to=4, width=5)
        self.count_spinbox.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.count_spinbox.set(2)
        
        # 登录区域
        login_frame = ttk.LabelFrame(self.root, text="账户信息")
        login_frame.pack(padx=20, pady=10, fill="x")
        
        ttk.Label(login_frame, text="手机号:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = ttk.Entry(login_frame, width=20)
        self.phone_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(login_frame, text="密码:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.password_entry = ttk.Entry(login_frame, width=20, show="*")
        self.password_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        self.login_btn = ttk.Button(login_frame, text="登录", command=self.mock_login, width=10)
        self.login_btn.grid(row=0, column=4, padx=10, pady=5)
        
        # 控制按钮
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=15)
        
        self.start_btn = ttk.Button(btn_frame, text="开始抢票", command=self.start_ticket, width=15)
        self.start_btn.pack(side="left", padx=10)
        
        self.stop_btn = ttk.Button(btn_frame, text="停止", command=self.stop_ticket, width=15, state="disabled")
        self.stop_btn.pack(side="left", padx=10)
        
        # 日志区域
        log_frame = ttk.LabelFrame(self.root, text="操作日志")
        log_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        self.log_area = scrolledtext.ScrolledText(log_frame, width=80, height=12, font=("Consolas", 9))
        self.log_area.pack(padx=10, pady=10, fill="both", expand=True)
        self.log_area.configure(state="disabled")
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        status_bar.pack(side="bottom", fill="x")
        
        # 初始化日志
        self.log_message("大麦网抢票助手已启动")
        self.log_message("请先配置抢票信息并登录账户")
        
    def log_message(self, message):
        """在日志区域添加消息"""
        self.log_area.configure(state="normal")
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_area.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_area.see(tk.END)
        self.log_area.configure(state="disabled")
        self.root.update()
    
    def update_status(self, message):
        """更新状态栏"""
        self.status_var.set(message)
        self.root.update()
    
    def mock_login(self):
        """模拟登录过程"""
        phone = self.phone_entry.get()
        password = self.password_entry.get()
        
        if not phone or not password:
            messagebox.showerror("错误", "请输入手机号和密码")
            return
            
        self.log_message(f"尝试登录: 手机号 {phone}")
        self.update_status("登录中...")
        
        # 模拟登录请求
        time.sleep(1.5)
        
        # 模拟登录成功
        self.login_status = True
        self.log_message("登录成功！")
        self.log_message("已获取用户信息")
        self.update_status("登录成功")
        
        # 更新UI
        self.login_btn.configure(text="已登录", state="disabled")
        self.phone_entry.configure(state="disabled")
        self.password_entry.configure(state="disabled")
    
    def start_ticket(self):
        """开始抢票流程"""
        if not self.login_status:
            messagebox.showerror("错误", "请先登录账户")
            return
            
        self.target_url = self.url_entry.get()
        self.target_performance = self.performance_entry.get()
        self.ticket_price = self.price_combobox.get()
        self.ticket_count = int(self.count_spinbox.get())
        
        if not self.target_url or not self.target_performance:
            messagebox.showerror("错误", "请填写演出URL和名称")
            return
            
        self.running = True
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        
        self.log_message("="*60)
        self.log_message(f"开始抢票: {self.target_performance}")
        self.log_message(f"目标票档: {self.ticket_price}, 数量: {self.ticket_count}")
        self.log_message("="*60)
        
        # 启动抢票线程
        self.root.after(100, self.ticket_process)
    
    def stop_ticket(self):
        """停止抢票"""
        self.running = False
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.log_message("抢票已停止")
        self.update_status("已停止")
    
    def ticket_process(self):
        """抢票主流程"""
        if not self.running:
            return
            
        try:
            # 模拟访问演出页面
            self.log_message("正在访问演出页面...")
            self.update_status("获取演出信息...")
            time.sleep(random.uniform(0.5, 1.2))
            
            # 模拟选择日期和场次
            self.log_message("正在选择场次...")
            self.update_status("选择场次...")
            time.sleep(random.uniform(0.3, 0.8))
            
            # 模拟选择票档
            self.log_message(f"正在选择票档: {self.ticket_price}")
            self.update_status("选择票档...")
            time.sleep(random.uniform(0.2, 0.6))
            
            # 模拟选择数量
            self.log_message(f"正在选择数量: {self.ticket_count}")
            self.update_status("选择数量...")
            time.sleep(random.uniform(0.1, 0.4))
            
            # 模拟提交订单
            self.log_message("正在提交订单...")
            self.update_status("提交订单...")
            time.sleep(random.uniform(0.8, 1.5))
            
            # 模拟处理验证
            self.log_message("正在处理安全验证...")
            self.update_status("安全验证...")
            time.sleep(random.uniform(1.0, 2.0))
            
            # 随机结果
            success = random.random() > 0.7  # 30%的成功率
            
            if success:
                self.log_message(">>> 恭喜！抢票成功！<<<")
                self.log_message(">>> 请尽快完成支付 <<<")
                self.update_status("抢票成功！请完成支付")
                
                # 播放成功音效
                self.root.bell()
                
                # 停止抢票
                self.running = False
                self.start_btn.configure(state="normal")
                self.stop_btn.configure(state="disabled")
            else:
                self.log_message("票已售罄，正在重试...")
                self.update_status("重试中...")
                self.root.after(500, self.ticket_process)  # 0.5秒后重试
        
        except Exception as e:
            self.log_message(f"发生错误: {str(e)}")
            self.log_message("5秒后重试...")
            self.root.after(5000, self.ticket_process)

# 启动应用
if __name__ == "__main__":
    app = DamaiTicketAssistant()
    app.root.mainloop()