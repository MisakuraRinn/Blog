
# Django Blog Project

本项目是一个基于 **Django** 框架实现的博客系统，用于完成课程 Project 19（19-1 / 19-5）的实验要求。  
系统支持博客发布、评论交互、用户权限控制，并在此基础上扩展了 **Markdown 内容渲染** 与 **Live2D 页面美化** 功能。

GitHub 仓库地址：  
? https://github.com/MisakuraRinn/Blog

---

## 一、项目功能概述

### 1. 博客系统（Project 19-1）

- 创建 Django 项目 `Blog`，应用 `blogs`
- 核心模型 `BlogPost`，包含：
  - `title`：博客标题
  - `text`：博客正文
  - `date_added`：创建时间
  - `owner`：博客作者
- 使用 Django Admin 后台创建与管理博客
- 首页按时间顺序展示所有博客文章
- 提供博客创建与编辑表单

---

### 2. 评论系统（Entry 模型）

- 在 `blogs` 应用中实现评论模型 `Entry`
- `Entry` 模型字段：
  - `topic`：关联的博客文章
  - `text`：评论内容
  - `date_added`：评论时间
  - `owner`：评论发布者
- 支持多个用户对同一博客进行评论
- 评论内容与博客详情页一并展示

---

### 3. 用户与权限控制（Project 19-5）

- 所有用户均可浏览博客与评论
- 仅注册并登录的用户可以：
  - 发布博客
  - 发布评论
- 权限约束规则：
  - **仅博客作者可以编辑自己的博客**
  - **仅评论发布者可以编辑自己的评论**
- 在视图函数中对用户身份进行校验，防止非法修改他人内容

---

## 二、扩展功能说明（Bonus）

### 1. Markdown 内容支持

- 博客正文与评论内容均支持 Markdown 语法
- 页面渲染时自动将 Markdown 转换为 HTML
- 支持：
  - 代码块
  - 列表
  - 表格
  - 粗体 / 斜体文本

该功能显著提升了博客内容的表达能力与可读性。

---

### 2. Live2D 动漫角色集成

- 在博客页面侧边栏中集成 Live2D 动漫角色
- 页面加载后自动显示
- 不影响正文阅读，仅作为界面美化与交互增强

---

## 三、项目结构说明

```text
Blog/
├─ Blog/                 # Django 项目配置
├─ blogs/                # 博客应用
│  ├─ models.py          # BlogPost 与 Entry 模型
│  ├─ views.py           # 视图逻辑（权限校验）
│  ├─ forms.py           # 博客与评论表单
│  ├─ templates/         # HTML 模板
│  └─ urls.py
├─ accounts/
├─ static/               # 静态资源（CSS / JS / Live2D）
├─ manage.py
└─ README.md
```

---

## 四、运行环境与依赖

* Python 3.x
* Django 6.0
* SQLite3（默认数据库）

---

## 五、运行方式

1. 克隆仓库

```bash
git clone https://github.com/MisakuraRinn/Blog.git
cd Blog
```

2. 创建并激活虚拟环境（可选）

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. 安装依赖

```bash
pip install django
```

（若项目中包含 `requirements.txt`，可使用 `pip install -r requirements.txt`）

4. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

5. 创建超级用户（用于 Admin 后台）

```bash
python manage.py createsuperuser
```

6. 启动开发服务器

```bash
python manage.py runserver
```

7. 访问项目

* 博客首页：[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* 管理后台：[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 六、说明

* 本项目为课程实验用途，重点在于 Django 基础功能、用户权限控制与扩展功能实现
* Markdown 与 Live2D 为在完成基础要求后的功能扩展
* 代码结构清晰，便于复现实验结果

---

## 七、作者

* 作者：MisakuraRinn
* 用途：课程 Project 19 实验作业