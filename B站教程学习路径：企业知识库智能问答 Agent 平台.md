# B站教程学习路径：企业知识库智能问答 Agent 平台

> 目标：用 B站公开课把这套技术方案（FastAPI + LangGraph + Qdrant + RAG 评估 + 可观测性 + K8s）从零学通。
> 配套技术方案原文：[AI-Agent项目-技术方案](https://www.workbuddy.cn/space/d/1BYqV52wuv55ndx9G22yEi)

## 怎么用这份清单

- 按阶段顺序推进，每个阶段结束产出一个能跑起来的小模块，而不是只看不写。
- 优先选带配套代码和资料的成套课程（黑马程序员、尚硅谷这类），避免零散单集。
- 项目技术栈以 Python 为主，但你的 Java 工程经验在「状态管理、发布治理、可观测性」这三块可以直接迁移，底层思路不用重学，重点补的是 Python 生态里对应的工具。
- B站视频随时可能下架或转为仅自己可见，这份清单里的每个链接我都按 2026 年 10 月的时间点核验过一遍。如果你打开时发现失效，直接把课程名或 BV 号丢进 B站搜索框即可，不必卡在原地。

## 阶段 0：环境与后端基础（约 1 周）

补 Python 异步编程、Docker、FastAPI，这是后面所有模块的地基。

- **Python 异步与工程化**：黑马程序员 Python 语言进阶 —— [https://www.bilibili.com/video/BV1U2WmzfEqp](https://www.bilibili.com/video/BV1U2WmzfEqp)
  - 重点看 async/await、生成器、类型注解，FastAPI 全程依赖这些。
- **FastAPI 从入门到实战**：黑马程序员 Python Web 开发 —— [https://www.bilibili.com/video/BV1zV2QBtE39](https://www.bilibili.com/video/BV1zV2QBtE39)
  - 覆盖路由、依赖注入、Pydantic、异步编程、ORM、项目拆分、部署、接口测试，是本项目 API 网关层的直接参考。
- **FastAPI 框架全套教程**（B站首发，偏基础原理）—— [https://www.bilibili.com/video/BV1zb421J7LQ](https://www.bilibili.com/video/BV1zb421J7LQ)
- **Docker 实战**：尚硅谷 Docker 实战教程 —— [https://www.bilibili.com/video/BV1HP4118797](https://www.bilibili.com/video/BV1HP4118797)
  - 本项目 MVP 阶段要用 docker-compose 编排 Qdrant、Redis 和服务本体，靠这套打底。

## 阶段 1：RAG 检索链路（核心，约 2-3 周）

这是项目里工作量最大、也最容易被面试官追问的部分。优先看第一套，它的目录几乎覆盖了技术方案中 RAG 数据层的每个要点。

- **【大模型 RAG】RAG 知识库搭建系统教程**（31.8 万播放，66 集 / 11.6 小时）—— https://www.bilibili.com/video/BV1otokBpENn
- 看课顺序：分片、索引、召回、重排、生成（P5-P9）→ 高质量文本分块实战（P10）→ RAG 检索优化上下（P11-P12）→ LangChain 最新版全体系（P13-P27）→ RAG 实战：文档加载、切分、Embedding、向量库、行业知识问答（P28-P34）→ 进阶专题：Re-ranker（P38）、PDF 表格预处理（P39）、历史对话记忆（P40-P41）→ 落地常见问题与「微调 vs RAG」（P42-P46）。P47 之后转入 Agent 篇章，留到阶段 2 再看。
- 这套课的 LangChain 部分是当前最新版 API，和阶段 2 的 LangGraph 属于同一代，术语能直接对上；Re-ranker 和 PDF 表格预处理这两集，正好对应技术方案里最难的两个点。
- **【2025最新AI大模型】RAG 大模型 0 基础全套教程**（77 集 / 14.2 小时，体系最完整的一套）—— https://www.bilibili.com/video/BV1K65LzGEaR
- 这是阶段 1 的深水区教材：稀疏与稠密检索、Query 增强（HyDE、子问题拆解）、多索引增强、融合检索、Re-rank、迭代检索、Self-RAG、Graph RAG 全部有独立章节，技术方案里「混合检索 + RRF + Reranker」这条链路的来龙去脉在这套课里讲得最透。它的第 8 章整章讲 RAG 评估（Ragas 框架 + 实战），所以这套同时是阶段 3 的主教材，可以边学检索边把评估流水线跑起来。
- **【实战教程】全面解析：构建高效企业级 RAG 知识库** —— [https://www.bilibili.com/video/BV13SkiYeEgy](https://www.bilibili.com/video/BV13SkiYeEgy)
  - 偏架构与工程化视角：切片算法与参数优化、向量库选型（Milvus）、Prompt 模板设计、多轮对话实现、会话管理、错误处理与重试机制、向量检索优化、监控与日志、部署前准备。适合跑通 Demo 之后做工程化补课。
- **黑马程序员：大模型 RAG 与 Agent 智能体项目实战**（基于 LangChain）—— [https://www.bilibili.com/video/BV1yjz5BLEoY](https://www.bilibili.com/video/BV1yjz5BLEoY)

**本阶段自检标准**：能用公开财报、技术文档或你自己的博客文章搭出一个可用的知识库，并且能讲清「为什么要混合检索」「Reranker 放在哪一步、为什么只对 Top-N 做」。

## 阶段 2：Agent 编排（LangGraph，约 2 周）

技术方案里 Agent 编排层的关键是先画出状态图：路由节点（判断是否需要检索）→ 检索节点 → 生成节点 → 反思/校验节点。

- **B站讲的最细的 LangGraph 快速入门教程** —— [https://www.bilibili.com/video/BV16gV8zNE9M](https://www.bilibili.com/video/BV16gV8zNE9M)
- **尚硅谷 LangGraph 教程**（85 万播放，132 集 / 21.3 小时）—— https://www.bilibili.com/video/BV1z3NY66EY1
- 这套是阶段 2 的底本：State 的四种实现、reducer 归约、条件边与 Command 路由、循环结构与步数限制、重试与超时控制、checkpointer 持久化（内存与 PostgreSQL 两种）、时间旅行与 fork 全都单独成集。技术方案里「状态图 + Redis 对话状态持久化」可以对着它的持久化章节直接改。
- **LangGraph 入门到精通（构建 Agent 智能体 + RAG 智能客服）** —— [https://www.bilibili.com/video/BV1fBQaYZESC](https://www.bilibili.com/video/BV1fBQaYZESC)
  - 这套里带一节「DeepSeek 大模型企业级 RAG 知识库项目实战」，是少见的把 RAG 与 LangGraph 串成完整项目的课程。
- **智能客服系统搭建全流程实战**（含混合检索、检索后排序、LangGraph 核心组件、GraphRAG）—— [https://www.bilibili.com/video/BV1G2MuzHEVW](https://www.bilibili.com/video/BV1G2MuzHEVW)
- **AI Agent 智能体企业级搭建教程** —— [https://www.bilibili.com/video/BV1de2UBjEzM](https://www.bilibili.com/video/BV1de2UBjEzM)

**看这几套时重点抓**：State 与 checkpointer（对应本项目用 Redis 做对话状态持久化）、条件边与循环、ReAct Agent、Function Calling 接工具、Human-in-the-loop。

## 阶段 3：评估与可观测性（差异化亮点，约 1-2 周）

这两块是技术方案里「区别于 90% 玩具 Demo」的护城河，但 B站上的专题视频偏少，要有「以官方文档为主、视频为辅」的心理准备。

先更正一句：这套课标题里的「评估」只是标题表述，正片里没有评估流水线。我核对了它的完整 86 集分P 目录，涉及评估与可观测性的只有一处：

- 第 26 个分P「25-LangChain入门-实战-对接LangSmith」，约 20 分钟，讲的是在实战项目里对接 LangSmith 做调用追踪——属于可观测性，不涉及数据集、评分器、回归对比。全课没有 RAGAS、LLM-as-Judge、回归阻断发布的任何章节。

真正讲评估流水线的，B站上是另外两套：

- **【2025最新AI大模型】RAG 大模型 0 基础全套教程**（第 8 章整章讲评估；与阶段 1 的深水区教材是同一套，不用重复找课）—— https://www.bilibili.com/video/BV1K65LzGEaR
- 第 8 章路径：8-2「RAG 迭代的关键：评估」→ 8-3「RAG 评估的三大步骤」→ 8-4「RAG 评价神器：Ragas 框架」（约 20 分钟）→ 8-5「实战：用 Ragas 评估制度问答模块的性能」。指标定义、RAGAS 落地、实战一条线走完，是本项目「评估流水线」最直接的教学内容。
- **RAGFlow 系列课程**（第 7 集「RAG 评估：评估指标、RAGAs、TruLens」，约 22 分钟）—— https://www.bilibili.com/video/BV1YkpazWE9v
- 单集把评估指标、RAGAS、TruLens 两个框架横向过一遍，适合当评估工具的速览，不适合当系统课。
- **给 RAG 打分：小白也能懂的 AI 系统评测全攻略**（B站专栏）—— [https://www.bilibili.com/read/mobile?id=43076231](https://www.bilibili.com/read/mobile?id=43076231)
  - Recall@K、MRR、NDCG、忠实性等指标的定义与直觉解释，正好对应本项目要写进简历的「Recall@K 与 LLM-as-Judge」。
- **做了 3 个 RAG 项目，我把召回率从 78% 折腾到了 92%**（B站专栏）—— [https://www.bilibili.com/read/cv50287427](https://www.bilibili.com/read/cv50287427)
  - 换 Embedding → 加混合检索 → 加 Reranker 这条优化链路，是很好的面试叙事素材，可以直接改造成你的评估流水线叙事。
- **Langfuse 本身**：B站没有成体系的自部署教程，建议直接看官方自部署文档（Docker Compose 和 Kubernetes/Helm 两种方式都有）。

## 阶段 4：发布治理与云原生部署（约 2 周）

- **尚硅谷 Kubernetes（k8s）入门到实战教程（新版）** —— [https://www.bilibili.com/video/BV1GT4y1A756](https://www.bilibili.com/video/BV1GT4y1A756)
  - 新版相比旧版增加了项目实战部署：完整演示一个真实项目从零部署到 K8s 集群，包括项目打包、制作镜像、部署过程，正好对应本项目「第 12 周 Helm 多环境」的目标。
  - 风险提示：技术方案里已经写明 K8s 学习容易卡住，对策是 MVP 阶段先用 docker-compose，最后阶段再上 K8s，本地用 Kind 即可。请按这个节奏走，不要提前死磕。
- **尚硅谷 Docker 实战教程** —— [https://www.bilibili.com/video/BV1HP4118797](https://www.bilibili.com/video/BV1HP4118797)
- **Helm 与灰度发布**：B站视频零散，建议以 Helm 官方文档配合 K8s 官方 Deployment/Ingress 文档为主，把「按比例切流」落到 Service + Ingress 的流量切分上。

## 阶段规划速览

- **阶段 0｜环境与后端基础** —— 对应项目模块：API 网关层、部署底座 —— 主推：黑马 FastAPI（BV1zV2QBtE39）+ 尚硅谷 Docker（BV1HP4118797）
- **阶段 1｜RAG 检索链路** —— 对应项目模块：文档摄入管道 + RAG 数据层 —— 主推：RAG 知识库搭建系统教程（BV1otokBpENn）打底 + RAG 0 基础全套教程（BV1K65LzGEaR）做深
- **阶段 2｜Agent 编排** —— 对应项目模块：Agent 编排层 —— 主推：尚硅谷 LangGraph（BV1z3NY66EY1）打底 + LangGraph 构建 Agent 与 RAG 智能客服（BV1fBQaYZESC）串项目
- **阶段 3｜评估与可观测性** —— 对应项目模块：评估流水线 + 可观测性 —— 主推：RAG 全套教程第 8 章（BV1K65LzGEaR）做评估；黑马实战第 26 分P（BV178w1z7EHQ）只用于补可观测性
- **阶段 4｜发布治理与云原生部署** —— 对应项目模块：发布治理 + 基础设施 —— 主推：尚硅谷 K8s（BV1GT4y1A756）

## B站资源的两个缺口

1. **Langfuse 自部署**、**Prompt 版本管理 + 灰度发布的完整落地**：这两块几乎找不到成套视频，官方文档是唯一可靠来源，不要在这上面浪费搜索时间。
2. **Qdrant 的中文视频教程**：B站上以 Milvus、Chroma 为主，Qdrant 多为图文专栏。好消息是 LangChain / LangGraph 里向量库接口高度统一，把 Milvus 或 Chroma 的用法学透之后，换成 Qdrant 主要就是改十几行初始化代码。

## 一句话学习顺序

阶段 0 打地基 → 阶段 1 把 RAG 检索链路做扎实 → 阶段 2 用 LangGraph 把它编成 Agent → 阶段 3 补评估与可观测性做出差异化 → 阶段 4 用 K8s 完成工程化收尾。
