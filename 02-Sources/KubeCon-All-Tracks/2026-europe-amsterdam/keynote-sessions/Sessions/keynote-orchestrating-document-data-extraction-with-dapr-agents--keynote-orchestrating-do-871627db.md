---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["AI ML", "Storage Data"]
speakers: ["Fabian Steinbach", "Software Architect", "ZEISS"]
sched_url: https://kccnceu2026.sched.com/event/2HgFV/keynote-orchestrating-document-data-extraction-with-dapr-agents-fabian-steinbach-software-architect-zeiss
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Orchestrating+Document+Data+Extraction+with+Dapr+Agents+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Keynote: Orchestrating Document Data Extraction with Dapr Agents - Fabian Steinbach, Software Architect, ZEISS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Fabian Steinbach, Software Architect, ZEISS
- Schedule: https://kccnceu2026.sched.com/event/2HgFV/keynote-orchestrating-document-data-extraction-with-dapr-agents-fabian-steinbach-software-architect-zeiss
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Orchestrating+Document+Data+Extraction+with+Dapr+Agents+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Keynote: Orchestrating Document Data Extraction with Dapr Agents.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgFV/keynote-orchestrating-document-data-extraction-with-dapr-agents-fabian-steinbach-software-architect-zeiss
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Orchestrating+Document+Data+Extraction+with+Dapr+Agents+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9QXoL0ZYDn8
- YouTube title: Keynote: Orchestrating Document Data Extraction with Dapr Agents - Fabian Steinbach
- Match score: 0.961
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/keynote-orchestrating-document-data-extraction-with-dapr-agents/9QXoL0ZYDn8.txt
- Transcript chars: 2274
- Keywords: models, workflow, agents, results, change, documents, everything, needed, process, capability, production, control, reliability, flexibility, durable, llm, second, better

### Resumo baseado na transcript

So, to manufacture precision lenses, you need structured optical data, but sometimes all we have is a photo of a hand-scribbled note. Think about handwritten notes, typed forms, and everything across multiple languages and writing systems. And having comparable recognition results, on par recognition results, with a specialized machine learning system.

### Excerpt da transcript

Hi, I'm Fabian, software architect at Zeiss. So, to manufacture precision lenses, you need structured optical data, but sometimes all we have is a photo of a hand-scribbled note. So, these documents we receive aren't standardized at all. Think about handwritten notes, typed forms, and everything across multiple languages and writing systems. Basically, everything you get from your doctor. But, extracting the data accurately is critical. Wrong data, wrong lens. So, we needed a way to extract the data reliably and automa- automated process. Turns out, modern models are surprisingly good at interpreting these documents, but to bring that capability into production, we needed three things: control, reliability, and flexibility. That's what Dapr Agents gave us. First, control. In our case, we didn't want some kind of fully autonomous agent generate unpredictable results. So, we constrained the AI using a durable workflow. Preprocessing, OCR, and then some generic LLM or agent calls. Second, reliability. With Dapr Agents durable workflow capability, um state is persisted after each step.

If something goes wrong midway through, the process doesn't start over again. So, an expensive, already completed OCR task doesn't run again. That saves time and cost. And third, flexibility. Even when the model landscape changes, the workflow should stay stable. With Dapr A- so, if a better or cheaper model appears tomorrow, we can use Dapr's conversation building block and just change the configuration. No No code change required. So, what are our three key takeaways from that? First, constrain the AI. For us, it worked way better constraining the AI with a workflow instead of just letting it run wild. Second, don't use a hammer for a screw. In our case, we mixed specialized models, general LLMs, with deterministic logic. Don't use an LLM where a function could do the job. And third, decouple. Change models via config, not code. That allows you use always the newest and best models. So, and that entire thing allowed us to go from prototype to production in two months with zero label training data required.

And having comparable recognition results, on par recognition results, with a specialized machine learning system. Thank you very much. >> [applause]
