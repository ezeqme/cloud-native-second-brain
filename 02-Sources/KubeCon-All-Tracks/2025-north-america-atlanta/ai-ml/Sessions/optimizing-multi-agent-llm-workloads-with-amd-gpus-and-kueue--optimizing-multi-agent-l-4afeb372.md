---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Yuchen Fama", "Cognality", "Jodie Su", "AMD", "Zhiming Shen", "Exostellar"]
sched_url: https://kccncna2025.sched.com/event/27Fb1/optimizing-multi-agent-llm-workloads-with-amd-gpus-and-kueue-yuchen-fama-cognality-jodie-su-amd-zhiming-shen-exostellar
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+Multi-Agent+LLM+Workloads+With+AMD+GPUs+and+Kueue+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Optimizing Multi-Agent LLM Workloads With AMD GPUs and Kueue - Yuchen Fama, Cognality; Jodie Su, AMD; Zhiming Shen, Exostellar

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: Yuchen Fama, Cognality, Jodie Su, AMD, Zhiming Shen, Exostellar
- Schedule: https://kccncna2025.sched.com/event/27Fb1/optimizing-multi-agent-llm-workloads-with-amd-gpus-and-kueue-yuchen-fama-cognality-jodie-su-amd-zhiming-shen-exostellar
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+Multi-Agent+LLM+Workloads+With+AMD+GPUs+and+Kueue+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Optimizing Multi-Agent LLM Workloads With AMD GPUs and Kueue.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fb1/optimizing-multi-agent-llm-workloads-with-amd-gpus-and-kueue-yuchen-fama-cognality-jodie-su-amd-zhiming-shen-exostellar
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+Multi-Agent+LLM+Workloads+With+AMD+GPUs+and+Kueue+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XiuqiIpGoOg
- YouTube title: Optimizing Multi-Agent LLM Workloads With AMD GPUs and Kueue - Yuchen Fama, Jodie Su & Zhiming Shen
- Match score: 0.859
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/optimizing-multi-agent-llm-workloads-with-amd-gpus-and-kueue/XiuqiIpGoOg.txt
- Transcript chars: 25297
- Keywords: gpu, actually, cluster, memory, background, resource, running, fractional, workloads, agents, allocate, request, workload, solution, output, second, workflow, workflows

### Resumo baseado na transcript

This is Yuchan CEO of uh um sorry [laughter] cognality and uh I have my co-speakers today uh Jodi Su from uh AMD um senior manager of engineering and also Jim Shen CTO of AXeller. So the model application layer, the hardware acceleration layer and the infrastructure orchestration layer. Now with agentic workflow it becomes a compound system with more challenges for disregulated serving and also the composible automation. In fact, most of the business problems can be solved by simple prompt chaining and structured output. So for this demo, we're going to use a really kind of a simplest most commonly used prompt chaining, which is also the building block for the right side system. Now the problem we're trying to focus today is actually one simple question.

### Excerpt da transcript

Good afternoon everyone. Thanks for coming. This is Yuchan CEO of uh um sorry [laughter] cognality and uh I have my co-speakers today uh Jodi Su from uh AMD um senior manager of engineering and also Jim Shen CTO of AXeller. It really takes a village to optimize LM serving stacks. Each of us represent a different layer of the stack. So the model application layer, the hardware acceleration layer and the infrastructure orchestration layer. We hope this cross layer close collaboration model in the open ecosystem continue to drive the full stack optimization from hardware to software. So as we all know AI workloads are extremely heterogeneous from small and mighty models to really large ones with meaningful trade-off and this is slide is just a one-dimensional view um with the model size even for the same size model different request shapes like token distribution prompt structure coming in batches can create this really bursty unpredictable traffic burst and resource pottex. For example, you may have um rag that has super long input including both the prompt and retrieve docs but short output.

On the other hand, you may also have um reasoning agents with short and media input but super long output. And on top of everything, you may have mission critical production models running and a lower priority experiments causing resource contentions. Now with agentic workflow it becomes a compound system with more challenges for disregulated serving and also the composible automation. So let's have a quick refresher. When we talk about agentic workflows it typically falls into two patterns. On the left humans are in control defining deterministic code path and chaining different tools and models. On the right, LMS are in control dynamically planning, reasoning and calling uh tools autonomously. So most production system actually use more reliable workflow patterns on the left. In fact, most of the business problems can be solved by simple prompt chaining and structured output. So for this demo, we're going to use a really kind of a simplest most commonly used prompt chaining, which is also the building block for the right side system.

Now the problem we're trying to focus today is actually one simple question. How do we free up more GPU resources so we can pack more workloads such as collocating tightly coupled agents on the same AMD GPU? We solve this problem by fine grain fractionalization uh at the gigabyte level granularity and also combined with Q start with a K
