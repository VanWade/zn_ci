# zn_ci
### 介绍
创建一个 post-receive hook 来监听远程仓库，一旦有代码更新就提交一个任务给
celery,celery worker 负责拉取最新代码到本地仓库并执行 unittests
### 创建仓库
* 远程仓库

```
mkdir test_repo
cd test_repo
git init --bare
```
* 本地开发仓库
```bash
git clone test_repo test_repo_dev
```
* 本地 CI 仓库
```bash
git clone test_repo test_repo_ci
```

### 添加 post-receive hook
* 把 post-receive 文件拷贝到 test_repo/hook/

### 关于 celery
* 安装 redis 作为 celery broker
* 把 tasks.py 也拷贝到 test_repo/hooks
* 执行 celery worker `celery -A tasks worker --loglevel=info`

### 修改代码触发单元测试
* 修改 test_repo_dev 中的代码并提交