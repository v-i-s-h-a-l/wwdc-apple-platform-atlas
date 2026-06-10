---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 2400
---

# MLX And Local Models
> Feature-level research page for MLX And Local Models.

## Entries

- [2026 339 - Bring An LLM Provider To The Foundation Models Framework](../sessions/wwdc2026-339-bring-an-llm-provider-to-the-foundation-models-framework.md) - `deep-researched`
- [2026 325 - Dive Into Core AI Model Authoring And Optimization](../sessions/wwdc2026-325-dive-into-core-ai-model-authoring-and-optimization.md) - `deep-researched`
- [2026 233 - Explore Distributed Inference And Training With MLX](../sessions/wwdc2026-233-explore-distributed-inference-and-training-with-mlx.md) - `deep-researched`
- [2026 328 - Explore Numerical Computing In Swift With MLX](../sessions/wwdc2026-328-explore-numerical-computing-in-swift-with-mlx.md) - `deep-researched`
- [2026 326 - Integrate On-Device AI Models Into Your App Using Core AI](../sessions/wwdc2026-326-integrate-on-device-ai-models-into-your-app-using-core-ai.md) - `deep-researched`
- [2026 330 - Optimize Custom Machine Learning Operations With Metal Tensors](../sessions/wwdc2026-330-optimize-custom-machine-learning-operations-with-metal-tensors.md) - `deep-researched`
- [2026 232 - Run Local Agentic AI On The Mac Using MLX](../sessions/wwdc2026-232-run-local-agentic-ai-on-the-mac-using-mlx.md) - `deep-researched`
- [2026 241 - What's New In The Foundation Models Framework](../sessions/wwdc2026-241-what-s-new-in-the-foundation-models-framework.md) - `deep-researched`
- [2025 308 - Optimize Cpu Performance With Instruments](../sessions/wwdc2025-308-optimize-cpu-performance-with-instruments.md) - `deep-researched`
- [2025 298 - Explore Large Language Models On Apple Silicon With MLX](../sessions/wwdc2025-298-explore-large-language-models-on-apple-silicon-with-mlx.md) - `metadata-only`
- [2025 315 - Get Started With MLX For Apple Silicon](../sessions/wwdc2025-315-get-started-with-mlx-for-apple-silicon.md) - `metadata-only`

## Synthesis

### What This Page Can Answer

- Whether this feature area appears in the indexed WWDC corpus.
- Which sessions and Apple documentation links are relevant.
- Which claims are backed by deep-researched session notes versus metadata-only indexing.

### Evidence-Backed Claims

- Extend the foundation models framework by implementing a languagemodelexecutor for new models. explore how to interface with the languagemodelsession's transcript, manage session state effectively, and optimize kv cache utilization. find out how to support custom segment types and unlock advanced capabilities for your generative ai features. Source: WWDC 2026 session 339.
- Dive into the complete custom model deployment workflow for apple silicon with the new core ai framework. discover powerful techniques for authoring models using custom metal kernels, alongside platform-aware compression strategies. the new core ai debugger offers deep intrinsic analysis, and ai-assisted workflows guide you from initial concept to optimized on-device execution. Source: WWDC 2026 session 325.
- MLX distributed workflows scale inference and fine-tuning across multiple Macs with cluster configuration and distributed communication. Source: WWDC 2026 session 233.
- The session covers model parallelism, pipeline parallelism, request batching, LoRA fine-tuning, and all-reduce APIs. Source: WWDC 2026 session 233.
- MLX numerical computing in Swift brings array-oriented model and math workflows closer to Apple-platform application code. Source: WWDC 2026 session 328.
- The session is relevant when agents need to reason about Swift-native ML prototyping instead of Python-only pipelines. Source: WWDC 2026 session 328.
- Discover a curated collection of popular open-source models — including qwen, mistral, sam3, and more — optimized for apple silicon using the new core ai framework. learn how to download, run, and benchmark models on your mac, and integrate them into your app with just a few lines of code. explore a new workflow for model compilation and on-device specialization to speed up first-time model load. find out how to profile and optimize runtime performance with core ai tools in xcode. Source: WWDC 2026 session 326.
- Metal tensors target custom machine-learning operation performance where higher-level frameworks are insufficient. Source: WWDC 2026 session 330.
- The session belongs in the low-level optimization path for Core AI, MLX, and custom model operations. Source: WWDC 2026 session 330.
- Local agentic AI on Mac combines MLX, Mac hardware, local model serving, and code agents such as opencode for private/offline workflows. Source: WWDC 2026 session 232.
- The agentic loop covers chat, tool integration, Xcode integration, local server setup, and performance tuning. Source: WWDC 2026 session 232.
- Explore what's new in the foundation models framework. learn how to access private cloud compute, integrate third-party and open source models, and work with vision capabilities. discover context management apis, built-in semantic search, and powerful primitives for creating agentic experiences in your apps. Source: WWDC 2026 session 241.

### Related APIs And Concepts

- ANE
- AllReduce
- AppleSilicon
- Arrays
- BNNS
- BarcodeReaderTool
- CGImage
- CLI
- CPUs
- CoreAILanguageModel
- CustomMLOperations
- DEtection
- DistributedCommunication
- DistributedInference
- DynamicProfile
- EAGER
- EXECutor
- EXECutors
- FFTs
- FP4
- FP8
- FineTuning
- GPT
- GRAPH
- GitHub
- INFINITY
- JACCL
- KMeansPalettizer

## Small Observations (Don't Delete)

- This is a neutral feature page, not a recommendation to adopt the feature.
- Prefer deep-researched sessions for strong answers.
- Verify beta SDK names before turning research into code.

<!-- docbot: end -->
