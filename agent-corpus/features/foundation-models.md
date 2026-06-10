---
type: reference
status: published
created: 2026-06-10
updated: 2026-06-10
max_words: 2400
---

# Foundation Models
> Feature-level research page for Foundation Models.

## Entries

- [2026 339 - Bring An LLM Provider To The Foundation Models Framework](../sessions/wwdc2026-339-bring-an-llm-provider-to-the-foundation-models-framework.md) - `deep-researched`
- [2026 242 - Build Agentic App Experiences With The Foundation Models Framework](../sessions/wwdc2026-242-build-agentic-app-experiences-with-the-foundation-models-framework.md) - `deep-researched`
- [2026 334 - Build AI-Powered Scripts With The FM CLI And Python SDK](../sessions/wwdc2026-334-build-ai-powered-scripts-with-the-fm-cli-and-python-sdk.md) - `deep-researched`
- [2026 319 - Build With The New Apple Foundation Model On Private Cloud Compute](../sessions/wwdc2026-319-build-with-the-new-apple-foundation-model-on-private-cloud-compute.md) - `deep-researched`
- [2026 299 - Create Robust Evaluations For Agentic Apps](../sessions/wwdc2026-299-create-robust-evaluations-for-agentic-apps.md) - `deep-researched`
- [2026 243 - Debug And Profile Agentic App Experiences With Instruments](../sessions/wwdc2026-243-debug-and-profile-agentic-app-experiences-with-instruments.md) - `deep-researched`
- [2026 326 - Integrate On-Device AI Models Into Your App Using Core AI](../sessions/wwdc2026-326-integrate-on-device-ai-models-into-your-app-using-core-ai.md) - `deep-researched`
- [2026 246 - LLM Search Using Core Spotlight](../sessions/wwdc2026-246-llm-search-using-core-spotlight.md) - `deep-researched`
- [2026 324 - Meet Core AI](../sessions/wwdc2026-324-meet-core-ai.md) - `deep-researched`
- [2026 298 - Meet The Evaluations Framework](../sessions/wwdc2026-298-meet-the-evaluations-framework.md) - `deep-researched`
- [2026 347 - Secure Your App: Mitigate Risks To Agentic Features](../sessions/wwdc2026-347-secure-your-app-mitigate-risks-to-agentic-features.md) - `deep-researched`
- [2026 241 - What's New In The Foundation Models Framework](../sessions/wwdc2026-241-what-s-new-in-the-foundation-models-framework.md) - `deep-researched`
- [2026 375 - Create High Quality Images Using Image Playground](../sessions/wwdc2026-375-create-high-quality-images-using-image-playground.md) - `metadata-only`
- [2026 237 - What's New In Image Understanding](../sessions/wwdc2026-237-what-s-new-in-image-understanding.md) - `metadata-only`
- [2025 259 - Code-Along: Bring On-Device AI To Your App Using The Foundation Models Framework](../sessions/wwdc2025-259-code-along-bring-on-device-ai-to-your-app-using-the-foundation-models-framework.md) - `metadata-only`
- [2025 301 - Deep Dive Into The Foundation Models Framework](../sessions/wwdc2025-301-deep-dive-into-the-foundation-models-framework.md) - `metadata-only`
- [2025 298 - Explore Large Language Models On Apple Silicon With MLX](../sessions/wwdc2025-298-explore-large-language-models-on-apple-silicon-with-mlx.md) - `metadata-only`
- [2025 248 - Explore Prompt Design & Safety For On-Device Foundation Models](../sessions/wwdc2025-248-explore-prompt-design-safety-for-on-device-foundation-models.md) - `metadata-only`
- [2025 286 - Meet The Foundation Models Framework](../sessions/wwdc2025-286-meet-the-foundation-models-framework.md) - `metadata-only`
- [2025 247 - What's New In Xcode 26](../sessions/wwdc2025-247-what-s-new-in-xcode-26.md) - `metadata-only`

## Synthesis

### What This Page Can Answer

- Whether this feature area appears in the indexed WWDC corpus.
- Which sessions and Apple documentation links are relevant.
- Which claims are backed by deep-researched session notes versus metadata-only indexing.

### Evidence-Backed Claims

- Extend the foundation models framework by implementing a languagemodelexecutor for new models. explore how to interface with the languagemodelsession's transcript, manage session state effectively, and optimize kv cache utilization. find out how to support custom segment types and unlock advanced capabilities for your generative ai features. Source: WWDC 2026 session 339.
- Learn how to take your intelligence features further with foundation models framework primitives for dynamic context and agentic workflows. we'll walk through engineering shared context, setting up privacy boundaries, and managing key value caching. discover how to orchestrate smooth handoffs between local and server models. Source: WWDC 2026 session 242.
- Explore all the new ways to leverage apple foundation models on macos. the foundation models sdk for python lets you integrate with popular tooling and evaluation packages in the python ecosystem. find out how to use the brand new fm command introduced in macos 27 to streamline scripting, automate model workflows, and accelerate your development process. Source: WWDC 2026 session 334.
- Private cloud compute lets you access powerful, frontier-class models while protecting user privacy. explore how it works and how to access it using the foundation models framework. discover best practices for checking availability and handling graceful fallbacks in your apps. Source: WWDC 2026 session 319.
- Learn how to leverage advanced features of the evaluations framework to build robust evaluations for your app. explore evaluating flows with tool calling and dynamic conditions, and how to define what correct behavior means for your use case. discover how to generate synthetic data, use judges effectively, and validate your datasets for reliable results. Source: WWDC 2026 session 299.
- Foundation Models apps need observability because outputs are probabilistic and multi-model pipelines can hide slow or failing steps. Source: WWDC 2026 session 243.
- The Foundation Models Instruments template shows instructions, prompts, responses, errors, sessions, requests, inferences, and tool calls. Source: WWDC 2026 session 243.
- Discover a curated collection of popular open-source models — including qwen, mistral, sam3, and more — optimized for apple silicon using the new core ai framework. learn how to download, run, and benchmark models on your mac, and integrate them into your app with just a few lines of code. explore a new workflow for model compilation and on-device specialization to speed up first-time model load. find out how to profile and optimize runtime performance with core ai tools in xcode. Source: WWDC 2026 session 326.
- Level up basic search into a retrieval-augmented system using spotlightsearchtool and languagemodelsession. explore core spotlight integration, delegate-based hydration patterns, and how metadata quality impacts your search results. learn how to use custom pipelinestages for tasks like sentiment analysis. discover best practices for indexing and building flexible, context-rich search experiences in your app. Source: WWDC 2026 session 246.

### Related APIs And Concepts

- AIModel
- AIModelCache
- ANE
- AppIntent
- BarcodeReaderTool
- BrewingTimerIntent
- CGImage
- CLI
- CSSearchableIndex
- CSSearchableItem
- CodingAssistant
- CoreAILanguageModel
- DeletePhotoIntent
- DynamicProfile
- DynamicSchemas
- EXECutor
- EXECutors
- Evaluations
- FineTuning
- FoundationModels
- Generable
- GenerateCraftIdeaTool
- GenerateCraftIdeasTool
- GitHub
- Guardrails
- GuidanceProfile
- Guide
- Instruments

## Small Observations (Don't Delete)

- This is a neutral feature page, not a recommendation to adopt the feature.
- Prefer deep-researched sessions for strong answers.
- Verify beta SDK names before turning research into code.

<!-- docbot: end -->
