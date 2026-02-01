# OpenBB 开放数据平台 - 桌面应用程序

ODP 桌面应用程序通过降低技术门槛来增强开发者体验，用于构建、展示和共享数据管道、洞察或多界面仪表板体验。

此代码库代表 OpenBB 发布的开放数据平台（ODP）桌面应用程序和系统托盘图标的完整源代码。

分发的二进制文件（目前为 macOS 和 Windows）是此仓库中构建操作的直接输出，负责生成发布工件。

请注意，虽然没有 Linux 分发的构建管道，但可以在本地构建和安装。

## 从源码构建和运行

### 环境要求

- **Rust** 1.90.0+
- **Node.js** 和 **NPM**
- **OpenSSL**

### 1. 安装 Rust

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

如果已安装 Rust，更新到最新版本：

```sh
rustup update
```

### 2. 安装 Node.js

按照 [此处](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) 的说明安装。

如果已有 `npm`，请在安装项目前更新：

```bash
npm install -g npm
```

### 3. 安装 OpenSSL

系统必须安装 OpenSSL，并设置以下环境变量：

```env
OPENSSL_DIR
OPENSSL_INCLUDE_DIR
OPENSSL_LIB_DIR
```

### 4. 安装项目依赖

在 `/desktop` 根文件夹下运行：

```sh
npm install
```

### 5. 启动开发服务器

```sh
npm run tauri dev
```

这将启动开发服务器并监视代码库的更改。大多数更改会被自动检测，但某些事件可能需要完全重启。

如果使用浏览器而非窗口查看开发服务器，某些功能将无法工作。这是预期的行为。

目前请忽略所有警告消息，我们稍后会清理。

## 技术栈

ODP Desktop 使用 Tauri & React 框架构建，代码大约是 50/50 的 Rust/TypeScript。

此技术栈通过依赖操作系统进行窗口创建来减少分发大小。安装后大约 35 MB；压缩后 12 MB。

该应用程序是托盘图标 - 后台服务 - 功能依赖于通过 ODP 单独安装的开发者工具。

换句话说，应用程序本身是与操作系统和命令行交互的 GUI 和包装器。

### 核心功能

- **环境管理**: 通过 Miniforge/Conda 管理 Python 环境
- **后端服务**: 启动/停止 ODP 后端 API
- **API 密钥管理**: 图形化配置数据提供商凭证
- **Jupyter 集成**: 启动 Jupyter Lab IDE

## 项目结构

```
desktop/
├── src/                    # 前端源码 (React + TypeScript)
│   ├── components/         # React 组件
│   ├── routes/             # 页面路由
│   └── tests/              # 测试文件
├── src-tauri/              # Tauri (Rust) 源码
│   ├── src/
│   │   ├── tauri_handlers/ # 命令处理器
│   │   └── utils/          # 工具模块
│   └── icons/              # 应用图标
└── package.json
```

## 推荐的 VS Code 扩展

- rust-analyzer
- Tauri
- Tailwind CSS IntelliSense

## 构建生产版本

生产构建计划通过 GitHub Actions 完成和签名。官方发布结构之外的构建可能需要调整 `beforeBundleCommand`。

## 开发指南

[Desktop 模块详解](../docs/knowledge/05-desktop-module.md)

## 许可证

参见 [LICENSE](../LICENSE)
