---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "Community Governance"]
speakers: ["Yaron Schneider", "Diagrid", "Roberto Rodriguez", "CyberChasquis"]
sched_url: https://kccnceu2025.sched.com/event/1tcyT/dapr-in-2025-durable-execution-for-agenticai-systems-and-becoming-the-backbone-of-app-platforms-yaron-schneider-diagrid-roberto-rodriguez-cyberchasquis
youtube_search_url: https://www.youtube.com/results?search_query=Dapr+in+2025%3A+Durable+Execution+for+AgenticAI+Systems+and+Becoming+the+Backbone+of+App+Platforms+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Dapr in 2025: Durable Execution for AgenticAI Systems and Becoming the Backbone of App Platforms - Yaron Schneider, Diagrid & Roberto Rodriguez, CyberChasquis

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Yaron Schneider, Diagrid, Roberto Rodriguez, CyberChasquis
- Schedule: https://kccnceu2025.sched.com/event/1tcyT/dapr-in-2025-durable-execution-for-agenticai-systems-and-becoming-the-backbone-of-app-platforms-yaron-schneider-diagrid-roberto-rodriguez-cyberchasquis
- Busca YouTube: https://www.youtube.com/results?search_query=Dapr+in+2025%3A+Durable+Execution+for+AgenticAI+Systems+and+Becoming+the+Backbone+of+App+Platforms+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Dapr in 2025: Durable Execution for AgenticAI Systems and Becoming the Backbone of App Platforms.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyT/dapr-in-2025-durable-execution-for-agenticai-systems-and-becoming-the-backbone-of-app-platforms-yaron-schneider-diagrid-roberto-rodriguez-cyberchasquis
- YouTube search: https://www.youtube.com/results?search_query=Dapr+in+2025%3A+Durable+Execution+for+AgenticAI+Systems+and+Becoming+the+Backbone+of+App+Platforms+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y21i3lG2jUM
- YouTube title: Dapr in 2025: Durable Execution for AgenticAI System... Yaron Schneider, Diagrid & Roberto Rodriguez
- Match score: 0.76
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dapr-in-2025-durable-execution-for-agenticai-systems-and-becoming-the/y21i3lG2jUM.txt
- Transcript chars: 39569
- Keywords: dapper, agents, actually, workflows, workflow, orchestrator, concept, essentially, agentic, pattern, multiple, trying, course, execute, pretty, systems, define, llm

### Resumo baseado na transcript

Uh my name is Schneider, core maintainer of the Dapper project, streaming committee member, also uh CTO co-founder at DIG Grid. Um, I'm also a new Dapper maintainer, creator of the Dapper Agents project, and I'm also part of the Nvidia uh team. Um, and then fire those off to a machine learning model that decides if the suit needs fixing. And on top of that, we add enterprise features like sensitive data offiscation which means if you want to make sure that the user prompt, which can really be anything, doesn't contain any sort of personal information like credit card numbers, um social security numbers, names, emails, Dapper will do that for you. You can essentially use it to do anything from data processing to notifications to timers and reminders to even writing your own Kubernetes like server and also AI agentic systems which we will cover more in this talk. So this can lower costs you if you have IO operations or you're hitting you know things like LM providers for example which cause you to pay Dapper will make sure that well that just doesn't happen because it will not kick off again uh

### Excerpt da transcript

Okay, I think we'll get started. Hello everyone. Maybe don't have to use the mic. Can you hear me in the back? All right. Hi. I do for stream. Yes. Sorry people watching online. I apologize. Uh my name is Schneider, core maintainer of the Dapper project, streaming committee member, also uh CTO co-founder at DIG Grid. And together with me we have Roberto. Yes. So my name is Roberto Rodriguez. Um, I'm also a new Dapper maintainer, creator of the Dapper Agents project, and I'm also part of the Nvidia uh team. Um, so I'm going to be doing how to enable autonomy, how to enable AI agents into security operations to defend Nvidia's, you know, products. Okay, I'm going to take the first section of our talk. Let's start with community updates. The Dapper project has been through a lot. uh it's gained new contributors, new end users. Um and one of the most important things that we've seen during the last year is that now we're a graduated CNCF project since November 12 uh 2024. And this is really a testament to the validity of the project, it's broad user adoption, the number of contributors that are contributing to the project and um it's been a a journey to get there.

But if you ever contributed to Dapper, opened an issue, communicated with maintainers, you have our thanks. Um, beyond this, we are one of the fastest growing projects in CNCF, currently 14th largest, over 700,000 Docker hub pools a month. Uh, more than 300,000 unique doc views. And our Discord community recently surpassed 8,000 members, and we're closing up on 4,000 individual contributors. This is great. And, um, beyond all that, the most important thing for us is to actually measure end user adoption. So, this has been pretty much off the charts. Um the Python SDK grew 151% I believe um year-over-year uh which is very much fueled by AI workloads that we'll talk about in a second. Umnet continues to see almost I I think it's actually over 200,000 uh downloads per week now um which is pretty great and of course we have other languages using Dapper but we don't have uh great ways to track them. This is obviously public metrics that we're taking. Um we're seeing amazing uh use cases. This is my own personal favorite.

NASA running Dapper on the International Space Station. Um, what it's doing there is Dapper is being used as the message bus layer to take pictures of astronaut suits. Um, and then fire those off to a machine learning model that decides if the suit needs fixing. In this case, we can see
