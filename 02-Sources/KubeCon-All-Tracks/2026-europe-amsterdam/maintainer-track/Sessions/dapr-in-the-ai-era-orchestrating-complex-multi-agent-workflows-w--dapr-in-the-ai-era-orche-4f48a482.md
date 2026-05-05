---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Yaron Schneider", "Diagrid"]
sched_url: https://kccnceu2026.sched.com/event/2EF4R/dapr-in-the-ai-era-orchestrating-complex-multi-agent-workflows-with-automatic-recovery-yaron-schneider-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Dapr+in+the+AI+Era%3A+Orchestrating+Complex+Multi-agent+Workflows+With+Automatic+Recovery+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Dapr in the AI Era: Orchestrating Complex Multi-agent Workflows With Automatic Recovery - Yaron Schneider, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yaron Schneider, Diagrid
- Schedule: https://kccnceu2026.sched.com/event/2EF4R/dapr-in-the-ai-era-orchestrating-complex-multi-agent-workflows-with-automatic-recovery-yaron-schneider-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Dapr+in+the+AI+Era%3A+Orchestrating+Complex+Multi-agent+Workflows+With+Automatic+Recovery+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Dapr in the AI Era: Orchestrating Complex Multi-agent Workflows With Automatic Recovery.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4R/dapr-in-the-ai-era-orchestrating-complex-multi-agent-workflows-with-automatic-recovery-yaron-schneider-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Dapr+in+the+AI+Era%3A+Orchestrating+Complex+Multi-agent+Workflows+With+Automatic+Recovery+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9gejXxl5JzE
- YouTube title: Dapr in the AI Era: Orchestrating Complex Multi-agent Workflows With Automatic... Yaron Schneider
- Match score: 0.996
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/dapr-in-the-ai-era-orchestrating-complex-multi-agent-workflows-with-au/9gejXxl5JzE.txt
- Transcript chars: 29288
- Keywords: agents, workflow, workflows, essentially, basically, talking, running, actually, llm, pretty, frameworks, everything, langgraph, process, framework, another, systems, important

### Resumo baseado na transcript

I'm one of the co-creators of the Dapr project together with this fine gentleman here um called Mark and uh steering committee member and also very recently elected as the chair for the workflow working group inside of the agenda KI Foundation. That was a very long intro, but what I really like to do is make agents run reliably in production. It's fairly lightweight um and yes, it will allow you to essentially just hand over to Dapr all of those hard distributed systems challenges you to deal with the thing you want to do the most which is to deliver software. All the rest of the metrics here are vanity metrics that we like to show because they're nice um and they just make the slide more dramatic, but really the thing that we care about as maintainers are the contributors and our Discord community. Um there's lots of really interesting talks there about distributed systems problems in general and yes, you can talk to me there, too. I assume we're all running in Kubernetes or at least some of us are moving towards Kubernetes and you know, we know the notions of pods.

### Excerpt da transcript

Yep. Okay, let's get started. Everyone, thank you for coming to my talk today. My name is Yaron Schneider. I'm a CTO and co-founder of Dapr Grid. I'm one of the co-creators of the Dapr project together with this fine gentleman here um called Mark and uh steering committee member and also very recently elected as the chair for the workflow working group inside of the agenda KI Foundation. That was a very long intro, but what I really like to do is make agents run reliably in production. That's what I do nowadays, believe it or not. Um I spend most of my time talking to people and trying to explain to them why it's a bad thing that their agent loses all of its state if it goes down and how much money they're going to have to pay when it basically picks back up and it's going to have to go through those 100 LLM calls over and over again. Um so today we'll be talking about ways in which the Dapr project can help you basically work around through all of those limitations that we see in um in risks when it comes to AI today.

So if you don't know Dapr, Dapr has been around since um the beginning of 2019. We donated it to CNCF when we worked at Microsoft um Mark and I and it became a graduated project in 2021. Um it is a set of APIs for developers to be able to focus on business logic and not infrastructure gluing and plumbing and interaction. It contains many building blocks and APIs today um and definitely the one that attracts the most attention is the workflows one which is in the uh top left there. We cannot talk about all of them today. We have a very short session but today we'll specifically be talking about how those workflows really play into agenda KI and AI agents. Um you can come into Dapr from any language. So as long as your language can talk HTTP, you can uh use Dapr. You can run it anywhere on your local machine, uh Linux, Mac, Windows. You can run it in any cloud. You can run it on a VM if even if you want to. It's fairly lightweight um and yes, it will allow you to essentially just hand over to Dapr all of those hard distributed systems challenges you to deal with the thing you want to do the most which is to deliver software.

We are a very big community. We're coming up at 9,000 Discord members. We have almost 5,000 individual contributors which is great. All the rest of the metrics here are vanity metrics that we like to show because they're nice um and they just make the slide more dramatic, but really the thing that we care about as mainta
